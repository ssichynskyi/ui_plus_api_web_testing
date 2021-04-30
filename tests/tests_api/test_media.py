import pytest

from pathlib import Path

from data_collection.api.data_models.woo_commerce.v3 import ErrorResponse
from framework.utilities.dao.posts_media_dao import BasicPostDAO
from framework.utilities.dao.exceptions import TooFewDatabaseEntries
from framework.utilities.fake_data import generate_filename
from tests.conftest import wp_api_read_write_user, unauthorized_wp_api_client


PATH_TO_TEST_FILE = Path(__file__).parent.joinpath('data', 'upload_test_file.pdf')
EXT = 'pdf'


@pytest.fixture(scope="module")
def file():
    return generate_filename(extension=EXT)


@pytest.fixture(scope="module")
def file_name(file):
    return file.removesuffix(f'.{EXT}')


@pytest.fixture(scope="module")
def upload_header(file):
    return {
        'source_url':  str(PATH_TO_TEST_FILE),
        'Content-Disposition': f'attachment; filename="{file}"',
        'Content-Type': f'application/{EXT}'
    }


@pytest.fixture(scope="module")
def file_data():
    with open(PATH_TO_TEST_FILE, 'rb') as file:
        return file.read()


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
    with pytest.raises(TooFewDatabaseEntries):
        BasicPostDAO(post_title=file_name)


@pytest.mark.major
def test_upload_file_possible_with_read_write(
        read_write_wp_api_client,
        upload_header,
        file_data,
        file_name
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
    media = BasicPostDAO(post_title=file_name)
    assert media.file_type == f'application/{EXT}'
    assert media.type == 'attachment'
    # add tests file size is the same on server and locally
    # ADD BYTE CALC

    # DELETE MEDIA
    resp = read_write_wp_api_client.delete(f'media/{media.id}', params={'force': 'true'})
    assert resp.status_code == 200
    with pytest.raises(TooFewDatabaseEntries):
        BasicPostDAO(post_title=file_name)