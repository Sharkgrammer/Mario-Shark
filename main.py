import time
import keyboard as keyboard

from data import SharkData

WAIT_MAX, WAIT_MIN = 0.06, 0.2
counter, shark = 0, 1
active = True


def stop():
    global active

    active = False


def get_wait(time_count):
    percent = time_count / sharks.time_max

    return (WAIT_MAX * percent) + WAIT_MIN


def keypress(k, wait):
    keyboard.send(k, do_release=False)
    print(f"S{shark}: {counter}/{length} -> {keys}, {round(wait, 2)} ")

    time.sleep(wait)
    keyboard.release(k)


sharks = SharkData()
active_shark = sharks.sort_data(shark)

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

    keypress(keys, get_wait(s['time_count']))

    if counter < length - 1:
        counter += 1
    else:
        counter = 0

        '''
        Code to auto change the shark if program was to be left running forever
        
        shark = shark + 1 if shark < 10 else 1
        length = active_shark["Shark"].count()
        '''
