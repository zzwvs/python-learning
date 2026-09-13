# import tkinter as tk
# import random

# class Minesweeper:
#     def __init__(self, root):
#         self.root = root
#         self.width = 10
#         self.height = 10
#         self.mines = 10
#         self.buttons = []
#         self.game_over = False
#         self.create_board()
#         self.create_widgets()

#     def create_board(self):
#         self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
#         self.mine_positions = set()
#         while len(self.mine_positions) < self.mines:
#             x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
#             if (x, y) not in self.mine_positions:
#                 self.mine_positions.add((x, y))
#                 self.place_mines(x, y)

#     def place_mines(self, x, y):
#         for dx in range(-1, 2):
#             for dy in range(-1, 2):
#                 if 0 <= x + dx < self.width and 0 <= y + dy < self.height and (x + dx, y + dy) not in self.mine_positions:
#                     self.board[y + dy][x + dx] += 1

#     def create_widgets(self):
#         for y in range(self.height):
#             row = []
#             for x in range(self.width):
#                 button = tk.Button(self.root, command=lambda x=x, y=y: self.click(x, y), width=2, height=1)
#                 button.grid(row=y, column=x)
#                 row.append(button)
#                 self.buttons.append(button)
#             self.buttons.append(row)

#     def click(self, x, y):
#         if self.game_over:
#             return
#         if (x, y) in self.mine_positions:
#             self.game_over = True
#             for button in self.buttons:
#                 if button in self.buttons:
#                     self.buttons.remove(button)
#                     button.config(text="X", state=tk.DISABLED)
#             self.buttons.append(tk.Button(self.root, text="Game Over", width=10, height=2, state=tk.DISABLED))
#             self.buttons[-1].grid(row=self.height, column=self.width // 2)
#             for button in self.buttons:
#                 if button not in self.buttons[-1:0]:
#                     button.config(state=tk.DISABLED)
#         else:
#             self.buttons[y * self.width + x].config(text=str(self.board[y][x]), state=tk.DISABLED)

#     def start(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Minesweeper")
#     game = Minesweeper(root)
#     game.start()




































import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, root, rows=16, cols=16, mines=20):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.mines = mines

        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()

        # 初始化游戏
        self.create_widgets()
        self.place_mines()
        self.calculate_numbers()

    def create_widgets(self):
        self.buttons = [[tk.Button(self.root, width=2, height=1, font='Arial 12', relief='raised', command=lambda r=i, c=j: self.reveal(r, c)) for j in range(self.cols)] for i in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].grid(row=i, column=j, sticky="nsew")
        
        # 点击右键标记地雷
        self.root.bind("<Button-3>", self.mark_mine)

    def place_mines(self):
        # 随机放置地雷
        while len(self.mine_positions) < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            self.mine_positions.add((r, c))
        
        # 确保生成的地图不包含地雷的区域，后期可用

    def calculate_numbers(self):
        # 统计每个格子周围雷的数量
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in self.mine_positions:
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                                if (r + dr, c + dc) in self.mine_positions:
                                    count += 1
                    self.board[r][c] = count

    def reveal(self, r, c):
        if self.revealed[r][c]:
            return
        
        if (r, c) in self.mine_positions:
            self.buttons[r][c].config(text="*", bg="red", relief="sunken")
            self.game_over()
        else:
            self.revealed[r][c] = True
            self.buttons[r][c].config(text=str(self.board[r][c]) if self.board[r][c] > 0 else "", relief="sunken")
            # 如果是数字且周围没有雷，可以展开周围格子（可选）
            if self.board[r][c] == 0:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                            self.reveal(r + dr, c + dc)
        
        # 检查胜利条件
        if self.check_win():
            self.game_win()

    def check_win(self):
        # 胜利条件：所有非雷格子都被翻开
        for r, c in self.mine_positions:
            if not self.revealed[r][c]:
                return False
        return True

    def game_over(self):
        # 显示所有雷的坐标
        for r, c in self.mine_positions:
            self.buttons[r][c].config(text="*", bg="red", relief="sunken")
        messagebox.showinfo("Game Over", "你踩到了地雷，游戏结束！")
        self.root.after(1000, self.root.destroy)

    def game_win(self):
        messagebox.showinfo("Congratulations", "你赢了！")
        self.root.after(1000, self.root.destroy)

    def mark_mine(self, event):
        # 右键标记地雷
        for i in range(self.rows):
            for j in range(self.cols):
                if self.buttons[i][j].winfo_containing(event.x_root, event.y_root) == self.buttons[i][j]:
                    if not self.revealed[i][j]:
                        # 标记为？
                        self.buttons[i][j].config(text="?", relief="groove", bg="yellow")
                    return

def main():
    root = tk.Tk()
    root.title("扫雷游戏")
    root.geometry("250x250")  # 250x250 窗口面积，适合 16x16 的格子
    root.resizable(False, False)
    root.configure(bg="lightgray")

    # 设置表格的大小，每个格子 15x15 像素
    for i in range(16):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    game = Minesweeper(root, rows=16, cols=16, mines=20)
    root.mainloop()

if __name__ == "__main__":
    main()