import tkinter as tk
def create_main_window():
    window = tk.Tk()
    window.geometry("300x200")

    # 라벨 추가
    label = tk.Label(window, text="hello A")
    label.pack(pady=50)
    
    # 종료 버튼 추가
    exit_button = tk.Button(window, text="종료", command=window.destroy)
    exit_button.pack()
    
    return window
