import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import threading
import os
from datetime import datetime
import time
from plyer import notification
import re

# TTS 초기화
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 말하는 속도 설정

# 메모 저장 폴더 생성
os.makedirs("memos", exist_ok=True)

# 음성 인식기 초기화
recognizer = sr.Recognizer()

# TTS로 음성 출력 함수
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 알림 출력 함수
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

# 시간 알림 기능
def tell_time():
    now = datetime.now().strftime("%H시 %M분")
    response = f"현재 시간은 {now}입니다."
    speak(response)
    show_notification("현재 시간", now)
    update_result_label(response)

# 메모 저장 기능
def save_memo():
    update_result_label("메모 내용을 말씀해주세요...")
    speak("메모 내용을 말씀해주세요")

    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
            memo_text = recognizer.recognize_sphinx(audio, language='ko-KR')
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"memos/memo_{timestamp}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(memo_text)
            response = "메모를 저장했어요"
            speak(response)
            show_notification("메모 저장됨", memo_text)
            update_result_label(response)
        except sr.UnknownValueError:
            update_result_label("메모를 인식하지 못했습니다.")
        except Exception as e:
            update_result_label(f"오류 발생: {e}")

# 타이머 기능
def set_timer(duration_text):
    # 숫자와 단위(초/분) 추출
    match = re.search(r'(\d+)\s*(초|분)', duration_text)
    if not match:
        update_result_label("타이머 시간을 인식하지 못했어요.")
        return

    number = int(match.group(1))
    unit = match.group(2)

    seconds = number * 60 if unit == "분" else number

    response = f"{number}{unit} 타이머를 시작할게요."
    speak(response)
    show_notification("타이머 시작", f"{number}{unit} 후 알림 예정")
    update_result_label(response)

    # 타이머 백그라운드 실행
    def timer_thread():
        time.sleep(seconds)
        done_message = f"{number}{unit}이 지났어요."
        speak(done_message)
        show_notification("타이머 완료", done_message)
        update_result_label(done_message)

    threading.Thread(target=timer_thread, daemon=True).start()

# 명령어 처리 함수
def process_command(command):
    command = command.strip()
    if "시간" in command:
        tell_time()
    elif "메모" in command:
        save_memo()
    elif "타이머" in command:
        set_timer(command)
    else:
        response = "명령어를 이해하지 못했어요."
        speak(response)
        update_result_label(response)

# 음성 인식 시작 함수
def start_listening():
    button.config(text="인식 중...")
    update_result_label("말씀을 듣고 있어요...")

    def listen():
        with sr.Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_sphinx(audio, language='ko-KR')
                print("인식된 명령어:", command)
                process_command(command)
            except sr.UnknownValueError:
                update_result_label("말을 이해하지 못했어요.")
            except Exception as e:
                update_result_label(f"오류 발생: {e}")
            finally:
                button.config(text="말씀하세요")

    threading.Thread(target=listen, daemon=True).start()

# 결과 표시 라벨 업데이트 함수
def update_result_label(text):
    result_label.config(text=text)

# GUI 설정
app = tk.Tk()
app.title("음성 비서")
app.geometry("400x300")

title_label = tk.Label(app, text="음성 비서", font=("Arial", 18))
title_label.pack(pady=10)

button = tk.Button(app, text="말씀하세요", font=("Arial", 14), command=start_listening)
button.pack(pady=20)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=10)

guide_label = tk.Label(app, text="예시: 지금 몇 시야 / 메모해줘 / 3분 타이머 설정해줘", fg="gray", wraplength=300)
guide_label.pack(side="bottom", pady=10)

app.mainloop()
