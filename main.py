import time

import keyboard as keyboard

from data import SharkData

sharks = SharkData()

shark_1 = sharks.sort_data(1)
# sharks.describe_data(shark_1)

length = shark_1["Shark"].count()

counter = 0
active = True

keyboard.wait('f9')
keyboard.write('Test text here')

while active:
    s = shark_1.iloc[counter]
    time.sleep(0.05)

    print(f"{s['up']} {s['right']} {counter}:{length}")
    counter = (counter + 1) if counter < length - 1 else 0
