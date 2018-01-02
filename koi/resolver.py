from koi.objproxy import Proxy

_resolver = None


def set_connection_resolver(db):
    global _resolver
    _resolver = db


current_resolver = Proxy(lambda: _resolver)

__all__ = [
    'set_connection_resolver',
    'current_resolver',
]
