import sys
from collections import defaultdict
import re
## Credit to jonathanpaulsson, I didnt't have the time, knowledge or brains to pull this off  :)
## Still need to figure out why it skips the first row with the test input

data = open("2023/4/input.txt").read().strip()

answer = 0
lines = data.split("\n")

win = set()
scratch = set()
nums = set()
NewC = defaultdict(int)
for i, line in enumerate(lines):
    NewC[i] += 1
    ws = line.split(":")[1]
    w,s = ws.split("|")
    win = set(w.strip().split())
    scratch = set(s.strip().split())
    nums= win.intersection(scratch)
    wins = len(win.intersection(scratch))
    if wins > 0:
        answer += 2**(wins-1)
    for j in range(wins):
        NewC[i+1+j] += NewC[i]

# Part 2 solution from Jonathan Paulsson. Brilliant!
print(answer)
print(sum(NewC.values()))