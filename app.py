import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileSystemModel
from ui import Ui_FileExplorerMainWindow


class FileExplorerMainWindow(QMainWindow, Ui_FileExplorerMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(''))
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #e2ebf0, stop:1 #cfd9df);
            }
            QTreeView {
                font-size: 16px;
            }
        """)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorerMainWindow()
    window.show()
    sys.exit(app.exec_())
