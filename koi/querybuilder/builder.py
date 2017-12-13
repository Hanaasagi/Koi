from koi.utils import builder, ignoredeepcopy
from .terms import Field


class Table:

    def __init__(self, table_name):
        self.table_name = table_name

    def to_sql(self, quote_char=None, **kwargs):
        table_sql = "{quote}{name}{quote}".format(
            name=self.table_name,
            quote=quote_char or ''
        )

        return table_sql

    @ignoredeepcopy
    def __getattr__(self, name):
        return Field(name)

    def __str__(self):
        return self.to_sql(quote_char='"')


class QueryBuilder:

    traits = []

    def __init__(self):
        self._from = []
        self._columns = []
        self._selects = []
        self._distinct = False

    @builder
    def from_(self, table):
        self._from.append(table)

    @builder
    def select(self, *terms):
        for term in terms:
            self._select_field(term)

    def _select_field(self, term):
        self._selects.append(term)

    def to_sql(self, **kwargs):
        kwargs['with_namespace'] = kwargs.get('with_namespace', False)
        querystring = ''
        querystring += self._select_sql(**kwargs)
        if self._from:
            querystring += self._from_sql(**kwargs)
        return querystring

    def _from_sql(self, subquery=None, with_alias=None, with_unions=None, **kwargs):
        return ' FROM {selectable}'.format(
            selectable=','.join(
                clause.to_sql(
                    subquery=True,
                    with_alias=kwargs['with_namespace'],
                    with_unions=True,
                    **kwargs
                ) for clause in self._from
            )
        )

    def _select_sql(self, **kwargs):
        return 'SELECT {distinct}{select}'.format(
            distinct='DISTINCT ' if self._distinct else '',
            select=','.join(
                term.to_sql(
                    with_alias=True,
                    **kwargs
                ) for term in self._selects
            )
        )
