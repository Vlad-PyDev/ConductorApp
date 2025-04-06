from PyQt5 import QtCore, QtWidgets


class Ui_FileExplorerMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("FileExplorerMainWindow")
        MainWindow.resize(1300, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Дерево файловой системы
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 20, 1280, 952))
        self.treeView.setObjectName("treeView")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtWidgets.QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проводник"))
