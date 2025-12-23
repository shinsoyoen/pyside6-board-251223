# 페이지 관리
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from views.page_list import ListPage
from views.page_create import CreatePage
from views.page_detail import DetailPage
from views.page_edit import EditPage

class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("게시판 프로그램")
        self.current_post_id = None
    
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        #페이지 생성
        self.page_list = ListPage()
        self.page_create = CreatePage()
        self.page_detail = DetailPage()
        self.page_edit = EditPage()

        #views 종류 등록
        self.stack.addWidget(self.page_list)
        self.stack.addWidget(self.page_create)
        self.stack.addWidget(self.page_detail)
        self.stack.addWidget(self.page_edit)
        
        self.load_list_page()
        
        # Sigmal-Solt 연결
        self.page_list.request_create.connect(self.move_create_page) #목록->생성
        self.page_list.request_detail.connect(self.move_detail_page) #목록->조회
        
        self.page_create.request_cancel.connect(self.move_list_page) #생성->취소->목록
        self.page_create.request_save.connect(self.save_post) # 생성->저장
        
        self.page_detail.request_list.connect(self.move_list_page) #조회->목록
        self.page_detail.request_edit.connect(self.move_edit_page) #조회->수정
        self.page_detail.request_delete.connect(self.ask_delete) #조회->삭제

        self.page_edit.request_save.connect(self.update_post)
        self.page_edit.request_cancel.connect(self.move_detail_page)

        # 처음으로
        self.stack.setCurrentWidget(self.page_list)

    def move_create_page(self):
        self.page_create.form_clear()
        self.stack.setCurrentWidget(self.page_create)
    #
    def load_list_page(self):
        posts = self.db.get_posts()
        self.page_list.load_posts(posts)
        self.stack.setCurrentWidget(self.page_list)
    #
    def move_list_page(self):
        self.load_list_page()

    def move_detail_page(self,post_id):
        self.current_post_id = post_id
        post = self.db.get_post(post_id)
        self.page_detail.set_post(post)
        self.stack.setCurrentWidget(self.page_detail)

    def move_edit_page(self):
        post = self.db.get_post(self.current_post_id)
        self.page_edit.set_post(post)
        self.stack.setCurrentWidget(self.page_edit)
        
    def ask_delete(self):
        if self.current_post_id is None:
            return

        ask = QMessageBox.question(
            self,
            "삭제 확인",
            "정말 삭제하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No
        )

        if ask == QMessageBox.Yes:
            self.db.delete_post(self.current_post_id)
            self.current_post_id = None
            self.move_list_page()
    
    def update_post(self, post: dict):
        self.db.update_post(
            post_id=post["id"],
            title=post["title"],
            content=post["content"]
        )
        self.move_detail_page(post["id"])

    def save_post(self, post: dict):
        if not post["title"] or not post["content"]:
            return
        self.db.insert_post(post)
        self.move_list_page()