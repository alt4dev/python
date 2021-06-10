import ssl
import grpc
import socket
from alt4.proto.definitions_pb2_grpc import LoggingStub
from datetime import datetime

global client
global dt


def get_client(reuse_client=True):
    """
    Get a GRPC logging client

    Args:
        reuse_client: Reuse the client in memory or create a new one.

    Returns: LoggingStub
    """
    global client
    global dt
    # Return cached client
    if "client" in globals() and reuse_client:
        return client, dt

    credentials = grpc.ssl_channel_credentials(get_server_credentials().encode("utf-8"))
    channel = grpc.secure_channel("rpc.alt4.dev", credentials)
    client = LoggingStub(channel)
    dt = datetime.now().timestamp()
    return client, dt


def get_server_credentials(hostname="rpc.alt4.dev", port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as conn:
        with context.wrap_socket(conn, server_hostname=hostname) as sock:
            cert = sock.getpeercert(True)
    return ssl.DER_cert_to_PEM_cert(cert)
