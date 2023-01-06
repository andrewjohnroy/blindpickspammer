"""
Mid Spammer for allpick in League of Legends

Types "mid" in chat when you press the scroll wheel down.

You must place your mouse over the chat input area first.
"""
import mouse
import keyboard


def spam():
    """Callback for creating mid spam"""
    mouse.click()
    keyboard.write("mid\nhttps://discord.gg/De97gMqpCH\n")


mouse.on_middle_click(spam)
input("Press Enter Key to Exit.")
