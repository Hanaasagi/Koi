from copy import deepcopy
from koi.connectors import strategies
from koi.utils.datatypes import Config
from koi.exceptions import ConfigError


class DatabaseManager:

    _connectors = {}
    _default_connector = None

    def __init__(self, config):
        if isinstance(config, dict):
            self.config = Config.from_dict(config)
        else:
            self.config = Config.from_object(config)
        self._init_connector()

    def get_connection(self):
        return {name: connector.connection
                for name, connector in self._connectors.items()}

    def _init_connector(self):
        default_db_name, default_db_config = self._get_default_db()
        self._default_connector = strategies[default_db_name](
            default_db_config)

        for db_name, db_config in self.config.items():
            self._connectors[db_name] = strategies[db_name](db_config)
            if db_name == default_db_name:
                self._default_connector = self._connectors[db_name]

    @property
    def connection(self):
        return self._default_connector.connection

    def _get_default_db(self):
        default = self.config.get('default')
        if default is not None:
            return default, self.config[default]
        if len(self.config) > 1:
            raise ConfigError("multiple db should set default")
        return deepcopy(self.config).popitem()
