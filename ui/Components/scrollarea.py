from PySide6.QtWidgets import QSlider , QScrollArea, QMainWindow ,QWidget,QHBoxLayout


class ScrollArea(QWidget):
    def __init__(self , widget:QWidget):
        super().__init__()
    
        slider= QScrollArea()
       
        slider.setStyleSheet("""
        background-color: blue;
        border-radius: 20px;
    """)
       
        
      

