import asyncio


class DatabaseManager:

    database = None

    def __init__(self, database=None, *, loop=None):
        if not any(database, self.database):
            raise Exception

        self.database = database or self.database
        self._conn = None
        if not loop:
            loop = asyncio.get_event_loop()
        self._loop = loop

    @property
    def is_connected(self):
        """"""

    @property
    def loop(self):
        return self._loop

    @property
    def connection(self):
        return self._conn

    async def connect(self):
        self._conn= await self.database.connect(loop=self.loop)

    async def close(self):
        await self.connection.close()
