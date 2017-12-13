class Term:

    def to_sql(self):
        raise NotImplementedError()


class Field(Term):

    def __init__(self, name, table=None):
        self.name = name
        self.table = table

    @property
    def tables_(self):
        return {self.table, }

    def to_sql(self, with_alias=False, with_namespace=False,
               quote_char=None, **kwargs):
        if self.table and (with_namespace or self.table.alias):
            field_sql = "{quote}{namespace}{quote}.{quote}{name}{quote}".format(  # noqa
                namespace=(self.table.alias or self.table.table_name),
                name=self.name,
                quote=quote_char or '',
            )
        else:
            field_sql = "{quote}{name}{quote}".format(
                name=self.name,
                quote=quote_char or '',
            )

        return field_sql
