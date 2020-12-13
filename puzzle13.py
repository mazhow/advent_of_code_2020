with open("puzzle13_input.txt") as f:
    data = f.readlines()

start = int(data[0])
bus_ids = [int(x) for x in data[1].split(",") if x.isdigit()]

print("start:" + str(start))
print(bus_ids)

def closest_time(start, bus):
    time1 = start - (start % bus)
    # closest number > start time divisible by bus schedule
    time2 = (start + bus) - (start % bus)
    if time1 == start:
        return time1
    else:
        return time2

bus_options = {}                    

for bus_id in bus_ids:
    bus_options[bus_id] = closest_time(start, int(bus_id))

bus_to_take = (min(bus_options, key=bus_options.get))
print("Get on bus: " + str(bus_to_take))
next_time = bus_options[bus_to_take]
print("which will arrive at: " + str(next_time))
min_wait = int(next_time) - start
print("You'll be waiting: " + str(min_wait) + " minutes")

print("PART 1 SOLUTION: " + str(int(bus_to_take) * min_wait))