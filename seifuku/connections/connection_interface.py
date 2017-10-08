class ConnectionInterface(object):
    """ Define what behavior a Connection object should have """

    def exec(self):
        """execute SQL statement"""

        raise NotImplementedError()

    def transaction(self):
        """subclass should implement as a context manager"""

        raise NotImplementedError()

    def begin(self):
        """begin transaction"""

        raise NotImplementedError()

    def commit(self):
        """commit transaction"""

        raise NotImplementedError()

    def rollback(self):
        """rollback transaction"""

        raise NotImplementedError()
