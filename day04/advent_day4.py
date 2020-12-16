
import re

def records_from_lines(lines):
    records = {}
    i = 0
    for line in lines:
        if line == '\n':
            i += 1
            continue
        
        try:
            records[i].append(line)
        except KeyError:
            records[i] = [line]

    for key, val in records.items():
        a = ''.join(val)
        a = a.strip().split()
        passport_data = [x.split(':') for x in a]
        records[key] =  {k:v for (k,v) in passport_data}

    return records

REQUIRED_KEYS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

#    Validation Rules
#    ================
#    byr (Birth Year) - four digits; at least 1920 and at most 2002.
#    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#    hgt (Height) - a number followed by either cm or in:
#        If cm, the number must be at least 150 and at most 193.
#        If in, the number must be at least 59 and at most 76.
#    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#    pid (Passport ID) - a nine-digit number, including leading zeroes.
#    cid (Country ID) - ignored, missing or not.

def check_year_range(val, min_val, max_val):
    if not len(val) == 4:
        return False
    else:
        val = int(val)
        return val >= min_val and val <= max_val

def check_range(val, min_val, max_val):
    return val >= min_val and val <= max_val

def check_hgt(hgt):

    hgt_unit = hgt[-2:]
    if hgt_unit not in ['in', 'cm']:
        print('invalid height: {}'.format(records[i]['hgt']))
        return False

    hgt = int(hgt[:-2])
    if hgt_unit == 'in':
        return check_range(hgt, 59, 76)

    elif hgt_unit == 'cm':
        return check_range(hgt, 150, 193)
    else:
        print('invalid height: {}'.format(records[i]['hgt']))
        return False

def validate_record(record):

    if REQUIRED_KEYS.issubset(record.keys()):

        if not check_year_range(record['byr'], 1920, 2002):
            return False
        
        if not check_year_range(record['iyr'], 2010, 2020):
            return False
        
        if not check_year_range(record['eyr'], 2020, 2030):
            return False

        if not check_hgt(record['hgt']):
            return False

        if not re.search('#[a-z0-9]', record['hcl']):
            return False 
        
        valid_ecls = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

        if not record['ecl'] in valid_ecls:
            return False
        
        pid = records[i]['pid']
        if not (len(pid) == 9 and pid.isnumeric()):
            return False

        return True

with open('advent_day4.txt') as fid:
    lines = fid.readlines()

records = records_from_lines(lines)

is_valid = 0

for i in records:
    if validate_record(records[i]):
        is_valid += 1



print('number of valid passports = {}'.format(is_valid))