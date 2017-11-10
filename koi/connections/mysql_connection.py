from koi.connections.connection import Connection


class MySQLConnection(Connection):

    name = 'mysql'

    def exec(self, statement):
        pass

    def begin(self):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass
