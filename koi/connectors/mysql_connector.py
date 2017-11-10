from koi.connections import MySQLConnection
from koi.connectors import Connector
from koi.exceptions import DriverNotSupport, ReadOnly
from koi.utils.dynamic_import import import_class


class MySQLConnector(Connector):

    _connection_cls = MySQLConnection

    driver_mapping = {
        'pymysql': import_class('koi.drivers.mysql.pymysql.driver'),
    }

    def __init__(self, config):
        self._driver = self._dispatch(config.pop('driver'))
        self._config = config
        self.connect()

    def _dispatch(self, driver_name):
        driver = self.driver_mapping.get(driver_name)
        if driver is None:
            raise DriverNotSupport(driver_name)
        return driver

    def connect(self):
        self._connection = self._connection_cls(
            self.driver.connect(self._config))

    def reconnect(self):
        pass

    def ping(self):
        pass

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, new_driver):
        raise ReadOnly("driver attribute is read only")

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, new_connection):
        raise ReadOnly("connection attribute is read only")

    def __getattr__(self, attr):
        return getattr(self._connection)
