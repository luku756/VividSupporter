from functools import partial

from Units import Units, Symbols, Level

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

# unit_list = Units.get_unit_list()

# for a in Symbols:
#     print(a.value)

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

    window.title("비비드 나이트 도우미 by Redwing (v 1.0.0)")
    window.geometry("950x660+500+200")
    # window.geometry("800x710-2500+700")
    # window.resizable(False, False)


    # 이미지 정보는 변수를 유지하지 않으면 사라진다. 그러니 미리 불러오기
    symbol_images = {}
    for s in Symbols:
        img_path = f'resource\\symbols\\{s.value}.png'
        symbol_images[s] = PhotoImage(file=img_path)

    # 이미지 정보는 변수를 유지하지 않으면 사라진다. 그러니 미리 불러오기
    unit_images = {}
    unit_list = Units.get_unit_list()
    for unit in unit_list:
        img_path = f'resource\\units\\{unit[0]}.png'

        # Resizing image to fit on button
        # photoimage = PhotoImage(file=img_path).subsample(2, 2)
        unit_images[unit[0]] = PhotoImage(file=img_path)

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
        # print(selected_symbol)
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

    # 심볼 목록 표시
    def display_symbols():
        for s in Symbols:
            tag_new_btn = tkinter.Button(symbol_list_frame, overrelief="groove", image=symbol_images[s], text=s.value,
                                         command=partial(symbol_click, s))

            Tooltip(tag_new_btn, text=s.value)

            # 관리할 상태 변수
            symbol_buttons[s] = {'button': tag_new_btn, 'state': ButtonState.unpressed}

            # text 위젯에 추가
            symbol_list_window.configure(state="normal")
            symbol_list_window.window_create("insert", window=tag_new_btn, padx=10, pady=10)
            symbol_list_window.configure(state="disabled")

    display_symbols()

    # 유닛 목록을 표시할 윈도우 생성
    unit_list_frame = tkinter.LabelFrame(window, text="선택된 심볼의 유닛 목록")
    unit_list_frame.pack(side='top', fill="both", padx=10, pady=10)

    unit_list_window = tk.Text(unit_list_frame, wrap="word", height='40',  bg='SystemButtonFace', yscrollcommand=lambda *args: unit_vsb.set(*args))
    unit_vsb = tk.Scrollbar(unit_list_frame, command=unit_list_window.yview)
    unit_vsb.pack(side="right", fill="y")
    unit_list_window.pack(side="left", fill="both", expand=True)


    # 유닛 클릭 이벤트. 유닛 화면을 비활성화한다.
    # 버튼을 누르면 눌린 상태를 유지하고, 그 상태에서 다시 누르면 원상복구한다.
    def unit_click(selected_symbol):
        print('as')
        # print(selected_symbol)
        # if symbol_buttons[selected_symbol]['state'] == ButtonState.unpressed:
        #     symbol_buttons[selected_symbol]['button']['background'] = 'gray'
        #     symbol_buttons[selected_symbol]['button'].config(relief=SUNKEN)  # 눌린 상태 유지
        #     symbol_buttons[selected_symbol]['state'] = ButtonState.pressed
        # else:
        #     symbol_buttons[selected_symbol]['button'].config(relief=RAISED)  # 눌린 상태 해제
        #     symbol_buttons[selected_symbol]['state'] = ButtonState.unpressed
        #     symbol_buttons[selected_symbol]['button']['background'] = 'SystemButtonFace'
        # 현재 ui 갱신
        # display_right_characters()

    # 현재 선택 상태에 맞는 유닛 목록을 출력한다.
    def display_right_characters():
        unit_list = Units.get_unit_list()

        unit_list_window.configure(state="normal")
        unit_list_window.delete("1.0", "end")
        unit_list_window.configure(state="disabled")

        for unit in unit_list:
            # 첫번째 심볼, 혹은 두번째 심볼이 클릭된 상태
            if symbol_buttons[unit[2]]['state'] == ButtonState.pressed or symbol_buttons[unit[3]]['state'] == ButtonState.pressed:

                # 등급에 따른 색상 테두리
                if unit[1] == Level.bronze:
                    color = '#CD7F32'
                elif unit[1] == Level.silver:
                    color = 'silver'
                elif unit[1] == Level.gold:
                    color = 'gold'

                # 전체 프레임
                unit_frame = tkinter.Frame(unit_list_frame,  bg=color #, command=partial(unit_click, s)
                                            )

                # 패딩 크기, 사실상 테두리 크기
                pad_size = 4

                unit_btn = tkinter.Label(unit_frame, image=unit_images[unit[0]], text=unit[0])
                unit_btn.pack(side='top', pady=(pad_size, 0), padx=pad_size)
                Tooltip(unit_btn, text=str(unit[0]))

                # 유닛이 지닌 심볼 표시
                symbol_frame = tkinter.Frame(unit_frame)

                symbol_first = tkinter.Label(symbol_frame, image=symbol_images[unit[2]])
                symbol_first.pack(side='left')
                Tooltip(symbol_first, text=str(unit[2].value))

                symbol_second = tkinter.Label(symbol_frame, image=symbol_images[unit[3]])
                symbol_second.pack(side='right')
                Tooltip(symbol_second, text=str(unit[3].value))

                symbol_frame.pack(side='top', pady=(0, pad_size), padx=pad_size, fill="both", expand=True)


                # 관리할 상태 변수
                # symbol_buttons[s] = {'button': tag_new_btn, 'state': ButtonState.unpressed}

                # text 위젯에 추가
                unit_list_window.configure(state="normal")
                unit_list_window.window_create("insert", window=unit_frame, padx=10, pady=10)
                unit_list_window.configure(state="disabled")


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