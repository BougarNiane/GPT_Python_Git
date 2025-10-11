import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
import datetime
import os

class TTSApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Text to Speech Converter')
        self.root.geometry('500x400')

        # 텍스트 입력창
        self.text_label = tk.Label(root, text='텍스트 입력', font=('Arial', 12))
        self.text_label.pack(pady=10)

        self.text_input = tk.Text(root, height=10, width=50)
        self.text_input.pack(pady=10)

        # 변환 버튼
        self.convert_button = tk.Button(root, text='음성 변환', command=self.convert_text_to_speech, bg='#4CAF50', fg='white', font=('Arial', 12))
        self.convert_button.pack(pady=10)

        # 상태 표시 라벨
        self.status_label = tk.Label(root, text='', font=('Arial', 10), fg='gray')
        self.status_label.pack(pady=10)

    def convert_text_to_speech(self):
        text = self.text_input.get('1.0', 'end').strip()
        if not text:
            messagebox.showwarning('경고', '텍스트를 입력하세요!')
            return

        try:
            self.status_label.config(text='Synthesizing speech (gTTS)...')
            self.root.update_idletasks()

            # 파일 이름 규칙: 연월일_시분초_처음텍스트10글자.mp3
            now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            short_text = text[:10].replace('\n', ' ').replace('\r', '')
            filename = f"{now}_{short_text}.mp3"

            # 저장 경로 선택
            save_path = filedialog.asksaveasfilename(defaultextension='.mp3', initialfile=filename, filetypes=[('MP3 files', '*.mp3')])
            if not save_path:
                self.status_label.config(text='저장 취소됨')
                return

            # gTTS 변환 및 저장
            tts = gTTS(text=text, lang='ko')
            tts.save(save_path)

            self.status_label.config(text=f'변환 완료: {os.path.basename(save_path)}')
            messagebox.showinfo('완료', f'음성 파일이 저장되었습니다.\n\n{save_path}')

        except Exception as e:
            messagebox.showerror('오류', f'음성 변환 중 문제가 발생했습니다:\n{e}')
            self.status_label.config(text='오류 발생')

if __name__ == '__main__':
    root = tk.Tk()
    app = TTSApp(root)
    root.mainloop()