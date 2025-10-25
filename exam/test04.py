import tkinter as tk
import random

class ColorMemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Memory Grid")

        # 색상 목록
        self.colors = ["red", "blue", "yellow", "green", "orange"]

        # 게임 상태 초기화
        self.sequence = []          # 정답 색상 순서
        self.user_sequence = []     # 사용자가 누른 순서
        self.level = 1              # 현재 라운드
        self.flash_time = 1000      # 색상 번쩍이는 시간(ms)

        # 점수 라벨
        self.status_label = tk.Label(self.root, text="게임을 시작하세요!", font=("Arial", 14))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        # 게임 시작 버튼
        self.start_button = tk.Button(self.root, text="게임 시작", command=self.start_game)
        self.start_button.grid(row=1, column=0, columnspan=3, pady=10)

        # 3x3 버튼 그리드 생성
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(self.root, width=10, height=5,
                                command=lambda x=i, y=j: self.handle_click(x, y))
                btn.grid(row=i+2, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def start_game(self):
        self.sequence = []
        self.user_sequence = []
        self.status_label.config(text=f"레벨 {self.level}: 순서를 잘 기억하세요!")
        self.start_button.config(state="disabled")
        self.generate_sequence()
        self.show_sequence()

    def generate_sequence(self):
        # 순서에 새로운 위치 추가
        for _ in range(self.level + 2):  # 레벨 1에서 3개, 이후로 +1씩 증가
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            color = random.choice(self.colors)
            self.sequence.append(((x, y), color))

    def show_sequence(self):
        delay = 0
        for index, ((x, y), color) in enumerate(self.sequence):
            # 원래 색으로 되돌리는 시간 포함하여 색상 번쩍이기 구현
            self.root.after(delay, lambda x=x, y=y, c=color: self.flash_button(x, y, c))
            delay += self.flash_time + 300

        # 사용자 입력 허용 시작
        self.root.after(delay, self.enable_input)

    def flash_button(self, x, y, color):
        original_color = self.buttons[x][y].cget("background")
        self.buttons[x][y].config(bg=color)
        self.root.after(self.flash_time, lambda: self.buttons[x][y].config(bg=original_color))

    def enable_input(self):
        self.user_sequence = []
        self.status_label.config(text="같은 순서대로 눌러보세요!")

    def handle_click(self, x, y):
        if len(self.user_sequence) >= len(self.sequence):
            return  # 더 이상 입력받지 않음

        self.user_sequence.append((x, y))
        self.buttons[x][y].config(relief="sunken")
        self.root.after(200, lambda: self.buttons[x][y].config(relief="raised"))

        # 누른 순서가 지금까지 맞는지 확인
        expected_x, expected_y = self.sequence[len(self.user_sequence)-1][0]
        if (x, y) != (expected_x, expected_y):
            self.game_over()
            return

        # 모두 맞춘 경우
        if len(self.user_sequence) == len(self.sequence):
            self.level += 1
            self.flash_time = max(100, int(self.flash_time * 0.9))  # 난이도 점점 증가
            self.status_label.config(text="성공! 다음 라운드로...")
            self.root.after(1000, self.start_game)

    def game_over(self):
        self.status_label.config(text="실패! 다시 도전하시겠어요?")
        self.start_button.config(state="normal", text="다시 시작")
        self.level = 1
        self.flash_time = 1000


if __name__ == "__main__":
    root = tk.Tk()
    game = ColorMemoryGame(root)
    root.mainloop()