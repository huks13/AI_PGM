import tkinter as tk
from tkinter import messagebox

# 버튼 클릭
def click(value):
    entry.insert(tk.END, value)

# 초기화
def clear():
    entry.delete(0, tk.END)

# 계산
def calculate():
    try:
        expression = entry.get().replace("×", "*").replace("÷", "/")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("오류", "0으로 나눌 수 없습니다.")
    except Exception:
        messagebox.showerror("오류", "잘못된 수식입니다.")

# 창 생성
window = tk.Tk()
window.title("GUI 계산기")
window.geometry("350x500")
window.minsize(300, 400)      # 최소 크기
window.resizable(True, True)  # 리사이즈 허용

# 행/열 크기 비율 설정
for i in range(6):   # 입력창 + 버튼 5줄
    window.grid_rowconfigure(i, weight=1)

for j in range(4):   # 4열
    window.grid_columnconfigure(j, weight=1)

# 입력창
entry = tk.Entry(window, font=("맑은 고딕", 22), justify="right")
entry.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=5,
    pady=5,
    sticky="nsew"
)

# 버튼 정보
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("÷",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("×",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("C",4,2), ("+",4,3),
]

# 버튼 생성
for (text, row, col) in buttons:
    if text == "C":
        cmd = clear
    else:
        cmd = lambda t=text: click(t)

    tk.Button(
        window,
        text=text,
        font=("맑은 고딕", 18),
        command=cmd
    ).grid(
        row=row,
        column=col,
        padx=3,
        pady=3,
        sticky="nsew"
    )

# = 버튼
tk.Button(
    window,
    text="=",
    font=("맑은 고딕", 20, "bold"),
    command=calculate
).grid(
    row=5,
    column=0,
    columnspan=4,
    padx=3,
    pady=3,
    sticky="nsew"
)

window.mainloop()