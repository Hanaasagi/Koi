class MySQLDriver_pymysql:
    driver = 'pymysql'

    def connect(config):
        pymysql = __import__('pymysql')
        return pymysql.connect(**config.data)


driver = MySQLDriver_pymysql
