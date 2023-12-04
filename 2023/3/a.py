import sys
from collections import defaultdict
import re
## Credit to jonathanpaulsson, I didnt't have the time, knowledge or brains to pull this off  :)
## Still need to figure out why it skips the first row with the test input

data = open("2023/3/input.txt").read().strip()

answer = 0
lines = data.split("\n")
Grid = [[c for c in line] for line in lines]
RowLen = len(Grid)
ColLen = len(Grid[0])

nums = defaultdict(list)
for row in range(len(Grid)):
    gears = set()
    n = 0
    has_part = False
    for col in range(len(Grid[row])+1):
        if col < ColLen and Grid[row][col].isdigit():
            n = n*10+int(Grid[row][col])
            for rr in [-1,0,1]:
                for cc in [-1,0,1]:
                    if 0<=row+rr<RowLen and 0<= col+cc < ColLen:
                        ch = Grid[row+rr][col+cc]
                        if not ch.isdigit() and ch != ".":
                            has_part = True
                        if ch == "*":
                            gears.add((row+rr,col+cc))
        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
                #print(n)
            if has_part:
                answer += n
            n=0
            has_part= False
            gears = set()

gearsum = 0
for k,v in nums.items():
    if(len(v)==2):
        gearsum += v[0]*v[1]
        #print(v)
    # else:
    #     print(v)

print(answer)
print(gearsum)
