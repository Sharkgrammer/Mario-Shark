import time
import random
import keyboard as keyboard

from data import SharkData

counter, shark = 0, 1
active = True


def stop():
    global active

    active = False


def keypress(k, wait):
    keyboard.send(k, do_release=False)
    print(f"S{shark}: {counter}/{length} -> {keys}, {round(wait, 2)} ")

    time.sleep(wait)
    keyboard.release(k)


sharks = SharkData()
active_shark = sharks.sort_data(shark)

sharks.describe_data(active_shark)

length = active_shark["Shark"].count()
keyboard.add_hotkey('shift+2', lambda: stop())

print(f"Keyboard ready and waiting! Input Length {length} for shark {shark}")
keyboard.wait('shift+1')

while active:
    s = active_shark.iloc[counter]

    keys = [
        "s" if s['up'] else "down",
        "right" if s['right'] else "left"
    ]

    wait = random.uniform(0.06, 0.3)

    keypress(keys, wait)

    '''
    if counter < length - 1:
        counter += 1
    else:
        counter = 0

        shark = shark + 1 if shark < 10 else 1
        length = active_shark["Shark"].count()
    '''
