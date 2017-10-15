class Connection:
    """Define what behavior a Connection object should have"""

    def __init__(self):
        pass

    def exec(self, statement):
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
