import numpy as np

with open("puzzle5_input.txt") as f:
    data = f.readlines()


##print(passes)
passes= []
#data=['BBFFBFFRRR','FBBFFBBLRR','FFBFBFBRRR','FFFBFBFRRR','BBFFBBFLRR','FFFFBBFRRL','FFFFBBFLRL']
#data = ['FBFBBFFRLR','BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
#Start by considering the whole range, rows 0 through 127.
#F means to take the lower half, keeping rows 0 through 63.
#B means to take the upper half, keeping rows 32 through 63.
#F means to take the lower half, keeping rows 32 through 47.
#B means to take the upper half, keeping rows 40 through 47.
#B keeps rows 44 through 47.
##The final F keeps the lower of the two, row 44.
#F keeps rows 44 through 45.
#data = ['BFFFBBFRRR'] #: row 70, column 7, seat ID 567.
#data = ['FFFBBBFRRR']#: row 14, column 7, seat ID 119.
# data = ['BBFFBBFRLL']#: row 102, column 4, seat ID 820.
for line in data:
    front = 0
    back = 127
    #print(line.strip())
    for pos in line[:-3]:
 #       print(pos)
        if pos == 'F':
            back = back - ((back - front) / 2) -1
        else:
 #           print("working with front: " + str(front) + " and back: " + str(back))
            front = front + ((back - front) / 2) + 1
 #           print(front)
 #   print ("Finished with front: " + str(front) + " and back: " + str(back))
    row = min(front,back)
 #   print("row: " + str(row))
#

    right = 7
    left = 0
    for pos in line[7:]:
#        print("pos: " + pos)
#        print(line[7:])
        if pos == "L":
 #           print("working with seats " + str(left) + " to " + str(right))
            right = right - ((right - left) / 2) -1
        else:
            left = left + ((right - left) /2 ) + 1
 #           print("working with seats " + str(left) + " to " + str(right))
  #  print("Finished with column: " + str(right) + " or " + str(left))
    column = min(left,right)

    seat_id = (row* 8) + column
    #if seat_id in [50,54]:
#    print(line)
   # print("Seat is row: " + str(row) + ", column: " + str(column))
#    print(seat_id)
    if seat_id in passes:
        print("HANG ON, ALREADY THERE") 
        break
    passes.append(seat_id)

print("Highest seat ID: " + str(np.max(passes)))

passes.sort()
print(passes)
prev_seat = 7
for seat in passes:
    #print(seat)
    #    print("Seat: " + str(seat))
    if seat != prev_seat + 1:
        print("Missing Seat between: " + str(seat) +" and " + str(prev_seat))
    prev_seat = seat
