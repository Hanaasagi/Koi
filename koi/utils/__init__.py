import copy


def builder(func):

    def _copy(self, *args, **kwargs):
        self_copy = copy.deepcopy(self)
        func(self_copy, *args, **kwargs)
        return self_copy

    return _copy


def ignoredeepcopy(func):
    def _getattr(self, name):
        if name in ('__deepcopy__', '__getstate__',
                    '__setstate__', '__getnewargs__'):
            raise AttributeError(
                "'%s' object has no attribute '%s'" % (self.__class__.__name__,
                                                       name))

        return func(self, name)

    return _getattr


__all__ = [
    'builder',
    'ignoredeepcopy',
]
