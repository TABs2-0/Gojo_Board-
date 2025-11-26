from PySide6.QtWidgets import QHBoxLayout, QWidget,QVBoxLayout,QSizePolicy,QToolButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from Components.menubuttons import MenuButtons
class MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
     

        layout = QHBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 5, 10, 5)
        
        file = MenuButtons("C:/Users/Public/Python Projects/Gojolab/Assets/loin.jpg", "File")
        home = MenuButtons("C:/Users/Public/Python Projects/Gojolab/Assets/loin.jpg", "Home")
        draw = MenuButtons("C:/Users/Public/Python Projects/Gojolab/Assets/loin.jpg", "Draw")
        insert = MenuButtons("C:/Users/Public/Python Projects/Gojolab/Assets/loin.jpg", "Insert")

        layout.addWidget(file)
        layout.addWidget(home)
        layout.addWidget(draw)
        layout.addWidget(insert)
        #file.clicked.connect(self.on_file_clicked())

    def on_file_clicked():
        options_widget= QWidget()
        options_widget.setStyleSheet("background-color:white;")
        options_widget.setContentsMargins(5,5,5,5)
        #layout to store the diffent toolButtons
        layout=QVBoxLayout()
        layout.addWidget(options_widget)

        new_option=QToolButton()
        open_option=QToolButton()
        save_option=QToolButton()
        save_as_option=QToolButton() 
        print_option=QToolButton()
        export_to_pdf_option=QToolButton()
        export_to_pdf_png=QToolButton()


