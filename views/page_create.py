from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QHBoxLayout, QMessageBox)
from PySide6.QtCore import Signal

class CreatePage(QWidget):
    request_cancel = Signal()
    request_save = Signal(dict)

    def __init__(self):
        super().__init__()

        self.title_input = QLineEdit()
        self.content_input = QTextEdit()
        self.author_input = QLineEdit()

        btn_save = QPushButton("저장")
        btn_cancel = QPushButton("취소")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_cancel)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("게시글 작성"))

        layout.addWidget(QLabel("제목"))
        layout.addWidget(self.title_input)

        layout.addWidget(QLabel("내용"))
        layout.addWidget(self.content_input)

        layout.addWidget(QLabel("작성자"))
        layout.addWidget(self.author_input)

        layout.addLayout(btn_layout)

        btn_save.clicked.connect(self.on_save)
        btn_cancel.clicked.connect(self.request_cancel.emit)

    def on_save(self):
        post = {
            "title": self.title_input.text().strip(),
            "content": self.content_input.toPlainText().strip(),
            "author": self.author_input.text().strip(),
        }
        # 유효성 검사
        if not post["title"] or not post["content"]:
            QMessageBox.warning(self, "경고", "제목과 내용은 필수입니다")
            return

        self.request_save.emit(post)
        self.form_clear()
    
    # 이전에 작성된 내용 지우기
    def form_clear(self):
        self.title_input.clear()
        self.content_input.clear()
        self.author_input.clear()
