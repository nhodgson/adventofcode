def walk_rule_dict(rule_dict, current_k):
    if 'shiny gold' in rule_dict[current_k].keys():
        return 1
    elif 'other' in rule_dict[current_k].keys():
        return 0
    else:
        counts = 0
        for k in rule_dict[current_k].keys():
            counts += walk_rule_dict(rule_dict, k)

        return counts > 0

def count_bags(rule_dict, current_k):

    if 'other' in rule_dict[current_k].keys():
        return 0

    cnts = []
    for k in rule_dict[current_k]:
        for _ in range(rule_dict[current_k][k]):
            cnts.append(count_bags(rule_dict, k))

    return sum(cnts) + len(cnts)

def get_bag_rule_dict(lines):
    bag_rule_dict = {}
    for l in slines:
        bag = l[0].strip()
        contents = l[1].strip()[:-1].split(',')
        contents =  [x.strip().split(' ', 1) for x in contents]
        allowed_bags = {}
        for c in contents:
            b = c[1]
            # this is horrible
            if 'bags' in b:
                b = b.replace(' bags','')
            if 'bag' in b:
                b = b.replace(' bag','')

            try:
                allowed_bags[b] = int(c[0]) 
            except:
                allowed_bags[b] = c[0]

        bag_rule_dict[bag] = allowed_bags
    
    return bag_rule_dict

def part1(bag_rule_dict):
    count = 0 
    for k in bag_rule_dict:
        count += walk_rule_dict(bag_rule_dict, k)

    print('Bags that can carry shiny gold: {}'.format(count))

def part2(bag_rule_dict):
    pass

with open('advent_day7_test.txt') as fid: 
    lines = fid.readlines()

slines = [x.strip().split('bags contain') for x in lines]

bag_rule_dict = get_bag_rule_dict(slines)

part1(bag_rule_dict)

print(f"Shiny gold bag holds: {count_bags(bag_rule_dict, 'shiny gold')} bags")