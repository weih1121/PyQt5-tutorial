from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./peopleinfo.db')

    if not db.open():
        QMessageBox.critical(None, ("无法打开数据库"), ("无法建立到数据库的连接，这个例子需要SQLite支持, 请检查数据库配置\n\n 单击取消按钮退出应用"),
                             QMessageBox.Cancel )
        return False

    query = QSqlQuery()
    query.exec_("create table people(id int PRIMARY KEY, name VARCHAR(20), address VARCHAR(30))")

    query.exec_("insert into people values(1, 'zhangsan1', 'beijing')")
    query.exec_("insert into people values(2, 'lisi', 'tianjin')")
    query.exec_("insert into people values(3, 'wangwu', 'hainan')")
    query.exec_("insert into people values(4, 'wangermazi', 'sichuan')")
    query.exec_("insert into people values(5, 'xiaotaoqi', 'guangzhou')")

    db.close()
    return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    createDB()
    sys.exit(app.exec_())
