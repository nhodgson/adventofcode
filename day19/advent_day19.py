import re 

def split_rule(r):
    rules = r.split('|')
    out = []
    for r in rules:
        out.append(tuple([int(i) for i in r.split()]))
    return tuple(out)

def get_input(fname):
    with open(fname) as fid:
        lines = fid.readlines()

    rules = {}
    msgs = []
    for line in lines:
        line = line.strip()
        if ':' in line:
            n, r = line.split(':')
            n = int(n)
            if '|' in r:
                rules[n] = split_rule(r)
            elif re.findall(r'"(.*)"', r) != []:
                a = re.findall(r'"(.*)"', r)
                if len(a) > 1:
                    raise ValueError(f'unexpected rule at {n}')
                rules[n] = a[0]
            else:
                rules[n] = tuple([int(x) for x in r.split()]),
        elif line.startswith(('a','b')):
            msgs.append(line)
        else:
            pass
    return rules, msgs

def match_rule_zero(msg, curr_rules):
    if len(curr_rules) > len(msg):
        return False
    elif len(curr_rules) == 0 or len(msg) == 0:
        # success if there are no more rules and we
        # have worked our way through the entire message
        return len(curr_rules) == 0 and len(msg) == 0

    c = curr_rules.pop()
    if isinstance(c, str):
        # we have a match
        if msg[0] == c:
            # start again, matching the next item in the messages
            return match_rule_zero(msg[1:], curr_rules.copy())
    else:
        for rule in rules[c]:
            if match_rule_zero(msg, curr_rules + list(reversed(rule))):
                return True
    return False

def count_valid_messages(rules, messages):
    total = 0
    for message in messages:
        if match_rule_zero(message, list(reversed(rules[0][0]))):
            total += 1
    return total


rules, msgs = get_input('advent_day19.txt')

valid_messages = count_valid_messages(rules, msgs)

print(f"Part 1: {valid_messages}")

rules[8] = ((42,), (42, 8))
rules[11] = ((42, 31), (42, 11, 31))

valid_messages = count_valid_messages(rules, msgs)
print(f"Part 2: {valid_messages}")
