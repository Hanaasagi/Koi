from collections import UserDict
from seifuku.utils.helpers import is_dunder

# for mypy
from typing import Any, Hashable


class Config(UserDict):
    """
    >>> class T:
    ...     VAR = 1
    ...     BAR = 2
    >>> config = Config.from_object(T)
    >>> config['VAR'] == 1
    True
    >>> config.BAR == 2
    True
    >>> nested_dict = {
    ...     'mysql': {
    ...         'driver': 'pymysql'
    ...     }
    ... }
    >>> config = Config.from_dict(nested_dict)
    >>> config.mysql.driver
    'pymysql'
    """
    @classmethod
    def from_object(cls, obj: Any):
        """collect all upper attrribute from object and generate a dict"""
        config = cls()
        for attr in dir(obj):
            if (not is_dunder(attr)) and attr.isupper():
                config.data[attr] = getattr(obj, attr)
        return config

    @classmethod
    def from_dict(cls, data_dict: dict):
        config = cls()
        for key, value in data_dict.items():
            if isinstance(value, dict):
                config[key] = cls.from_dict(value)
            else:
                config[key] = value
        return config

    def __getattr__(self, attr: str) -> Any:
        return self.data[attr]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
