"""
QR Code Manager GUI (Python 3.13)

기능
- QR 코드 생성 (png)
- QR 관련 정보 입력 : QR코드 이름, QR 코드 값, 파일경로
- MySQL 데이터베이스로 QR코드 정보 관리 (계정: python / 비밀번호: 123456 / DB: python)
- QR 코드 관리 : 이름 변경, 정보 및 이미지 삭제
- 대시보드 : 등록된 QR 코드 리스트 확인, 수정/삭제
- DB 접속 시 qr_code 테이블 자동 생성

필요 패키지 설치 (명령행에서):
pip install qrcode[pil] pillow mysql-connector-python

저장 규칙
- 파일 확장자: .png
- 파일명: 연월일_시분초_코드이름.png  (예: 20251011_153045_알클사이트.png)

"""

import os
import uuid
import re
import qrcode
from PIL import Image
import mysql.connector
from datetime import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# -------------------------------
# DB 설정 (사용자 요구사항)
# -------------------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'python',
    'password': '123456',
    'database': 'python',
    'auth_plugin': 'mysql_native_password'
}

TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS qr_code (
    no INT AUTO_INCREMENT PRIMARY KEY,
    id VARCHAR(36) NOT NULL,
    name VARCHAR(255) NOT NULL,
    value TEXT NOT NULL,
    path TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

# -------------------------------
# 유틸리티 함수
# -------------------------------

def sanitize_filename(name: str) -> str:
    # 파일 이름에 사용 불가 문자를 제거
    name = name.strip()
    return re.sub(r"[^0-9A-Za-z가-힣 _\-()\[\]]+", "", name)


def make_image_filename(name: str, when: datetime) -> str:
    safe = sanitize_filename(name)
    return f"{when.strftime('%Y%m%d_%H%M%S')}_{safe}.png"


# -------------------------------
# DB 연결 및 기본 작업
# -------------------------------

def connect_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn


def ensure_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(TABLE_SCHEMA)
    conn.commit()
    cur.close()
    conn.close()


# -------------------------------
# QR 코드 생성 및 파일 저장
# -------------------------------

def generate_qr_image(value: str, save_path: str):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(value)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # PIL Image
    img = img.convert('RGB')
    img.save(save_path, format='PNG')


# -------------------------------
# DB CRUD
# -------------------------------

def insert_qr_record(uuid_str, name, value, path):
    now = datetime.now()
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO qr_code (id, name, value, path, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)",
        (uuid_str, name, value, path, now, now)
    )
    conn.commit()
    cur.close()
    conn.close()


def update_qr_record(id_str, new_name=None, new_path=None):
    now = datetime.now()
    conn = connect_db()
    cur = conn.cursor()
    sets = []
    vals = []
    if new_name is not None:
        sets.append('name = %s')
        vals.append(new_name)
    if new_path is not None:
        sets.append('path = %s')
        vals.append(new_path)
    sets.append('updated_at = %s')
    vals.append(now)
    vals.append(id_str)
    sql = f"UPDATE qr_code SET {', '.join(sets)} WHERE id = %s"
    cur.execute(sql, tuple(vals))
    conn.commit()
    cur.close()
    conn.close()


def delete_qr_record(id_str):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM qr_code WHERE id = %s", (id_str,))
    conn.commit()
    cur.close()
    conn.close()


def fetch_all_qr_records():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT no, id, name, value, path, created_at, updated_at FROM qr_code ORDER BY no DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def fetch_record_by_id(id_str):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT no, id, name, value, path, created_at, updated_at FROM qr_code WHERE id = %s", (id_str,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


# -------------------------------
# GUI 정의
# -------------------------------

class QRManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('QR Code Manager')
        self.geometry('980x640')

        # 상단: 입력 영역
        self.frame_input = ttk.LabelFrame(self, text='QR 코드 생성')
        self.frame_input.pack(fill='x', padx=10, pady=8)

        lbl_name = ttk.Label(self.frame_input, text='QR 코드 이름')
        lbl_name.grid(row=0, column=0, padx=6, pady=6, sticky='w')
        self.entry_name = ttk.Entry(self.frame_input, width=40)
        self.entry_name.grid(row=0, column=1, padx=6, pady=6, sticky='w')

        lbl_value = ttk.Label(self.frame_input, text='QR 값 (URL/Text)')
        lbl_value.grid(row=1, column=0, padx=6, pady=6, sticky='w')
        self.entry_value = ttk.Entry(self.frame_input, width=60)
        self.entry_value.grid(row=1, column=1, padx=6, pady=6, sticky='w')

        lbl_path = ttk.Label(self.frame_input, text='저장 폴더')
        lbl_path.grid(row=2, column=0, padx=6, pady=6, sticky='w')
        self.entry_path = ttk.Entry(self.frame_input, width=60)
        self.entry_path.grid(row=2, column=1, padx=6, pady=6, sticky='w')
        btn_browse = ttk.Button(self.frame_input, text='찾아보기', command=self.browse_folder)
        btn_browse.grid(row=2, column=2, padx=6, pady=6)

        btn_generate = ttk.Button(self.frame_input, text='생성 및 저장', command=self.on_generate)
        btn_generate.grid(row=0, column=3, rowspan=3, padx=8, pady=6)

        # 중간: 대시보드
        self.frame_dash = ttk.LabelFrame(self, text='QR 코드 관리 대시보드')
        self.frame_dash.pack(fill='both', expand=True, padx=10, pady=8)

        columns = ('no', 'id', 'name', 'value', 'path', 'created_at', 'updated_at')
        self.tree = ttk.Treeview(self.frame_dash, columns=columns, show='headings', selectmode='browse')
        for col in columns:
            self.tree.heading(col, text=col)
            if col == 'value':
                self.tree.column(col, width=260)
            elif col == 'path':
                self.tree.column(col, width=220)
            elif col == 'name':
                self.tree.column(col, width=140)
            else:
                self.tree.column(col, width=100)

        vsb = ttk.Scrollbar(self.frame_dash, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)
        self.tree.pack(side='left', fill='both', expand=True)
        vsb.pack(side='left', fill='y')

        # 우측 버튼들
        btn_frame = ttk.Frame(self.frame_dash)
        btn_frame.pack(side='right', fill='y', padx=8, pady=8)
        ttk.Button(btn_frame, text='새로고침', command=self.refresh_list).pack(fill='x', pady=4)
        ttk.Button(btn_frame, text='선택 수정', command=self.on_edit).pack(fill='x', pady=4)
        ttk.Button(btn_frame, text='선택 삭제', command=self.on_delete).pack(fill='x', pady=4)
        ttk.Button(btn_frame, text='폴더 열기', command=self.open_selected_folder).pack(fill='x', pady=4)

        # 시작 시 DB 테이블 확인 및 리스트 로드
        ensure_table()
        self.refresh_list()

    # --------------------- UI event handlers ---------------------
    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, folder)

    def on_generate(self):
        name = self.entry_name.get().strip()
        value = self.entry_value.get().strip()
        folder = self.entry_path.get().strip()

        if not name or not value or not folder:
            messagebox.showinfo('입력 필요', '이름, 값, 저장 폴더를 모두 입력해주세요.')
            return

        if not os.path.isdir(folder):
            messagebox.showinfo('폴더 없음', '지정한 폴더가 존재하지 않습니다. 폴더를 확인해주세요.')
            return

        now = datetime.now()
        filename = make_image_filename(name, now)
        fullpath = os.path.join(folder, filename)

        try:
            generate_qr_image(value, fullpath)
            uid = str(uuid.uuid4())
            insert_qr_record(uid, name, value, fullpath)
            messagebox.showinfo('생성 완료', f'QR 코드가 생성되어 저장되었습니다.\n{fullpath}')
            self.refresh_list()
        except Exception as e:
            messagebox.showerror('생성 오류', f'QR 코드 생성 중 오류가 발생했습니다.\n{e}')

    def refresh_list(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        try:
            rows = fetch_all_qr_records()
            for row in rows:
                # row: (no, id, name, value, path, created_at, updated_at)
                self.tree.insert('', 'end', values=row)
        except Exception as e:
            messagebox.showerror('조회 오류', f'레코드 조회 중 오류가 발생했습니다.\n{e}')

    def get_selected_record(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo('선택 필요', '수정 또는 삭제할 항목을 선택하세요.')
            return None
        vals = self.tree.item(sel[0], 'values')
        return vals

    def on_edit(self):
        rec = self.get_selected_record()
        if not rec:
            return
        EditWindow(self, rec, self.refresh_list)

    def on_delete(self):
        rec = self.get_selected_record()
        if not rec:
            return
        no, id_str, name, value, path, created_at, updated_at = rec
        confirm = messagebox.askyesno('삭제 확인', f'선택한 레코드를 삭제하시겠습니까?\n이 작업은 이미지 파일을 함께 삭제합니다.\n{name}')
        if not confirm:
            return
        # 파일 삭제 시도
        try:
            if os.path.isfile(path):
                os.remove(path)
        except Exception as e:
            # 파일 삭제 실패는 진행하되 사용자에게 알림
            messagebox.showinfo('파일 삭제 실패', f'이미지 파일 삭제에 실패했습니다.\n{e}')
        try:
            delete_qr_record(id_str)
            messagebox.showinfo('삭제 완료', '레코드가 삭제되었습니다.')
            self.refresh_list()
        except Exception as e:
            messagebox.showerror('삭제 오류', f'레코드 삭제 중 오류가 발생했습니다.\n{e}')

    def open_selected_folder(self):
        rec = self.get_selected_record()
        if not rec:
            return
        path = rec[4]
        folder = os.path.dirname(path)
        if os.path.isdir(folder):
            # 플랫폼별 폴더 열기
            if os.name == 'nt':
                os.startfile(folder)
            elif os.name == 'posix':
                try:
                    # mac or linux
                    if 'darwin' in os.sys.platform:
                        os.system(f'open "{folder}"')
                    else:
                        os.system(f'xdg-open "{folder}"')
                except Exception as e:
                    messagebox.showinfo('폴더 열기 실패', f'폴더를 여는 동안 오류가 발생했습니다.\n{e}')
        else:
            messagebox.showinfo('폴더 없음', '저장된 폴더가 존재하지 않습니다.')


class EditWindow(tk.Toplevel):
    def __init__(self, parent, record_values, on_done_callback):
        super().__init__(parent)
        self.title('QR 코드 수정')
        self.geometry('560x220')
        self.on_done = on_done_callback

        # record_values: (no, id, name, value, path, created_at, updated_at)
        self.record = {
            'no': record_values[0],
            'id': record_values[1],
            'name': record_values[2],
            'value': record_values[3],
            'path': record_values[4],
            'created_at': record_values[5],
            'updated_at': record_values[6]
        }

        ttk.Label(self, text='QR 코드 이름').pack(anchor='w', padx=10, pady=(10, 2))
        self.entry_name = ttk.Entry(self, width=60)
        self.entry_name.pack(padx=10, pady=4)
        self.entry_name.insert(0, self.record['name'])

        ttk.Label(self, text='QR 값 (읽기 전용)').pack(anchor='w', padx=10, pady=(8, 2))
        self.lbl_value = ttk.Label(self, text=self.record['value'], wraplength=520)
        self.lbl_value.pack(anchor='w', padx=10)

        ttk.Label(self, text='이미지 경로').pack(anchor='w', padx=10, pady=(8, 2))
        self.entry_path = ttk.Entry(self, width=60)
        self.entry_path.pack(padx=10, pady=4)
        self.entry_path.insert(0, self.record['path'])

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill='x', pady=10, padx=10)
        ttk.Button(btn_frame, text='경로 변경', command=self.change_path).pack(side='left', padx=4)
        ttk.Button(btn_frame, text='이름 변경 저장', command=self.save_changes).pack(side='left', padx=4)
        ttk.Button(btn_frame, text='레코드 및 이미지 삭제', command=self.delete_record).pack(side='right', padx=4)

    def change_path(self):
        folder = filedialog.askdirectory(initialdir=os.path.dirname(self.record['path']))
        if folder:
            # 파일 이동: 기존 파일을 새 경로로 이동
            old_path = self.record['path']
            # 새로운 파일명 (시간은 기존 파일의 생성일자 사용하여 변경 안함)
            base_name = os.path.basename(old_path)
            new_path = os.path.join(folder, base_name)
            try:
                os.replace(old_path, new_path)
                self.record['path'] = new_path
                self.entry_path.delete(0, tk.END)
                self.entry_path.insert(0, new_path)
                update_qr_record(self.record['id'], new_path=new_path)
                messagebox.showinfo('이동 완료', '이미지 파일이 이동되었습니다.')
            except Exception as e:
                messagebox.showerror('이동 오류', f'파일 이동에 실패했습니다.\n{e}')

    def save_changes(self):
        new_name = self.entry_name.get().strip()
        if not new_name:
            messagebox.showinfo('이름 필요', '새 이름을 입력하세요.')
            return

        # 파일명 변경 처리 (파일 시스템 상에서 이름 변경)
        old_path = self.record['path']
        folder = os.path.dirname(old_path)
        # 새 파일명 생성: 기존 날짜 부분 유지하려면 기존 파일명에서 시간 가져오기
        old_base = os.path.basename(old_path)
        m = re.match(r'(\d{8}_\d{6})_(.+)\.png', old_base)
        if m:
            timepart = m.group(1)
            new_filename = f"{timepart}_{sanitize_filename(new_name)}.png"
        else:
            new_filename = make_image_filename(new_name, datetime.now())

        new_path = os.path.join(folder, new_filename)
        try:
            os.replace(old_path, new_path)
            update_qr_record(self.record['id'], new_name=new_name, new_path=new_path)
            messagebox.showinfo('저장 완료', '이름 및 경로가 업데이트 되었습니다.')
            self.on_done()
            self.destroy()
        except Exception as e:
            messagebox.showerror('변경 오류', f'이름 변경 중 오류가 발생했습니다.\n{e}')

    def delete_record(self):
        confirm = messagebox.askyesno('삭제 확인', '레코드와 이미지를 영구히 삭제하시겠습니까?')
        if not confirm:
            return
        try:
            if os.path.isfile(self.record['path']):
                os.remove(self.record['path'])
        except Exception as e:
            messagebox.showinfo('파일 삭제 실패', f'이미지 파일 삭제에 실패했습니다.\n{e}')
        try:
            delete_qr_record(self.record['id'])
            messagebox.showinfo('삭제 완료', '레코드가 삭제되었습니다.')
            self.on_done()
            self.destroy()
        except Exception as e:
            messagebox.showerror('삭제 오류', f'레코드 삭제 중 오류가 발생했습니다.\n{e}')


# -------------------------------
# 예시: 빠른 생성 데모 함수
# -------------------------------

def demo_create_example(folder):
    # 예시: "https://xn--pe5b27r.com/" 를 코드 값으로, 이름: 알클 사이트
    name = '알클 사이트'
    value = 'https://xn--pe5b27r.com/'
    now = datetime.now()
    filename = make_image_filename(name, now)
    fullpath = os.path.join(folder, filename)
    generate_qr_image(value, fullpath)
    uid = str(uuid.uuid4())
    insert_qr_record(uid, name, value, fullpath)


if __name__ == '__main__':
    # DB 접속 테스트 및 테이블 생성
    try:
        ensure_table()
    except Exception as e:
        # DB 접속에 실패하면 경고창을 띄우되 프로그램은 계속 열리게 함
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror('DB 연결 실패', f'DB 연결 또는 테이블 생성에 실패했습니다.\n{e}')
        root.destroy()

    app = QRManagerApp()
    app.mainloop()
