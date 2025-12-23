from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QLineEdit,QTextEdit, QPushButton, QHBoxLayout, QMessageBox)
from PySide6.QtCore import Signal

class EditPage(QWidget):
    request_cancel = Signal()
    request_save = Signal(dict)

    def __init__(self):
        super().__init__()

        self.current_post_id = None

        self.title_input = QLineEdit()
        self.content_input = QTextEdit()
        self.author_label = QLabel()

        btn_save = QPushButton("수정 저장")
        btn_cancel = QPushButton("취소")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_cancel)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("게시글 수정"))
        layout.addWidget(QLabel("제목"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("내용"))
        layout.addWidget(self.content_input)
        layout.addWidget(QLabel("작성자"))
        layout.addWidget(self.author_label)
        layout.addLayout(btn_layout)

        btn_save.clicked.connect(self.on_save)
        btn_cancel.clicked.connect(self.request_cancel.emit)

    # 게시글 작성
    def set_post(self, post: dict):
        self.current_post_id = post["id"]
        self.title_input.setText(post["title"])
        self.content_input.setText(post["content"])
        self.author_label.setText(post["author"])

    # 게시글 저장
    def on_save(self):
        title = self.title_input.text().strip()
        content = self.content_input.toPlainText().strip()

        if not title or not content:
            QMessageBox.warning(self,"제목과 내용은 필수입니다")
            return

        self.request_save.emit({
            "id": self.current_post_id,
            "title": title,
            "content": content
        })