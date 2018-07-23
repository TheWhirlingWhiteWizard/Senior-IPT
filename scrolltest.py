import csv
import os
import sys

from PyQt5 import QtCore, QtGui, QtMultimedia, QtWidgets,Qt
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QGridLayout,
                             QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                             QScrollBar, QSizePolicy, QVBoxLayout, QWidget)

path = (os.path.dirname(os.path.abspath(__file__)))
os.chdir(path)

class MainGame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.fieldnames = ['name', 'scores']
        """---Finding Screen Variables---"""
        self.screensize = self.findscreensize()
        self.centerPoint = self.findcenter(self.screensize)

        self.draw_mainmenu()
        self.play_button.clicked.connect(self.btn_click)
        self.exit_button.clicked.connect(self.exit_game)
        self.login_menu()
        self.scrollArea.hide()
        self.login_menu_widget.hide()
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
        #self.mainmenu.hide()
        #self.login_menu()
        self.mainmenu.hide()
        self.scrollArea.show()
        self.login_menu_widget.show()
    def btn_choose_acc(self):
        print('profile chosen')

    def exit_game(self):
        sys.exit()

    def draw_mainmenu(self):
        """---Labels---"""
        self.title = QtWidgets.QLabel('hello', self)
        self.title.setText('Fun Math Game')
        

        




        #label2.setPixmap(QtGui.QPixmap('test.png')) Picture
        """---Buttons---""" 
        self.play_button = QtWidgets.QPushButton(self)
        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setText('Exit ')
        self.exit_button.setGeometry(0, 0, float(
            self.screensize[0]*0.05208333333333333333333333333333), float(self.screensize[1])*0.0462962962962962962962962962963)
        
        
        
        
        
        
        
        



        """---Layout Stuff---"""
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.title)
        self.v_layout.addStretch()
        self.v_layout.addWidget(self.play_button)
        self.v_layout.addStretch()
        self.h_layout.addStretch()
        self.h_layout.addLayout(self.v_layout)
        self.h_layout.addStretch()
        self.play_button.setText('Play')
        font = self.play_button.font()
        font.setPixelSize(
            float(self.screensize[1])*0.09259259259259259259259259259259 * 0.5)
        self.play_button.setFont(font)
        self.play_button.setGeometry(int(self.centerPoint[0])-(float(self.screensize[0])*0.10416666666666666666666666666667), int(
            self.centerPoint[1])-(float(self.screensize[1])*0.0462962962962962962962962962963), float(self.screensize[0])*0.20833333333333333333333333333333, float(self.screensize[1])*0.09259259259259259259259259259259)
        """---Set Window Title---"""
        self.setWindowTitle('Main Game Test')
        font = self.title.font()
        font.setPixelSize(
            float(self.screensize[1])*0.09259259259259259259259259259259 * 0.8)
        self.title.setFont(font)
        self.setLayout(self.h_layout)
        self.play_button.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred)

        #self.setGeometry(100,100,300,200)
        #self.move(int(centerPoint[0])-150,int(centerPoint[1])-100)\

        #self.play_button.setGeometry(int(self.centerPoint[0])-200, int(self.centerPoint[1])-50, 400, 100)
        self.mainmenu = QtWidgets.QWidget(self)
        self.mainmenu.setLayout(self.h_layout)
        self.qr = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center()
        self.qr.moveCenter(self.cp)
        self.mainmenu.move(self.qr.topLeft())
        """selferPoint[0])-(float(self.screensize[0])*0.10416666666666666666666666666667), int(
            se.mainmenu.move(int(self.centlf.centerPoint[1])-(float(self.screensize[1])*0.0462962962962962962962962962963),)"""

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
        h_box.addWidget(self.title)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.play_button)
        v_box.addLayout(h_box)
        v_box.addStretch()
        

        self.setLayout(v_box)
        """
    def create_new_profile(self):
        self.write_new = True
        with open(path+'/'+'names.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.fieldnames)
            next(reader)
            print('hello')
            for row in reader:
                #print(row['name'] + self.enter_new_name)
                print('tests')
                if self.enter_new_name.text() == row['name']:      
                    self.write_new = False
        if self.write_new == True and len(self.enter_new_name.text()) > 0:
            with open(path+'/'+'names.csv', 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writerow({'name': self.enter_new_name.text(), 'scores': []})
                """
                writer.writerow({'first_name': 'Baked', 'last_name': 'Beans', 'scores': ['1', '2']})
                writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam', 'scores': ['1', '2']})
                writer.writerow({'first_name': 'Wonderful','last_name': 'Spam', 'scores': ['1', '2']})
                print('goodbye')
                    """
                print(self.enter_new_name.text())

    def login_menu(self):
        self.login_menu_widget = QtWidgets.QWidget(self)
        """---Scroll Wheel Area---"""
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(int(self.centerPoint[0])-(float(self.screensize[0])*0.10416666666666666666666666666667), int(
            self.centerPoint[1])-(float(self.screensize[1])*0.0462962962962962962962962962963), 300, 300))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setEnabled(True)
        self.v_box1 = QVBoxLayout()
        self.scrollArea.setContentsMargins(0,0,0,0)
        self.scrollArea.setObjectName('myscrollarea')
        self.scrollArea.setStyleSheet(
            '#myscrollarea {background-color: #1e195e; color: red;}')
        self.v_box1.setAlignment(QtCore.Qt.AlignTop)

        """---Create Storage Widget---"""
        self.goodwidget = QtWidgets.QWidget()
        """---Store Layout Inside Storage Variable---"""
        self.goodwidget.setLayout(self.v_box1)
        """---CSV Stuff---"""
        try:
            with open(path+'\\'+'names.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=self.fieldnames)
                next(reader)
                self.button_list = []
                for row in reader:
                    print(row['name'])
                    name_button = QtWidgets.QPushButton()
                    name_button.setText(row['name'])
                    name_button.clicked.connect(self.btn_choose_acc)
                    self.button_list.append(name_button)
                    
                for button in self.button_list:
                    self.v_box1.addWidget(button)
        except:
            with open(path+'\\'+'names.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writeheader()
                """
                writer.writerow(
                    {'first_name': 'Baked', 'last_name': 'Beans', 'scores': ['1', '2']})
                writer.writerow(
                    {'first_name': 'Lovely', 'last_name': 'Spam', 'scores': ['1', '2']})
                writer.writerow({'first_name': 'Wonderful',
                                 'last_name': 'Spam', 'scores': ['1', '2']})
                print('goodbye')
                """
                print('write')
        """---Store Buttons In V_Box---"""
        self.scrollArea.setWidget(self.goodwidget)
        self.login_text = QtWidgets.QLabel()
        self.login_text.setText('Profiles')
        font = self.login_text.font()
        font.setPixelSize(float(self.screensize[1])*0.09259259259259259259259259259259 * 0.5)
        self.login_text.setFont(font)
        
        self.login_menu_v_box = QVBoxLayout(self)
        self.login_menu_v_box.addWidget(self.login_text)
        self.enter_new_name = QtWidgets.QLineEdit(self)
        self.create_new_profile_button = QtWidgets.QPushButton(self)
        self.create_new_profile_button.setText('Create New Profile')
        self.login_menu_v_box.addWidget(self.scrollArea)
        self.login_menu_v_box.addWidget(self.enter_new_name)
        self.login_menu_v_box.addWidget(self.create_new_profile_button)
        self.enter_new_name.setPlaceholderText('Enter New Name')
        self.login_menu_widget.setLayout(self.login_menu_v_box)
        self.login_menu_widget.setGeometry(QtCore.QRect(int(self.centerPoint[0])-(float(self.screensize[0])*0.21666666666666666666666666666667), int(
            self.centerPoint[1])-(float(self.screensize[1])*0.39074074074074074074074074074074), 800, 800))
        self.create_new_profile_button.clicked.connect(self.create_new_profile)






        

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    game = MainGame()
    sys.exit(app.exec_())
    import csv
