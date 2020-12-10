with open("puzzle7_input.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]


def get_num_bags(colour):
    lines = [ line for line in data if colour in line and line.index(colour) != 0]
    all_colours = []

    print(lines)

    if len(lines) == 0:
        return[]

    colours = [line[:line.index(' bags')] for line in lines]
    colours = [ colour for colour in colours if colour not in all_colours]
    print(colours)

    for colour in colours:
        all_colours.append(colour)
        bags = get_num_bags(colour)

        all_colours += bags
        print(all_colours)

     # do stuff about unique colours
    unique_colours = set()
    for colour in all_colours:
        unique_colours.add(colour)  
       
    return(unique_colours)

colours = get_num_bags("shiny gold")
print(len(colours))

# part 2


def get_bag_count(colour):
    rule = ""
    for line in data:
        if line[:line.index(' bags')] == colour:
            rule = line

    if "no" in rule:
        return 1

    rule = rule[rule.index('contain')+8:].split()
    
    i = 0
    total = 0
    while i < len(rule):
        count = rule[i]
        colour = rule[i+1] + " " + rule[i+2]
        
        total += int(count) * int(get_bag_count(colour)) 
        
        i +=4
    
    return total + 1


count = get_bag_count("shiny gold")
print(count -1)
