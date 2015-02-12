import os
import time
from random import randint

def next_gen():
    m = int(raw_input('width:'))
    n = int(raw_input('height:'))
    genLim = int(raw_input('number of generations: '))
    speed = float(raw_input('speed: '))
    cells = [[randint(0,1) for i in xrange(m)] for k in xrange(n)]
    for i in xrange(0,genLim):
        next = [[0 for i in row] for row in cells]
        printfriend = [[0 for i in row] for row in cells]
        for i in xrange(0,n):
            for k in xrange(0,m):
                next[i][k] = cells[-1+(i%n)][k%m] + cells[-1+(i%n)][-1+(k%m)] + cells[i%n][-1+(k%m)] + cells[i%n][(k+1)%m] + cells[-1+(i%n)][(k+1)%m] + cells[(i+1)%n][k%m] + cells[(i+1)%n][-1+(k%m)] + cells[(i+1)%n][(k+1)%m]
        for i in xrange(n):
            for k in xrange(m):
                if cells[i][k] == 1:
                    if next[i][k] < 2:
                        next[i][k] = 0    # underpopularion
        for i in xrange(n):
            for k in xrange(m):
                if cells[i][k] == 1:
                    if next[i][k] == 2 or next[i][k] == 3:
                        next[i][k] = 1      # Stasis
        for i in xrange(n):
            for k in xrange(m):
                    if next[i][k] > 3:
                        next[i][k] = 0      # overpopulation
        for i in xrange(n):
            for k in xrange(m):
                if cells[i][k] == 0:
                    if next[i][k] == 3:
                        next[i][k] = 1
                    else: next[i][k] = 0    # reproduction
        cells = next
        for i in xrange(n):
            for k in xrange(m):
                if next[i][k] == 1: printfriend[i][k] = '#'
                else: printfriend[i][k] = ' '

        os.system('cls' if os.name == 'nt' else 'clear')
        print "\n\n\n"
        for i in printfriend: print ''.join(i)
        time.sleep(1/speed)
    return 0

next_gen()
