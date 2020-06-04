def configure_grpc_error(context, rpc_error):
    """
    Sets proper error details and code on context

    Args:
        context (grpc.Context)
        rpc_error (grpc.RpcError)
    """
    context.set_details(rpc_error.details())
    context.set_code(rpc_error.code())
