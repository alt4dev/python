# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from alt4.proto import definitions_pb2 as definitions__pb2


class LoggingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WriteLog = channel.unary_unary(
                '/proto.Logging/WriteLog',
                request_serializer=definitions__pb2.Log.SerializeToString,
                response_deserializer=definitions__pb2.Result.FromString,
                )
        self.WriteAuditLog = channel.unary_unary(
                '/proto.Logging/WriteAuditLog',
                request_serializer=definitions__pb2.AuditLog.SerializeToString,
                response_deserializer=definitions__pb2.Result.FromString,
                )
        self.AuditQuery = channel.unary_unary(
                '/proto.Logging/AuditQuery',
                request_serializer=definitions__pb2.Query.SerializeToString,
                response_deserializer=definitions__pb2.QueryResult.FromString,
                )


class LoggingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WriteLog(self, request, context):
        """Creates a log
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteAuditLog(self, request, context):
        """Creates an audit log
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuditQuery(self, request, context):
        """Query audit logs for reporting or something
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LoggingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WriteLog': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteLog,
                    request_deserializer=definitions__pb2.Log.FromString,
                    response_serializer=definitions__pb2.Result.SerializeToString,
            ),
            'WriteAuditLog': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteAuditLog,
                    request_deserializer=definitions__pb2.AuditLog.FromString,
                    response_serializer=definitions__pb2.Result.SerializeToString,
            ),
            'AuditQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.AuditQuery,
                    request_deserializer=definitions__pb2.Query.FromString,
                    response_serializer=definitions__pb2.QueryResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.Logging', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Logging(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WriteLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Logging/WriteLog',
            definitions__pb2.Log.SerializeToString,
            definitions__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteAuditLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Logging/WriteAuditLog',
            definitions__pb2.AuditLog.SerializeToString,
            definitions__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuditQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Logging/AuditQuery',
            definitions__pb2.Query.SerializeToString,
            definitions__pb2.QueryResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
