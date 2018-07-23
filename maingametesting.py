import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget, QApplication,QHBoxLayout,QVBoxLayout


class MainGame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.redraw_mainmenu()
        self.button1.clicked.connect(self.btn_click)
        self.showFullScreen()

    def findcenter(self, screensize):
        centerPoint = [screensize[0]/2, screensize[1]/2]
        return(centerPoint)

    def findscreensize(self):
        screen = app.primaryScreen()
        size = screen.size()
        screensize = [size.width(), size.height()]
        print(screensize)
        return screensize

    def btn_click(self):
        self.Label1.setText('testing changing text')

    def redraw_mainmenu(self):
        """---Finding Screen Variables---"""
        self.screensize = self.findscreensize()
        self.centerPoint = self.findcenter(self.screensize)
        """---Labels---"""
        self.Label1 = QtWidgets.QLabel(self)
        self.Label1.setText('Hello there')
        self.label2 = QtWidgets.QLabel(self)
        #label2.setPixmap(QtGui.QPixmap('test.png')) Picture
        """---Buttons---"""
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Play')
        my_h_grid = QHBoxLayout()
        my_v_grid = QVBoxLayout()
        my_v_grid.addWidget(self.Label1)
        my_v_grid.addStretch()
        my_v_grid.addWidget(self.button1)
        my_v_grid.addStretch()
        my_h_grid.addStretch()
        my_h_grid.addLayout(my_v_grid)
        my_h_grid.addStretch()
        self.setLayout(my_h_grid)
        """---Set Window Title---"""
        self.setWindowTitle('Main Game Test')
        self.button1.resize(float(self.screensize[0])*0.20833333333333333333333333333333, float(self.screensize[1])*0.09259259259259259259259259259259)
        #self.setGeometry(100,100,300,200)
        #self.move(int(centerPoint[0])-150,int(centerPoint[1])-100)\

        #self.button1.setGeometry(int(self.centerPoint[0])-200, int(self.centerPoint[1])-50, 400, 100)

        #Change Background Colour
        self.setObjectName('MainWidget')
        self.setStyleSheet("""
            #MainWidget {
                background-color: #87ceeb;
            }
        """)
        #PyQt Auto layout System
        """
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.Label1)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.button1)
        v_box.addLayout(h_box)
        v_box.addStretch()
        

        self.setLayout(v_box)
        """


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    game = MainGame()
    sys.exit(app.exec_())
