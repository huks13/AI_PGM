import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("메모장")
root.geometry("900x600")

filename = None
modified = False


# -----------------------------
# 제목 업데이트
# -----------------------------
def update_title():
    name = "새 문서" if filename is None else filename.split("/")[-1]
    star = "*" if modified else ""
    root.title(f"{star}{name} - 메모장")


# -----------------------------
# 새 파일
# -----------------------------
def new_file():
    global filename, modified

    if modified:
        answer = messagebox.askyesnocancel("저장", "변경 내용을 저장하시겠습니까?")
        if answer:
            save_file()
        elif answer is None:
            return

    text.delete("1.0", tk.END)
    filename = None
    modified = False
    update_title()


# -----------------------------
# 열기
# -----------------------------
def open_file():
    global filename, modified

    path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not path:
        return

    with open(path, "r", encoding="utf-8") as f:
        text.delete("1.0", tk.END)
        text.insert("1.0", f.read())

    filename = path
    modified = False
    update_title()


# -----------------------------
# 저장
# -----------------------------
def save_file():
    global filename, modified

    if filename is None:
        return save_as()

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", tk.END))

    modified = False
    update_title()


# -----------------------------
# 다른 이름으로 저장
# -----------------------------
def save_as():
    global filename, modified

    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not path:
        return

    filename = path

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", tk.END))

    modified = False
    update_title()


# -----------------------------
# 종료
# -----------------------------
def exit_app():
    if modified:
        answer = messagebox.askyesnocancel("종료", "저장하시겠습니까?")
        if answer:
            save_file()
        elif answer is None:
            return

    root.destroy()


# -----------------------------
# 수정 감지
# -----------------------------
def on_modified(event=None):
    global modified

    modified = text.edit_modified()
    update_title()
    text.edit_modified(False)
    update_cursor()


# -----------------------------
# 커서 위치
# -----------------------------
def update_cursor(event=None):
    line, col = text.index(tk.INSERT).split(".")
    status.config(text=f"Ln {line}, Col {int(col)+1}")


# -----------------------------
# 메뉴
# -----------------------------
menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="새로 만들기", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="열기", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="저장", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="다른 이름으로 저장", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="종료", command=exit_app)

menu.add_cascade(label="파일", menu=file_menu)


edit_menu = tk.Menu(menu, tearoff=0)
edit_menu.add_command(label="실행 취소", command=text.edit_undo if False else lambda: text.event_generate("<<Undo>>"))
edit_menu.add_command(label="다시 실행", command=lambda: text.event_generate("<<Redo>>"))
edit_menu.add_separator()
edit_menu.add_command(label="잘라내기", command=lambda: text.event_generate("<<Cut>>"))
edit_menu.add_command(label="복사", command=lambda: text.event_generate("<<Copy>>"))
edit_menu.add_command(label="붙여넣기", command=lambda: text.event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="모두 선택", command=lambda: text.tag_add("sel", "1.0", "end"))

menu.add_cascade(label="편집", menu=edit_menu)

root.config(menu=menu)


# -----------------------------
# 텍스트 영역
# -----------------------------
text = tk.Text(
    root,
    undo=True,
    wrap="word",
    font=("맑은 고딕", 11)
)

text.pack(fill="both", expand=True)

status = tk.Label(root, anchor="e", relief="sunken")
status.pack(fill="x")


# -----------------------------
# 이벤트
# -----------------------------
text.bind("<<Modified>>", on_modified)
text.bind("<KeyRelease>", update_cursor)
text.bind("<ButtonRelease>", update_cursor)

root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())

root.protocol("WM_DELETE_WINDOW", exit_app)

update_title()
update_cursor()

root.mainloop()