import os
import time
from random import randint

def next_gen():
    n = int(raw_input('width:'))
    m = int(raw_input('height:'))
    genLim = int(raw_input('number of generations: '))
    speed = float(raw_input('speed: '))
    cells = [[randint(0,1) for i in xrange(n)] for k in xrange(m)]
    for i in xrange(0,genLim):
        next = [[0 for i in row] for row in cells]
        printfriend = [[0 for i in row] for row in cells]
        for i in xrange(0,n):
            for k in xrange(0,m):
                if i == 0:
                    if k == 0:
                        next[i][k] = cells[i+1][k] + cells[i+1][k+1] + cells[i][k+1]
                    elif k == m-1:
                        next[i][k] = cells[i+1][k] + cells[i+1][k-1] + cells[i][k-1]
                    else:
                        next[i][k] = cells[i+1][k] + cells[i+1][k-1] + cells[i][k-1] + cells[i][k+1] + cells[i+1][k+1]
                elif i == n-1:
                    if k == 0:
                        next[i][k] = cells[i-1][k] + cells[i-1][k+1] + cells[i][k+1]
                    elif k == m-1:
                        next[i][k] = cells[i-1][k] + cells[i-1][k-1] + cells[i][k-1]
                    else:
                        next[i][k] = cells[i-1][k] + cells[i-1][k-1] + cells[i][k-1] + cells[i][k+1] + cells[i-1][k+1]
                elif k == 0:
                    next[i][k] = cells[i-1][k] + cells[i+1][k] + cells[i-1][k+1] + cells[i][k+1] + cells[i-1][k+1]
                elif k == m-1:
                    next[i][k] = cells[i-1][k] + cells[i+1][k] + cells[i-1][k-1] + cells[i][k-1] + cells[i-1][k-1]
                else:
                    next[i][k] = cells[i-1][k] + cells[i-1][k-1] + cells[i][k-1] + cells[i][k+1] + cells[i-1][k+1] + cells[i+1][k] + cells[i+1][k-1] + cells[i+1][k+1]
        for i in xrange(n):
            for k in xrange(m):
                if cells[i][k] == 0:
                    if next[i][k] == 3:
                        next[i][k] = 1
                    else: next[i][k] = 0
                elif cells[i][k] == 1:
                    if next[i][k] < 2:
                        next[i][k] = 0
                    elif next[i][k] == 2 or next[i][k] == 3:
                        next[i][k] = 1
                    elif next[i][k] > 3:
                        next[i][k] = 0
        cells = next
        for i in xrange(n):
            for k in xrange(m):
                if next[i][k] == 1: printfriend[i][k] = '#'
                else: printfriend[i][k] = ' '

        os.system('cls' if os.name == 'nt' else 'clear')
        print "\n\n\n"
        for i in printfriend: print '  '.join(i), "\n"
        time.sleep(1/speed)
    return 0

next_gen()
