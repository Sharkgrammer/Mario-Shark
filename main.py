import time
import random
import keyboard as keyboard

from data import SharkData

counter, shark = 0, 1
active = True


def stop():
    global active

    active = False


def keypress(k):
    keyboard.send(k, do_release=False)
    wait = random.uniform(0.06, 0.3)
    print(f"{keys}, {wait} ")

    time.sleep(wait)
    keyboard.release(k)


sharks = SharkData()
shark_1 = sharks.sort_data(shark)

length = shark_1["Shark"].count()
keyboard.add_hotkey('shift+2', lambda: stop())

print(f"Keyboard ready and waiting! Input Length {length} for shark {shark}")
keyboard.wait('shift+1')

while active:
    s = shark_1.iloc[counter]

    keys = [
        "s" if s['up'] else "down",
        "right" if s['right'] else "left"
    ]

    keypress(keys)

    counter = (counter + 1) if counter < length - 1 else 0
