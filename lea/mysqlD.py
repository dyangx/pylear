import pymysql as pymysql

@staticmethod
def get_conn():
    url = "152.136.190.118"
    conn = pymysql.connect(user="root", passwd="mysql88", db="test", host=url, port=33061)
    return conn

def con_mysql():
    url = "152.136.190.118"
    conn = pymysql.connect(user="root",passwd="mysql88",db="test",host=url,port=33061)

    cursor = conn.cursor()
    sql = "SELECT * from test3 where 1 = {}".format(1)
    values = query(sql)
    for val in values:
        print(val)

    sql2 = "update test3 set addr = {} where id = 1".format("'帆帆帆帆'")
    update(sql2)

def query(sql):
    conn = get_conn()
    cursor = conn.cursor()
    print("this is sql:  ",sql)
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor.close()
    conn.close()

    return values

def update(sql):
    conn = get_conn()
    cursor = conn.cursor()
    print("this is sql:  ", sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    con_mysql()
