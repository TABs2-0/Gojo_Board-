import sys
from PySide6.QtWidgets import QApplication, QLabel

def main():
    # Step 1: Create the application
    app = QApplication(sys.argv)

    # Step 2: Create a widget (here just a label)
    label = QLabel("Hello, PySide!")
    label.resize(1900, 1000)
    label.show()

    # Step 3: Run the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()