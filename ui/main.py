from Components.mainboard import Mainboard
from PySide6.QtWidgets import QWidget, QSplashScreen, QApplication, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys, time

from Components.scrollarea import ScrollArea
from Components.menubar import MenuBar

def main():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    screensize = screen.availableGeometry()
    width, height = screensize.width(), screensize.height()

   
    pix = QPixmap("C:\\Users\\Tab's\\Downloads\\Gina_3.png")
    splash = QSplashScreen(pix)
    splash.show()
    time.sleep(5)
    splash.close()

  
    widget = QWidget()
    scroll = ScrollArea(widget)

   
    window = Mainboard(scroll)
    window.resize(width, height)
    

    # Container with vertical layout
    container = QWidget()
    container.setStyleSheet("background-color: #f0f0f0;")
    vbox = QVBoxLayout(container)
    vbox.setContentsMargins(0,0,0,0)
    vbox.setSpacing(0)

    # Top menu bar
    menubar = MenuBar()
    menuhbox=QHBoxLayout()
    menuhbox.setContentsMargins(0,0,0,0)
    menuhbox.setSpacing(0)
    menuhbox.addWidget(menubar)
    vbox.addLayout(menuhbox)

    content_area = QWidget()
    content_area.setStyleSheet("background-color: white;")
    content_area.setFixedWidth(int((width * 0.9)+70))
    content_area.setFixedHeight(int((height * 0.8)))

   

    # Put scroll inside content_area if needed
    content_layout = QVBoxLayout(content_area)
    content_layout.setContentsMargins(0,0,0,0)
    content_layout.addWidget(scroll)

     #htis Hbox is to center the content Widget
    hbox = QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(content_area)
    hbox.addStretch()
    vbox.addLayout(hbox)
    

               

   


    # Set container as central widget
    window.setCentralWidget(container)

    window.show()
    app.exec()

if __name__ == "__main__":
    main()