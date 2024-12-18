import time
import random
import keyboard as keyboard

from data import SharkData

counter = 0
active = True


def stop():
    global active

    active = False


def keypress(keys):
    keyboard.send(keys, do_release=False)
    time.sleep(random.uniform(0.1, 0.3))
    keyboard.release(keys)


sharks = SharkData()

shark_1 = sharks.sort_data(1)
# sharks.describe_data(shark_1)

length = shark_1["Shark"].count()

print("Keyboard read and waiting!")

keyboard.add_hotkey('shift+2', lambda: stop())
keyboard.wait('shift+1')

while active:
    s = shark_1.iloc[counter]
    up, right = s['up'], s['right']

    keys = [
        "s" if up else "down",
        "right" if right else "left"
    ]

    print(f"Keys pressed: {keys}")
    keypress(keys)

    counter = (counter + 1) if counter < length - 1 else 0
