from PySide6.QtWidgets import QToolButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


class MenuButtons(QToolButton):
    def __init__(self,icon_path,text:str):
        super().__init__()

        self.setText(text) 
        self.setIcon(QIcon(icon_path)) 
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setAutoRaise(True) #to bring out the same buton effect
         
         

        self.setStyleSheet("""  QToolButton {
            padding: 2px 8px;
            background-color: transparent;
            color: #2D323E;
            border: none;
            font-size: 14px;
        }

        QToolButton:hover {
            background-color: #F2F4F7;
            border-radius: 6px;
        }""")     
            