import re


def is_dunder_wrapper():
    # avoid global variable
    dunder_regex = re.compile('__[a-zA-Z0-9]+__')

    def is_dunder(attr):
        """dunder method starts with two underscores and ends with two
        underscores not three or four. So maybe using `(attr.startswith('__')
        and attr.endswith('__))` is wrong.`
        >>> is_dunder('__valid__')
        True
        >>> is_dunder('no_underscores')
        False
        >>> is_dunder('___three_underscores__')
        False
        >>> is_dunder('__*invalid*__')
        False
        """
        if dunder_regex.match(attr):
            return True
        return False
    return is_dunder


is_dunder = is_dunder_wrapper()


# VOID is a special constant
VOID = type('VOID', (object,), {})()


def navigate(obj, attr_path):
    """get the final attribute, will raise AttributeError when attr not exists
    >>> navigate(dict(), '__class__.__name__')
    'dict'
    """
    attrs = attr_path.split('.')
    target = obj

    for attr in attrs:
        target = getattr(target, attr)

    return target


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
