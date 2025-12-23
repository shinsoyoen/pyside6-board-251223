# main 시작

import sys
from PySide6.QtWidgets import QApplication
from db.db_manager import DBManager
from views.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    db = DBManager()
    window = MainWindow(db)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()