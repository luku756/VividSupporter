from functools import partial

from Units import Units, Symbols

import os
from Tootip import Tooltip

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter
import json
import tkinter
import tkinter.font
import tkinter.ttk
from urllib import request

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from enum import Enum

class ButtonState(Enum):
    pressed = 0
    unpressed = 1

unit_list = Units.get_unit_list()

for a in Symbols:
    print(a.value)

def create_gui():

    window = tkinter.Tk()

    def close(event):
        window.destroy()  # if you want to bring it back

    window.bind('<Escape>', close)  # esc 로 종료 가능

    # 위치 설정
    window.lift()
    window.attributes('-topmost', 1)
    window.after(1, lambda: window.focus_force())
    window.attributes('-topmost', 0)

    window.title("비비드 나이트 도우미 by Redwing")
    window.geometry("950x660+500+200")
    # window.geometry("800x710-2500+700")
    # window.resizable(False, False)

    # 심볼 목록 표시
    symbol_list_frame = tkinter.LabelFrame(window, text="심볼 선택")
    symbol_list_frame.pack(side='top', fill="both", padx=10, pady=10)

    # 심볼 표시
    symbol_list_window = tk.Text(symbol_list_frame, wrap="word", height='10', bg='SystemButtonFace', yscrollcommand=lambda *args: symbol_vsb.set(*args))
    symbol_vsb = tk.Scrollbar(symbol_list_frame, command=symbol_list_window.yview)
    symbol_vsb.pack(side="right", fill="y")
    symbol_list_window.pack(side="left", fill="both", expand=True)

    # 심볼 클릭 이벤트. 아래에 디스플레이 되는 목록을 변경한다.
    # 버튼을 누르면 눌린 상태를 유지하고, 그 상태에서 다시 누르면 원상복구한다.
    def symbol_click(selected_symbol):
        print(selected_symbol)
        if symbol_buttons[selected_symbol]['state'] == ButtonState.unpressed:
            symbol_buttons[selected_symbol]['button']['background'] = 'gray'
            symbol_buttons[selected_symbol]['button'].config(relief=SUNKEN)  # 눌린 상태 유지
            symbol_buttons[selected_symbol]['state'] = ButtonState.pressed
        else:
            symbol_buttons[selected_symbol]['button'].config(relief=RAISED)  # 눌린 상태 해제
            symbol_buttons[selected_symbol]['state'] = ButtonState.unpressed
            symbol_buttons[selected_symbol]['button']['background'] = 'SystemButtonFace'
        # 현재 ui 갱신
        display_right_characters()

    # 심볼과 해당 심볼 버튼 상태
    symbol_buttons = {}
    # 이미지 정보는 변수를 유지하지 않으면 사라진다
    symbol_images = {}

    # 심볼 목록 표시
    def display_symbols():

        for s in Symbols:
            img_path = f'resource\\symbols\\{s.value}.png'
            symbol_images[s] = PhotoImage(file=img_path)

            tag_new_btn = tkinter.Button(symbol_list_frame, overrelief="groove", image=symbol_images[s], text=s.value,
                                         command=partial(symbol_click, s))

            Tooltip(tag_new_btn, text=s.value)

            # 관리할 상태 변수
            symbol_buttons[s] = {'button': tag_new_btn, 'state': ButtonState.unpressed}

            symbol_list_window.configure(state="normal")
            symbol_list_window.window_create("insert", window=tag_new_btn, padx=10, pady=10)
            symbol_list_window.configure(state="disabled")

            # 꽉차면 위치를 바꿔가며 채우기
            # tag_new_btn.grid(row=grid_index_y, column=grid_index_x)
            # # tag_new_btn.pack(side='top', fill="both", padx=10, pady=10)
            # grid_index_x = grid_index_x + 1
            # if grid_index_x == grid_x_max:
            #     grid_index_x = 0
            #     grid_index_y = grid_index_y + 1

            # print(s.value)

    display_symbols()


    # 심볼 목록 표시
    character_list_frame = tkinter.LabelFrame(window, text="선택된 심볼의 유닛 목록")
    character_list_frame.pack(side='top', fill="both", padx=10, pady=10)

    # 심볼 표시
    character_list_window = tk.Text(character_list_frame, wrap="word", yscrollcommand=lambda *args: character_vsb.set(*args))
    character_vsb = tk.Scrollbar(character_list_frame, command=character_list_window.yview)
    character_vsb.pack(side="right", fill="y")
    character_list_window.pack(side="left", fill="both", expand=True)

    # 현재 선택 상태에 맞는 캐릭터 목록을 출력한다.
    def display_right_characters():
        print('a')



    # 메인루프 시작
    window.mainloop()



create_gui()

COUNT = 0
def test():
    import tkinter as tk

    root = tk.Tk()
    toolbar = tk.Frame(root)
    text = tk.Text(root, wrap="word", yscrollcommand=lambda *args: vsb.set(*args))
    vsb = tk.Scrollbar(root, command=text.yview)

    toolbar.pack(side="top", fill="x")
    vsb.pack(side="right", fill="y")
    text.pack(side="left", fill="both", expand=True)

    def event():
        print('pal')

    def add_widget():
        global COUNT
        # COUNT += 1
        widget = tk.Button(root, width=12, text=f"Widget #{COUNT}", bd=1, relief="raised", command=event,
                          bg="#5C9BD5", foreground="white", padx=4, pady=4)
        text.configure(state="normal")
        text.window_create("insert", window=widget, padx=10, pady=10)
        text.configure(state="disabled")

    add_button = tk.Button(toolbar, command=add_widget, text="Add")
    add_button.pack(side="left")

    for i in range(9):
        add_widget()

    root.mainloop()


#test()