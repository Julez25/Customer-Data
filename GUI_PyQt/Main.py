import sys
from PyQt6.QtWidgets import QApplication, QWidget

def main():
    app = QApplication(sys.argv)
    test_Win = QWidget()
    test_Win.setWindowTitle("Test Fenster")
    test_Win.resize(400, 300)
    test_Win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()