with open("puzzle6_input.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]


#print(data)
yes_set = set()
person_answers = {}
group_answers = []
all_yes = []
people = 0
for line in data:
    if line != '':
        people +=1
 #       print(line)
        for char in line:
            yes_set.add(char)
            if char not in person_answers:
                person_answers[char] = 1
            else:
                person_answers[char] +=1
        #        print(person_answers)
        #print(yes_set)
    else:
        # at end of group, count answers
 #       print('end of group')
        group_count = len(yes_set)
        group_answers.append(group_count)
 #       print ("No. of yes answers in group: " + str(group_count))
        print("People in group:" + str(people))
        print(person_answers)
        all_yes.append(sum(1 for i in person_answers.values() if i == people))
        yes_set = set()
        person_answers={}
        people = 0

# don't forget the last group
print("People in group:" + str(people))
all_yes.append(sum(1 for i in person_answers.values() if i == people))
group_count = len(yes_set)
group_answers.append(group_count)

print("Sum of all answers for groups = " + str(sum(group_answers)))
print("Sum of questions to which everyone answered yes = " + str(sum(all_yes)))
