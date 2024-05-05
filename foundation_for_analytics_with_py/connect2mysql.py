import mysql.connector
import pymysql


def mysql_connection():
    # 创建连接对象
    cnx = mysql.connector.connect(user='root', password='123456', host='localhost')

    # 创建游标
    cursor = cnx.cursor()

    # 选择要查看的数据库
    cursor.execute("USE houzi_data_analysis")

    # 查询所有表名
    cursor.execute("SHOW TABLES")

    # 打印所有表名
    for table_name in cursor:
        print(table_name[0])

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def pymysql_connection():
    # 连接数据库
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='houzi_data_analysis')

    # 创建游标对象
    cursor = conn.cursor()

    # 编写SQL查询语句
    # sql = "SELECT * FROM fangyuanpingfentongji"

    sql = "SELECT 城市, avg(分数) as average_score FROM fangyuanpingfentongji group by 城市 order by average_score"

    # 执行SQL查询
    cursor.execute(sql)

    # 获取查询结果
    results = cursor.fetchall()

    # 遍历结果并打印
    for row in results:
        print(row)

    # 关闭游标和数据库连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    pymysql_connection()
