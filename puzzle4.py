
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
good_passports=[]

def validate(passport):
    for field in fields:
        if field not in passport:
            return False
    return True

valid=0
passport=""
with open("puzzle4_input.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

for line in data:
    if line != '':
        passport += " " + line
    else:
        if validate(passport):
            good_passports.append(passport)
            valid +=1
        passport=''

if validate(passport):
    valid +=1
    good_passports.append(passport)
    
print("No. of passports with minimum attributes: " + str(valid))

# part 2
def valid_byr(byr):
    byr  = int(byr)
    if byr < 1920 or byr > 2002:
        return False
    return True

def valid_iyr(iyr):
    iyr  = int(iyr)
    if iyr < 2010 or iyr > 2020:
        return False
    return True
    
def valid_eyr(eyr):
    eyr = int(eyr)
    if eyr < 2020 or eyr > 2030:
        return False
    return True

def valid_hgt(hgt):
    units = hgt[-2:]
    if units not in ["in","cm"]:
        return False
    if units == "":
        return False
    if units == "cm":
        if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
            return False
    if units == "in":
        if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
            return False
    return True

def valid_hcl(hcl):
    if hcl[0] != "#":
        return False
    if len(hcl) != 7:
        return False 
    return True

def valid_ecl(ecl):
    if ecl not in ["amb","blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    return True

def valid_pid(pid):
    if len(pid) != 9:
        return False 
    return True

def validateFields(passport):
    passport = passport.split()
    d={}
    for field in passport:
        key = field[:3]
        val = field[4:]
        d[key] = val

    if not valid_byr(d['byr']) or not valid_iyr(d['iyr']) or not valid_eyr(d['eyr']) or not valid_hgt(d['hgt']) or not valid_hcl(d['hcl']) or not valid_ecl(d['ecl']) or not valid_pid(d['pid']):
        return False
    return True

valid_good = 0
for passport in good_passports:
    if validateFields(passport):
        valid_good +=1
    
print ("No. of fully validated passports: " + str(valid_good))
