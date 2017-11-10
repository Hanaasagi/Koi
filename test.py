config = {
    'mysql': {
        'read': {
            'host': '192.168.1.1'
        },
        'write': {
            'host': '192.168.1.2'
        },
        'driver': 'pymysql',
        'database': 'database',
        'username': 'root',
        'password': '',
        'prefix': ''
    }
}

from koi import DatabaseManager

db = DatabaseManager(config)
