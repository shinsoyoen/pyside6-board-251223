#DB 세팅

import sqlite3

class DBManager:
    def __init__(self, db_path="board.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.create_table()

    # 테이블 생성
    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
        );
        """
        self.conn.execute(sql)
        self.conn.commit()

    # 게시글 조회
    def get_posts(self):
        sql = """
        SELECT id, title, author, created_at, updated_at
        FROM posts
        ORDER BY id DESC
        """
        cursor = self.conn.execute(sql)
        return cursor.fetchall()

    def get_post(self, post_id: int):
        sql = """
        SELECT id, title, content, author, created_at, updated_at
        FROM posts
        WHERE id = ?
        """
        cursor = self.conn.execute(sql, (post_id,))
        return cursor.fetchone()

    # 게시글 수정
    def update_post(self, post_id: int, title: str, content: str) -> None:
        try:
            sql = """
            UPDATE posts
            SET title = ?, content = ?, updated_at = datetime('now', 'localtime')
            WHERE id = ?
            """
            cursor = self.conn.execute(sql, (title, content, post_id))
            self.conn.commit()

            if cursor.rowcount == 0:
                raise ValueError("해당 post_id가 존재하지 않습니다.")

        except Exception as e:
            self.conn.rollback()
            raise e

    # 게시글 추가
    def insert_post(self, post: dict) -> int:
        try:
            sql = """
            INSERT INTO posts (title, content, author)
            VALUES (?, ?, ?)
            """
            cursor = self.conn.execute(
                sql,
                (
                    post.get("title"),
                    post.get("content"),
                    post.get("author"),
                )
            )
            self.conn.commit()
            return cursor.lastrowid

        except Exception as e:
            self.conn.rollback()
            raise e

    # 게시글 삭제
    def delete_post(self, post_id: int) -> None:
        try:
            sql = "DELETE FROM posts WHERE id = ?"
            cursor = self.conn.execute(sql, (post_id,))
            self.conn.commit()

            if cursor.rowcount == 0:
                raise ValueError("해당 post_id가 존재하지 않습니다.")

        except Exception as e:
            self.conn.rollback()
            raise e
