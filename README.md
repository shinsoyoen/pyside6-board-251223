지원자 : 신소연

## 실행 방법
### 1. 가상환경 생성
conda create -n pyside6 -c conda-forge pyside6 qt-main

### 2. 가상환경 활성화
conda activate pyside6

### 3. pip 설치
python -m pip install --upgrade pip

### 4. 실행
python main.py


## 파일명
main_window : 페이지간 이동 연결

page_create : 게시글 생성 (C)

page_detail : 게시글 조회 (R)

page_edit : 게시글 수정 (U)

page_list : 전체 게시글 목록 (main)

DB : SQLite


## 개발 기록
2025.12.18 : conda 가상환경 생성, 파일 구조 생성, DB 생성 및 연결 확인, 페이지 간 Signal 버튼 연결(list에서 Create 간 이동)

2025.12.19 : 조회 페이지 버튼 생성(목록/수정/삭제), 게시글 작성 및 저장 버튼, 작성된 게시글 목록에서 보여지는 지 확인

2025.12.20 : updated_at(1.게시글 생성시, 생성일=수정일 2.게시글 수정시, 수정일만 변경), 삭제&수정 기능 추가
