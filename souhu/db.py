import pymysql
from pymysql.cursors import DictCursor

def main():
    # 1. 创建数据库连接对象
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='li3325228')
    try:
        # 2. 通过连接对象获取游标
        with con.cursor(cursor=DictCursor) as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            cursor.execute(
                'delete from tb_dept where dno=1133'
            )
            cursor.execute(
                'select dno as no, dname as name, dloc as loc from tb_dept'
            )
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'])

    finally:
        con.close()


if __name__ == '__main__':
    main()
