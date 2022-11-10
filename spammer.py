"""Mid Spammer for allpick in League of Legends

This spams mid by pressing mouse3, typing "mid", then pressing enter
"""
import mouse
import keyboard


def spam():
    """Callback for creating mid spam"""
    mouse.click()
    keyboard.write("mid\n")


mouse.on_middle_click(spam)
input("Press Enter Key to Exit.")
