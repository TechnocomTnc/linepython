def conn():
    dbconn=MySQLdb.connect(database='db_junebot', user='root', password='', host='localhost',charset='utf8')
    query = "select * from question"
    with dbconn.cursor(MySQLdb.cursors.DictCursor) as cursor:
    cursor.execute(query)
    data = cursor.fetchall()
    x = json.dumps(data,indent=4)
    return x
