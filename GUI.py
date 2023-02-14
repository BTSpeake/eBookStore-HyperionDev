from PyQt6.QtWidgets import *

class StoreMainWin(QMainWindow):
    def __init__(self, store):
        super(StoreMainWin, self).__init__()

        self.store = store

        mainW = QWidget()
        mainW.setLayout(QVBoxLayout())
        
        self.table = QTextEdit()
        self.table.setMarkdown(self.store.listAllItems())
        print(self.store.listAllItems())
        self.table.setMinimumWidth(400)
        mainW.layout().addWidget(self.table)

        self.setCentralWidget(mainW)
        self.setWindowTitle("eBook Store")
        self.show()

        return


def runGUI(store):
    app = QApplication([])
    win = StoreMainWin(store)
    app.exec()
    return