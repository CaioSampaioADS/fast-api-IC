import pymysql


def conectar():
    return pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='provas',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)