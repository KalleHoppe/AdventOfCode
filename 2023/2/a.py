import sys
from collections import defaultdict

data = open("2023/2/input.txt").read().strip()
ansA = 0
games = []
tr = 12
tg = 13
tb = 14
ansB = 0
for line in data.split("\n"):
    game = line.split(":")
    results = game[1].split(";")
    gn = int(game[0].split("Game")[1])

    gOk = True
    V = defaultdict(int)
    for res in results:
        # for balls in res.split(","):
        #     n,color = balls.split()
        #     if int(n) > {"red":12, "green":13, "blue":14}.get(color, 0):
        #         gOk = False
        sr = 0
        sb = 0
        sg = 0
        for r in res.strip().split(","):
            if r.find("red") >= 0:
                sr += int(r.strip().split(" ")[0])
                V["red"] = max(V["red"], int(r.strip().split(" ")[0]))
            if r.find("green") >= 0:
                sg += int(r.strip().split(" ")[0])
                V["green"] = max(V["green"], int(r.strip().split(" ")[0]))
            if r.find("blue") >= 0:
                sb += int(r.strip().split(" ")[0])
                V["blue"] = max(V["blue"], int(r.strip().split(" ")[0]))

        if (sr > tr or sg > tg or sb > tb):
            gOk = False
    #print(V)

    score = 1
    for v in V.values():
        score *= v
    ansB += score

    if gOk:
        ansA += gn

print(ansA)
print(ansB)