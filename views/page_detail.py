# 게시글 삭제

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Signal

class DetailPage(QWidget):
    request_list = Signal()
    request_edit = Signal()
    request_delete = Signal()
    
    def __init__(self):
        super().__init__()

        self.lbl_title = QLabel()
        self.lbl_author = QLabel()
        self.lbl_content = QLabel()
        self.lbl_created_at = QLabel()
        self.lbl_updated_at = QLabel()
        
        btn_list = QPushButton("글 목록")
        btn_edit = QPushButton("글 수정")
        btn_delete = QPushButton("글 삭제")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_list)
        btn_layout.addWidget(btn_edit)
        btn_layout.addWidget(btn_delete)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("게시글 상세내용"))

        layout.addWidget(self.lbl_title)
        layout.addWidget(self.lbl_author)
        layout.addWidget(self.lbl_content)
        layout.addWidget(self.lbl_created_at)
        layout.addWidget(self.lbl_updated_at)

        layout.addLayout(btn_layout)
        
        btn_list.clicked.connect(self.request_list.emit)
        btn_edit.clicked.connect(self.request_edit.emit)
        btn_delete.clicked.connect(self.request_delete.emit)
        
    # 게시글 상세, 저장된 내용 보여주기
    def set_post(self, post: dict):
        if post is None:
            return
        self.lbl_title.setText(f"제목: {post['title']}")
        self.lbl_author.setText(f"작성자: {post['author']}")
        self.lbl_content.setText(post["content"])
        self.lbl_created_at.setText(f"작성일: {post['created_at']}")
        self.lbl_updated_at.setText(f"수정 작성일: {post['updated_at']}")