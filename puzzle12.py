import math
with open("puzzle12_input.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

#data = ['F10',
#'N3',
#'F7',
#'R90',
#'F11']
def rotate(origin, point, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))

sh = {"x": 0, "y": 0}
wp = {"x": 10, "y": 1}

for ins in data:
    # N, E, S, W move waypoint only
    if ins[0] in ("N","E","W","S"):
        wp["x"] += (int(ins[1:]) if ins[0] == "N" else 0)
        wp["x"] -= (int(ins[1:]) if ins[0] == "S" else 0)
        wp["y"] += (int(ins[1:]) if ins[0] == "E" else 0)
        wp["y"] -= (int(ins[1:]) if ins[0] == "W" else 0)
 
    # F moves ship
    if ins[0] == "F":
        sh["x"] += wp["x"] * int(ins[1:])
        sh["y"] += wp["y"] * int(ins[1:])

    # L/R rotate waypoint:
    if ins[0] in ("R","L"):
        if ins[0] == "R":
            n = -int(ins[1:])
        else:
            n = int(ins[1:])
        wp["x"], wp["y"] = rotate((0,0), (wp["x"],wp["y"]), math.radians(n))

print(wp)
print(sh)
print("TASK 2 SOLUTION: " + str(abs(sh["x"] + abs(sh["y"]))))
# 19276 too low, should be 42908