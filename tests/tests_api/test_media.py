import hashlib
import os
import pytest
from urllib.request import urlretrieve

from pathlib import Path

from data_collection.api.data_models.woo_commerce.v3 import ErrorResponse
from framework.utilities.dao.dao_helpers import generate_dao_objects
from framework.utilities.dao.posts_dao import PostDao
from framework.utilities.fake_data import generate_filename


PATH_TO_TEST_DATA = Path(__file__).parent.joinpath('data')
PATH_TO_TEST_FILE = Path(PATH_TO_TEST_DATA).joinpath('upload_test_file.pdf')
EXT = 'pdf'


@pytest.fixture(scope="module")
def file():
    yield generate_filename(extension=EXT)


@pytest.fixture(scope="module")
def file_name(file):
    yield file.removesuffix(f'.{EXT}')


@pytest.fixture(scope="module")
def upload_header(file):
    yield {
        'source_url':  str(PATH_TO_TEST_FILE),
        'Content-Disposition': f'attachment; filename="{file}"',
        'Content-Type': f'application/{EXT}'
    }


@pytest.fixture(scope="module")
def file_data():
    with open(PATH_TO_TEST_FILE, 'rb') as file:
        yield file.read()


@pytest.fixture(scope="module")
def download_file(file_name) -> tuple:
    """Downloads file if possible.

    Note:
        construction with inner function and yielding it
        is done in order to pass variable arguments to a fixture

    Returns:
        (file_path, http_status_code)
    """
    file_path = PATH_TO_TEST_DATA.joinpath(f'{file_name}.{EXT}')

    def process_with_params(*args, **kwargs):
        return urlretrieve(
            *args,
            filename=file_path,
            **kwargs
        )

    yield process_with_params
    if file_path.exists():
        os.remove(file_path)


def files_identical(path1: Path, path2: Path) -> bool:
    """Compares files using md5 checksum"""
    with open(path1, 'rb') as f1, open(path2, 'rb') as f2:
        f1 = f1.read()
        f2 = f2.read()
    if hashlib.md5(f1).hexdigest() == hashlib.md5(f2).hexdigest():
        return True
    return False


@pytest.mark.major
def test_upload_file_impossible_with_unauthorized(
        unauthorized_wp_api_client,
        upload_header,
        file_data,
        file_name
):
    resp = unauthorized_wp_api_client.post('media', headers=upload_header, data=file_data)
    assert resp.status_code == 401
    ErrorResponse(**resp.json())
    media = generate_dao_objects(PostDao, PostDao.TABLE,
                                 filter_criteria={'post_title': file_name})
    assert len(media) == 0


@pytest.mark.slow
@pytest.mark.major
def test_upload_file_possible_with_read_write(
        read_write_wp_api_client,
        upload_header,
        file_data,
        file_name,
        download_file
):
    # This looks like WP problem.
    # File is uploaded successfully but connection forcibly closed by the remote host
    # Apache server logs shows only "child process exited with status 3221226505"
    from requests.exceptions import ConnectionError
    try:
        resp = read_write_wp_api_client.post('media', headers=upload_header, data=file_data)
    except ConnectionError:
        pass
    # Temporary not possible to make an assertion below because of no response
    # assert resp.status_code == 200
    media = generate_dao_objects(
        PostDao, PostDao.TABLE,
        filter_criteria={'post_title': file_name}
    )
    assert len(media) == 1
    assert media[0].file_type == f'application/{EXT}'
    assert media[0].type == 'attachment'

    # Verify that file on the server is the same as test data file
    verification_file, _ = download_file(media[0].guid)
    assert files_identical(verification_file, PATH_TO_TEST_FILE) is True
    # DELETE MEDIA
    resp = read_write_wp_api_client.delete(f'media/{media[0].id}', params={'force': 'true'})
    assert resp.status_code == 200, read_write_wp_api_client.get_http_error_message(resp)
    media = generate_dao_objects(PostDao, PostDao.TABLE,
                                 filter_criteria={'post_title': file_name})
    assert len(media) == 0
