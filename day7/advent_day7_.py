with open("advent_day7.txt", "r") as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

# to make a dictionary of bags
bag_types = []
all_bags = {}
for line in lines:
    mbag = " ".join(line.split(" ")[:2])
    contains = line[line.index("contain ")+8:-1]
    each_contain = contains.split(",")
    each_contain = [cnt.lstrip() for cnt in each_contain]
    each_contain = [" ".join(cont.split(" ")[:-1]) for cont in each_contain]
    #print(each_contain)
    each_contain = {" ".join(cont.split(" ")[1:]):cont.split(" ")[0] for cont in each_contain}
    #print(each_contain)
    if mbag not in bag_types:
        bag_types.append(mbag)
    if all_bags.get(mbag):
        each_contain.update(all_bags[mbag]) 
    all_bags[mbag] = each_contain

def check_bag(bags, my_bag, current_bag):
    if current_bag==my_bag:
        return 1
    if bags.get(current_bag) is None:
        return 0
    else:
        counts = []
        for k, v in bags[current_bag].items():
            counts.append(check_bag(bags, my_bag, k))
        return max(counts)

found_bags = 0
my_bag = "shiny gold"
for k, v in all_bags.items():
    if k != my_bag:
        found_bags+=check_bag(all_bags, my_bag, k)
print(f"{found_bags} bags can contain {my_bag} bag.")
