import pymysql


# 获取数据库连接
def get_connection():
    host = '119.23.253.128'
    port = 3306
    user = 'root'
    password = '123456'
    database = 'jd_text'
    db = pymysql.connect(host, user, password, database, charset='utf8', port=port)
    return db


# 获取数据库游标
def get_cursor(db):
    cursor = db.cursor()
    return cursor


# 关闭连接
def close_connection(db):
    db.close()


# 插入数据
def insert_record(db, cursor, item):
    sql = 'insert into jd_goods(title, img_url, price, detail) values ("%s", "%s", "%s", "%s")'
    cursor.execute(sql, (item['title'], item['img_url'], item['price'], item['detail']))
    db.commit()
