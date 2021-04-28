"""Custom assertions"""


def assert_raises(exception_type, func, *args, **kwargs):
    """Asserts the function called with params raises exception of given type

    Args:
        exception_type: type/class of the expected exception
        func: function to call
        *args: set of positional arguments to feed to func
        **kwargs: set of keyword arguments to feed to func

    Returns:
        None

    Raises:
        AssertionError

    """
    try:
        func(*args, **kwargs)
    except exception_type:
        return
    except BaseException as e:
        raise AssertionError(
            f'Wrong Exception raised. Expected {exception_type.__name__}, got {type(e).__name__}.')
    raise AssertionError(f'Expected Exception {exception_type.__name__} but nothing raised')
