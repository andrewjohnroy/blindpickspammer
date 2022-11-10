"""
Copyright 2022 Andrew John Roy Stephenson andrewjohnroy@gmail.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

-------------------------------------------------------------------------------

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
