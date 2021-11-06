from functools import partial

from Units import Units, Symbols, Level, ColorSymbols , MarkSymbols

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

# 컴파일 시 리소스 가져오기
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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

    window.title("비비드 나이트 도우미 by Redwing (v 1.1.0)")
    window.geometry("1100x800+500+100")
    # window.geometry("800x710-2500+700")
    # window.resizable(False, False)

    window.iconbitmap(resource_path('resource\\logo.ico'))
    # window.iconphoto(False, tk.PhotoImage(file=resource_path('resource\\아멜리.jpg')))

    # 상단 메뉴 추가
    menubar = tkinter.Menu(window)

    # 초기화 메뉴 클릭
    def click_clear_menu(menu):
        for s in Symbols: # 모든 버튼이 안 눌린 상태로 변경
            symbol_buttons[s]['button'].config(relief=RAISED)  # 눌린 상태 해제
            symbol_buttons[s]['state'] = ButtonState.unpressed
            symbol_buttons[s]['button']['background'] = 'SystemButtonFace'

        if menu == 'new game':  # 랜덤유닛 선택지도 같이 초기화
            # 선택 데이터 초기화
            Units.reset_random_unit()
            # 심볼 이미지 초기화
            for u in Units.get_random_unit_list():
                random_unit_selected_symbols[u[0]][0].config(image=symbol_images[Symbols.random_color])  # 이미지 변경
                random_unit_selected_symbols[u[0]][1].config(image=symbol_images[Symbols.random_mark])  # 이미지 변경

        display_right_units()  # 화면 갱신

    menubar.add_cascade(label="새 게임", command=partial(click_clear_menu, 'new game'))
    menubar.add_cascade(label="선택 초기화", command=partial(click_clear_menu, 'clear'))
    window.config(menu=menubar)

    # 이미지 정보는 변수를 유지하지 않으면 사라진다. 그러니 미리 불러오기
    symbol_images = {}
    for s in Symbols:
        img_path = f'resource\\symbols\\{s.value}.png'
        symbol_images[s] = PhotoImage(file=resource_path(img_path))

    # 이미지 정보는 변수를 유지하지 않으면 사라진다. 그러니 미리 불러오기
    unit_images = {}
    unit_list = Units.get_unit_list()
    for unit in unit_list:
        img_path = f'resource\\units\\{unit[0]}.png'

        # Resizing image to fit on button
        # photoimage = PhotoImage(file=img_path).subsample(2, 2)
        unit_images[unit[0]] = PhotoImage(file=resource_path(img_path))


    upper_frame = tkinter.Frame(window)
    upper_frame.pack(side="top")

    # 심볼 목록 표시
    symbol_list_frame = tkinter.LabelFrame(upper_frame, text="심볼 선택")
    symbol_list_frame.pack(side='left', fill="both", padx=10, pady=10)

    # 심볼 표시
    symbol_list_window = tk.Text(symbol_list_frame, wrap="word", width='100', height='15', bg='SystemButtonFace', yscrollcommand=lambda *args: symbol_vsb.set(*args))
    symbol_vsb = tk.Scrollbar(symbol_list_frame, command=symbol_list_window.yview)
    symbol_vsb.pack(side="right", fill="y")
    symbol_list_window.pack(side="left", fill="both", expand=True)


    # 랜덤 유닛의 속성 선택
    random_unit_select_symbol = tkinter.LabelFrame(upper_frame,  text="랜덤유닛 속성", width='5')
    random_unit_select_symbol.pack(side="right")

    # label = tkinter.Label(random_unit_select_symbol, text="궁정화가 지르콘")
    # label.pack(side='top')

    # 랜덤 유닛 심볼 정보
    random_unit_selected_symbols = {}

    # 랜덤유닛의 옵션 설정 기능 추가
    def add_random_unit(upper_widget, name):
        def click_menu(clicked, symbol_type, btn, unit_name):
            btn.config(image=symbol_images[clicked.value])  # 이미지 변경
            Units.set_random_unit_state(unit_name, symbol_type, clicked.value)  # 상태 결정
            display_right_units() # 화면 갱신

        # 메뉴를 만들어 심볼 선택
        def create_menu(widget, unit_name):
            menu = tkinter.Menu(widget, tearoff=0)
            # print(widget['text'])
            if widget['text'] == '컬러랜덤':
                for s in ColorSymbols:
                    menu.add_command(image=symbol_images[s.value], command=partial(click_menu, s, widget['text'], widget, unit_name))
            else:
                for s in MarkSymbols:
                    menu.add_command(image=symbol_images[s.value], command=partial(click_menu, s, widget['text'], widget, unit_name))

            widget["menu"] = menu

        te = tkinter.LabelFrame(upper_widget, text=name)

        symbol_1 = tkinter.Menubutton(te, image=symbol_images[Symbols.random_color], text=Symbols.random_color.value,
                                      relief="raised", direction="right")
        symbol_1.pack(side="left")
        create_menu(symbol_1, name)

        symbol_2 = tkinter.Menubutton(te, image=symbol_images[Symbols.random_mark], text=Symbols.random_mark.value,
                                      relief="raised", direction="right")
        symbol_2.pack(side="right")

        # 심볼을 변수로 관리
        random_unit_selected_symbols[name] = [symbol_1, symbol_2]

        create_menu(symbol_2, name)
        te.pack(side="top", padx=10, pady=10)

    add_random_unit(random_unit_select_symbol, '궁정 화가 지르콘')
    add_random_unit(random_unit_select_symbol, '점성술사 래브라')

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
        display_right_units()

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

    unit_list_window = tk.Text(unit_list_frame, wrap="word", height='40',
                               bg='SystemButtonFace', yscrollcommand=lambda *args: unit_vsb.set(*args))
    unit_vsb = tk.Scrollbar(unit_list_frame, command=unit_list_window.yview)
    unit_vsb.pack(side="right", fill="y")
    unit_list_window.pack(side="left", fill="both", expand=True)

    # 현재 선택 상태에 맞는 유닛 목록을 출력한다.
    def display_right_units():
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
                unit_frame = tkinter.Frame(unit_list_frame,  bg=color) #, command=partial(unit_click, s)


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