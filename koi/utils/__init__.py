import copy


def builder(func):

    def _copy(self, *args, **kwargs):
        self_copy = copy.deepcopy(self)
        func(self_copy, *args, **kwargs)
        return self_copy

    return _copy


__all__ = [
    'builder',
]
