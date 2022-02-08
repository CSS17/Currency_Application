from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys
from doviz import *




def window():
    global yazı
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setWindowTitle("Döviz Programı")
    win.setFixedSize(600, 400)
    yazı=QLabel(win)
    yazı.setFont(QFont('Arial', 24))
    buton=QPushButton("Dolar $",win)
    buton.setGeometry(50, 50, 100, 50)
    buton.setStyleSheet("background-color : lightgreen")
    buton.clicked.connect(dolar_goster)
    buton2=QPushButton("Euro €",win)
    buton2.setGeometry(150, 50, 100, 50)
    buton2.setStyleSheet("background-color : orange")
    buton2.clicked.connect(euro_goster)
    buton3=QPushButton("Sterlin £",win)
    buton3.setGeometry(250, 50, 100, 50)
    buton3.setStyleSheet("background-color : pink")
    buton3.clicked.connect(sterlin_goster)
    buton4=QPushButton("G.Altın",win)
    buton4.setGeometry(350, 50, 100, 50)
    buton4.setStyleSheet("background-color : yellow")
    buton4.clicked.connect(altın_goster)
    buton5=QPushButton("BTC ₿",win)
    buton5.setGeometry(450, 50, 100, 50)
    buton5.setStyleSheet("background-color : lightblue")
    buton5.clicked.connect(btc_goster)
    win.show()
    sys.exit(app.exec())

def dolar_goster():
    yazı.setGeometry(170,200, 310, 250)
    yazı.setText("1 $ ="+dolar()+" ₺")

def euro_goster():
    yazı.setGeometry(170,200, 310, 250)
    yazı.setText("1 € ="+euro()+" ₺" )

def sterlin_goster():
    yazı.setGeometry(170,200, 310, 250)
    yazı.setText("1 £ ="+sterlin()+" ₺" )
    
def altın_goster():
    yazı.setGeometry(160,200, 310, 250)
    yazı.setText("1 GAU ="+altın()+" ₺" )

def btc_goster():
    yazı.setText("1 ₿ ="+btc()+" $" )
    yazı.setGeometry(150,200, 310, 250)
    

window()
