class HideIntrospectMiddleware:
    """
    This middleware should use for production mode. This class hide the
    introspection.
    """

    @classmethod
    def resolve(cls, next, root, info, **args):
        if info.field_name == '__schema':
            return None
        return next(root, info, **args)


def build_middleware():
    return [HideIntrospectMiddleware()]
