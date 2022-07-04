# -*- coding: utf-8 -*-

import random
from re import X
import pyautogui as pg
import sys


def printPosition():
    x, y = pg.position()
    positionStr = 'X: ' + str(x) + ',  Y: ' + str(y)
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)


print('Press Ctrl-C to quit.')

try:
    # 移動範囲
    X1 = 1600
    Y1 = 256
    X2 = 2240
    Y2 = 960
    # 移動長さ
    LEN = 10
    # 現在位置
    x = 1920
    y = 512
    # 移動回数
    cnt = 0
    while True:
        # 方向
        direction = random.randint(0, 3)

        # 右へ
        if direction == 0:
            if x + LEN <= X2:
                x += LEN
            else:
                x -= LEN
        # 左へ
        elif direction == 1:
            if x - LEN >= X1:
                x -= LEN
            else:
                x += LEN
        # 下へ
        if direction == 2:
            if y + LEN <= Y2:
                y += LEN
            else:
                y -= LEN
        # 上へ
        elif direction == 3:
            if y - LEN >= Y1:
                y -= LEN
            else:
                y += LEN

        # 移動
        pg.moveTo(x, y, 1)
        printPosition()

        cnt += 1
        if cnt % 100 == 0:
            pg.click()

except KeyboardInterrupt:
    print('/n')
