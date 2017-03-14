import MySQLdb

class sql(object):
    def __init__(self, username, password, db):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user=username,         # your username
                     passwd=password,  # your password
                     db=db)

    def pull(self, sql):
        cur = self.db.curson()
        cur.excute(sql)

    def generat_chart():
        pass

if __name__ == "__main__":
    qianzhan= sql("qian"，"zhan")
    qianzhan.pull()
#
#    aiqianjin= sql("aiqian","jin")
#    aiqianjin.pull()
#
#    qianqian= sql("qian", "qian")
#    qianqian.pull()
#
