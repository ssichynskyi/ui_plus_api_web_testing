import socket


def assert_connection(ip_address: str, port: int, timeout: int = 2) -> None:
    """Checks the given host and port for accessibility

    Args:
        ip_address: IP address as string. Format: '127.0.0.1'
        port: port number, int
        timeout: number of seconds to wait

    Returns:
        None

    Raises:
        ConnectionError - if not possible to establish connection in
            a given timeout

    """
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with test_socket:
        test_socket.settimeout(timeout)
        try:
            test_socket.connect((ip_address, port))
        except BaseException as e:
            msg = f'Not possible to connect to host {ip_address}:{port}'
            raise ConnectionError(msg) from e
