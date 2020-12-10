with open("puzzle7_input.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

rules = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
'bright white bags contain 1 shiny gold bag.',
'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
'faded blue bags contain no other bags.',
'dotted black bags contain no other bags.']

rule_dict = {}
#contents = []

def get_num_bags(colour):
    pass
get_num_bags("shiny gold")       

for rule in rules:
    split_rule = rule.split()
    key = split_rule[0]+' '+split_rule[1]
    count=0
    rule_content = {}
    for i in split_rule:
        count +=1
        if i.isdigit():
#            print(i)
            content_key = split_rule[count] + ' ' + split_rule[count+1]
#            print("content key " + content_key)
            rule_content[content_key]=i
 #           print(rule_content)
    rule_dict[key] = rule_content
print(rule_dict)

def get_bags(bag):
    for key, value in rule_dict.items():
        if bag in rule_dict.items():
            print(key)
            print(value.keys())
            print(value.values())

bag = "shiny gold"
#print(get_bags(bag))
for key, value in rule_dict.items():
    print(key)
    print("rule keys: " + str(rule_dict[key]))
    if bag in rule_dict[key]: 
        print ("found bag")
        print(rule_dict[key].get(bag))
    else:
        # Look inside the bags to see if they can contain
        print("Look inside " + str(rule_dict[key].keys()))
        for x in rule_dict[key].keys():
            print(x)
    