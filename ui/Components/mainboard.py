from PySide6.QtWidgets import QWidget, QPushButton,QMainWindow,QSplashScreen



class Mainboard(QMainWindow):
    def __init__(self,widget:QWidget):
        super().__init__()
       
        self.setWindowTitle("GojoBoard") 
        self.setStyleSheet("""
            background-color:grey;
            color: white;
        """)

        
       

       
        
    