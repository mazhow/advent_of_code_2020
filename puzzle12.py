with open("puzzle12_input.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

#data = ['F10',
#'N3',
#'F7',
#'R90',
#'F11']

face = "E"
e=0
w=0 
n=0
s=0

for ins in data:
    e += (int(ins[1:]) if ins[0] == "E" or (face == "E" and ins[0] == "F") else 0)
    w += (int(ins[1:]) if ins[0] == "W" or (face == "W" and ins[0] == "F") else 0)
    n += (int(ins[1:]) if ins[0] == "N" or (face=="N" and ins[0] == "F") else 0)
    s += (int(ins[1:]) if ins[0] == "S" or (face=="S" and ins[0] == "F") else 0)
    if ins[0] in ("R","L"):
        if ins in ("R180","L180"):
            face = ("S" if face == "N" else "W" if face == "E" else "N" if face == "S" else "E" if face == "W" else "0")
        elif ins in("R90","L270"):
            face = ("S" if face == "E" else "W" if face == "S" else "N" if face == "W" else "E" if face == "N" else face)
        elif ins in ("L90","R270"):
            face = ("S" if face == "W" else "W" if face == "N" else "N" if face == "E" else "E" if face == "S" else face)
    
print("{'S': " + str(s) + " , 'E': " + str(e) + " , 'W': " + str(w) + " , 'N': " + str(n) + "}")
print("TASK 1 SOLUTION: " + str(abs((e-w) + (n-s))))
