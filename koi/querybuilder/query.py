from .builder import Builder


class Query:

    @classmethod
    def _builder(cls):
        return Builder()

    @classmethod
    def from_(cls, table):
        return cls._builder().from_(table)

    @classmethod
    def into(cls, table):
        return cls._builder().into(table)

    @classmethod
    def select(cls, *terms):
        return cls._builder().select(*terms)

    @classmethod
    def update(cls, table):
        return cls._builder().update(table)
