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

frame_left = tk.Frame(main, bg="yellow", width=main_width // 2, height=main_height)
frame_right = tk.Frame(main, bg="blue", width=main_width // 2, height=main_height)
frame_left.pack(side="left")
frame_right.pack(side="right")





# create function catalog

def create_catalog(window, fun_name, layout, cmd):

    but = tk.Button(window, text=fun_name, width=30, command=cmd)
    but.grid(row=layout[0], column=layout[1])



# command functions

def display_test_auto_cmd():
    pass



create_catalog(frame_left, "display_test_auto", [0, 0], display_test_auto_cmd)


