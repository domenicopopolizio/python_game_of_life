import os
import time
from typing import List

width:int = 0
height:int = 0
counter:int = 0

buffer:bool = True

buff1: List[List[str]] = []
buff2: List[List[str]] = []


def parseFile(file):
    global width, height, buff1, buff2
    f = open(file, "r")
    lines:List[str] = f.read().splitlines()
    height = len(lines)
    if(height <= 0):
        return
    width = len(lines[0])

    for line in range(0, len(lines)):
        buff1.append([])
        buff2.append([])
        for c in range(0, len(lines[line])):
            buff1[line].append(lines[line][c])
            buff2[line].append('.') 
    f.close()

def leggi(r:int, c:int) -> str:
    global buff1, buff2, buffer
    if buffer:
        return buff1[r][c]
    else:
        return buff2[r][c]

def scrivi(r:int, c:int, val:str) -> None:
    global buff1, buff2, buffer
    if buffer:
        buff2[r][c] = val
    else:
        buff1[r][c] = val


def neighbors_number(r: int, c: int) -> int:
    counter: int = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            
            #if(abs(i) != abs(j)):
            if(i == 0 and j == 0):
                continue
            if c+i >= 0 and c+i <= width-1 and r+j >= 0 and r+j <= height-1:
                if(leggi(r+j, c+i) is '#'):
                    counter += 1
    return counter
            

def run() -> None:
    global buffer, counter, width, height

    while True:
        os.system("clear")
        
        for r in range(0, height):
            for c in range(0, width):
                print(('■' if leggi(r, c) == '#' else ' ' )+' ', end='')
            print()

        for r in range(0, height):
            for c in range(0, width):
                
                nn:int = neighbors_number(r, c)

                if leggi(r, c) == '.':
                    if nn == 3:
                        scrivi(r, c, '#')
                    else:
                        scrivi(r, c, '.')
                else:
                    if nn < 2:
                        scrivi(r, c, '.')
                    elif nn == 2 or nn == 3:
                        scrivi(r, c, '#')   
                    elif nn > 3:
                        scrivi(r, c, '.')  
                        


        buffer = not buffer
        counter += 1
        time.sleep(1/60)

def main():
    parseFile("input.txt")
    run()

    
if __name__ == '__main__':
    main()