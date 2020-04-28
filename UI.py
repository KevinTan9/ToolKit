# encoding: utf-8
# by: Kevin Tang
"""
Here is the UI of program ToolKit.

"""

import tkinter as tk
import json


def config_parse(arg):
    """
    parse configuration file with json format
    :param arg: full path of json file
    :return: python data
    """
    with open(arg, 'r', encoding='utf-8') as f:
        json_str = json.load(f)
    return json_str


# get the data of config.json

config = config_parse("./config.json")


def set_center(win, width, height):
    """
    set the ui size and set it center
    :param win: ui object
    :param width: the ui width
    :param height: the ui height
    :return: null
    """
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    center_width = (screen_width - width) // 2
    center_height = (screen_height - height) // 2
    win.geometry("+%s+%s" % (center_width, center_height))


main_title = config["main_win"]["title"]
main_width = config["main_win"]["size"]["width"]
main_height = config["main_win"]["size"]["height"]

main = tk.Tk()
main.title(main_title)
main.geometry("%sx%s" % (main_width, main_height))
set_center(main, main_width, main_height)

# frame layout

frame_left = tk.Frame(main, bg="black", width=200, height=main_height)
frame_right = tk.Frame(main, bg="blue", width=main_width // 2, height=main_height)
frame_left.pack(side="left")
frame_right.pack(side="right")


lab1 = tk.Button(frame_left, text="lab1", width=frame_left.winfo_y(), bg="red")
lab2 = tk.Button(frame_left, text="lab2", width=10, bg="yellow")
lab3 = tk.Button(frame_left, text="lab3", width=10, bg="blue")
lab1.pack()
lab2.pack()
lab3.pack()
