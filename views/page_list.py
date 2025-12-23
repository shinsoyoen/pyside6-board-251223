# 게시글 리스트 출력
# self-btu-layout
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton,QTableWidget, QTableWidgetItem
from PySide6.QtCore import Signal

class ListPage(QWidget):
    request_create = Signal()
    request_detail = Signal(int)

    def __init__(self):
        super().__init__()

        self.table = QTableWidget()
        self.table.setColumnCount(5) #컬럼 수
        self.table.setHorizontalHeaderLabels(
            ["ID", "제목", "작성자", "작성일", "수정일"]
        )
        
        btn_create = QPushButton("글 작성")

        layout = QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addWidget(btn_create)

        btn_create.clicked.connect(self.request_create.emit)
        self.table.cellDoubleClicked.connect(self.on_row_clicked)

    def load_posts(self, posts):
        self.table.setRowCount(len(posts))
        for row, post in enumerate(posts):
            self.table.setItem(row, 0, QTableWidgetItem(str(post["id"])))
            self.table.setItem(row, 1, QTableWidgetItem(post["title"]))
            self.table.setItem(row, 2, QTableWidgetItem(post["author"]))
            self.table.setItem(row, 3, QTableWidgetItem(post["created_at"]))
            self.table.setItem(row, 4, QTableWidgetItem(post["updated_at"]))

    def on_row_clicked(self, row, column):
        post_id = int(self.table.item(row, 0).text())
        self.request_detail.emit(post_id)

