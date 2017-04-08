import csv

##Weapons: Name, Rank, Mt, Hit, Crit, Avoid, Rng, Value, Desc
##Healing: Name, Rank, Hit, Range, Uses, Worth, Exp, Desc
##Consumable: Name, Uses, Worth, Description
class Item:
    def __init__(self, name, value, desc):
        self.name = name
        self.value = value
        self.desc = desc
        pass

    def get_name(self):
        return str(self.name)

    pass


class Weapon(Item):
    def __init__(self, name, value, desc, rank, mt, hit, crit, avo, rng):
        Item.__init__(self, name, value, desc)
        self.rank = rank
        self.mt = mt
        self.hit = hit
        self.crit = crit
        self.avo = avo
        self.rng = rng
        pass

    def print_item(self):
        print(self.name, self.value, self.desc, self.rank, self.mt, self.hit, self.crit, self.avo, self.rng)
        pass
    ##pass


class Consumable(Item):
    def __init__(self, name, uses, value, desc):
        Item.__init__(self, name, value, desc)
        self.uses = uses
    pass

    def print_item(self):
        print(self.name, self.uses, self.value, self.desc)


class Support(Item):
    def __init__(self, name, rank, dmg, rng, uses, value, exp, desc):
        Item.__init__(self, name, value, desc)
        self.rank = rank
        self.dmg = dmg
        self.rng = rng
        self.uses = uses
        self.exp = exp

    def print_item(self):
        print(self.name, self.rank, self.dmg, self.rng, self.uses, self.exp, self.value, self.desc)


class Unit:

    def __init__(self, data):
        self.data = []
        self.supports = []
        self.data = data

    def print_unit(self):
        print(
        "Name:", self.data[0], "Str:", self.data[1], "Mag:", self.data[2], "Skl", self.data[3], "Spd", self.data[4],
        "Lck", self.data[5], "Def", self.data[6], "Res", self.data[7])

    def get_name(self):
        return str(self.data[0])

    def set_name(self, name):
        self.data[0] = name

    def get_stats(self):
        return self.data

    def set_stats(self, data):
        self.data = list(data)

    def get_supports(self):
        return self.supports

    def set_supports(self, supports):
        self.supports = supports

    def get_pairing_score(self, other):
        out = [0, 0, 0, 0, 0, 0, 0]
        input = other.get_stats()
        for i in self.data:
            out[i] = self.data[i] + 1
            out[i] = out[i] + input[i] + 1

        for i in out:
            avg = 0
            avg = avg + out[i]
            avg = avg / len(out)

        return avg


class Child(Unit):

    def __init__(self, data, parent):
        Unit.__init__(self, data)
        self.secondary = ""
        self.parent = parent

    def get_parent(self):
        return self.parent

    def set_secondary(self, secondary):
        self.secondary = secondary

    def get_secondary(self):
        base=""

        return self.secondary


# Nohr Prince(ss),40 23 17 19  21 22 21 19,Sword B Dragonstone B

class UnitClass:
    def __init__(self, name, stats, weapons):
        self.weapons = {}
        self.name = name
        self.stats = stats.split()
        temp = weapons.split()
        for i in range(0, len(temp) - 1, 2):
            k = temp[i]
            v = temp[i + 1]
            self.weapons.update({k: v})
            pass

    def get_name(self):
        return self.name

    def print_class(self):
        print(self.name, self.stats, self.weapons)

    pass

'''
class AdvancedClass:
    def __init__(self, name, stats, weapons):
        self.weapons = {}
        self.name=name
        self.stats=stats.split()
        temp = weapons.split()
        for i in range(0,len(temp)-1,2):
            k = temp[i]
            v = temp[i+1]
            self.weapons.update({k:v})
            pass

    def get_name(self):
        return self.name

    def print_class(self):
        print(self.name, self.stats, self.weapons)

    pass

class BaseClass(AdvancedClass):
    def __init__(self, n, s, w):
        AdvancedClass.__init__(self,n, s, w)
        self.base = []

    def print_class(self):
        print(self.name, self.stats, self.weapons, self.base)

    def set_base(self,base):
        self.base=base

    pass
'''
Fathers = []
Mothers = []
Children = []

Items = []
Classes = []
ClassSets={}
UnitClasses={}

with open('classes.csv','r') as classes:
    creader=csv.reader(classes, delimiter=',', quotechar="|")
    for row in creader:
        temp = UnitClass(row[0],row[1],row[2])
        Classes.append(temp)
        ##temp.print_class()

'''
with open('baseclass.csv','r') as baseclass:
    creader=csv.reader(baseclass, delimiter=',', quotechar="|")
    for row in creader:
        temp = BaseClass(row[0],row[1],row[2])
        Classes.append(temp)
        ##temp.print_class()

with open('advancedclass.csv','r') as advclass:
    creader=csv.reader(advclass, delimiter=',', quotechar="|")
    for row in creader:
        temp = AdvancedClass(row[0],row[1],row[2])
        Classes.append(temp)
        ##temp.print_class()
'''

with open('classets.csv','r') as classsets:
    creader=csv.reader(classsets, delimiter=',', quotechar="|")
    for row in creader:
        k=row[0]
        v=row[1]
        ClassSets.update({k:v})

with open('unitclasses.csv','r') as unitsets:
    creader=csv.reader(unitsets, delimiter=',', quotechar="|")
    for row in creader:
        ##print(row)
        k=row[0]
        v=row[1]
        UnitClasses.update({k:v})

with open('mothers.csv', 'r') as mothers:
    mreader = csv.reader(mothers, delimiter=',', quotechar="|")
    for row in mreader:
        temp = Unit((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        Mothers.append(temp)

with open('fathers.csv', 'r') as fathers:
    freader = csv.reader(fathers, delimiter=',', quotechar="|")
    for row in freader:
        temp = Unit((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        Fathers.append(temp)

with open('children.csv', 'r') as children:
    creader = csv.reader(children, delimiter=',', quotechar="|")
    for row in creader:
        temp = Child((row[0], 0, 0, 0, 0, 0, 0, 0), row[1])
        namebak = temp.get_name()
        if row[1] == "Azura":
            for i in Mothers:
                if i.get_name() == temp.get_parent():
                    temp.set_stats(i.get_stats())
                    temp.set_name(namebak)
        else:
            for i in Fathers:
                if i.get_name() == temp.get_parent():
                    temp.set_stats(i.get_stats())
                    temp.set_name(namebak)

        Children.append(temp)

with open('supports.csv', 'r') as supports:
    sreader = csv.reader(supports, delimiter=',', quotechar="|")
    for row in sreader:

        for i in Mothers:
            n1 = str(row[0])
            n2 = str(i.get_name())
            if n1 == n2:
                r = row[1].split()
                i.set_supports(r)

        for i in Fathers:
            n1 = str(row[0])
            n2 = str(i.get_name())
            if n1 == n2:
                r = row[1].split()
                i.set_supports(r)

        for i in Children:
            n1 = str(row[0])
            n2 = str(i.get_name())
            if n1 == n2:
                r = row[1].split()
                i.set_supports(r)

# 0,   7,    8,   1,  2, 3, 4,   5,  6
# c def __init__(self,name,value,desc,rank,mt,hit,crit,avo,rng):
with open('weapons.csv', 'r') as weapons:
    wreader = csv.reader(weapons, delimiter=',', quotechar="|")
    for row in wreader:
        ##print(row[0],row[1],row[2],row[3],row[7],row[8])
        temp = Weapon(row[0], row[7], row[8], row[1], row[2], row[3], row[4], row[5], row[6])
        ##temp.print_item()
        Items.append(temp)
        pass

with open('consumables.csv', 'r') as consumables:
    creader = csv.reader(consumables, delimiter=",", quotechar="|")
    for row in creader:
        temp = Consumable(row[0], row[1], row[2], row[3])
        ##temp.print_item()
        Items.append(temp)
        pass

with open('support.csv', 'r') as supports:
    sreader = csv.reader(supports, delimiter=",", quotechar="|")
    for row in sreader:
        temp = Support(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        ##temp.print_item()
        Items.append(temp)
        pass


def addCorrin(bane, boon, sex):
    ## Str,Mag,Skl,Spd,Lck,Def,Res
    data = ["Corrin", 0, 0, 0, 0, 0, 0, 0]

    if (bane == "HP"):
        data[1] = data[1] - 1
        data[2] = data[2] - 1
        data[5] = data[5] - 1
        data[6] = data[6] - 1
        data[7] = data[7] - 1
    elif (bane == "Str"):
        data[1] = data[1] - 3
        data[3] = data[3] - 1
        data[6] = data[6] - 1
    elif (bane == "Mag"):
        data[2] = data[2] - 3
        data[4] = data[4] - 1
        data[7] = data[7] - 1
    elif (bane == "Skl"):
        data[1] = data[1] - 1
        data[3] = data[3] - 3
        data[6] = data[6] - 1
    elif (bane == "Spd"):
        data[4] = data[4] - 3
        data[3] = data[3] - 1
        data[6] = data[6] - 1
    elif (bane == "Lck"):
        data[1] = data[1] - 1
        data[2] = data[2] - 1
        data[5] = data[5] - 3
    elif (bane == "Def"):
        data[5] = data[5] - 1
        data[6] = data[6] - 3
        data[7] = data[7] - 1
    elif (bane == "Res"):
        data[2] = data[2] - 1
        data[4] = data[4] - 1
        data[7] = data[7] - 3
    else:
        print("Invalid Boon. Please follow the format: HP, Str, Mag, Skl, Spd, Lck, Def, Res.")
        return False

    if (boon == "HP"):
        data[1] = data[1] + 1
        data[2] = data[2] + 1
        data[5] = data[5] + 2
        data[6] = data[6] + 2
        data[7] = data[7] + 2
    elif (boon == "Str"):
        data[1] = data[1] + 4
        data[3] = data[3] + 2
        data[6] = data[6] + 2
    elif (boon == "Mag"):
        data[2] = data[2] + 4
        data[4] = data[4] + 2
        data[7] = data[7] + 2
    elif (boon == "Skl"):
        data[1] = data[1] + 2
        data[3] = data[3] + 4
        data[6] = data[6] + 2
    elif (boon == "Spd"):
        data[4] = data[4] + 4
        data[3] = data[3] + 2
        data[6] = data[6] + 2
    elif (boon == "Lck"):
        data[1] = data[1] + 2
        data[2] = data[2] + 2
        data[5] = data[5] + 4
    elif (boon == "Def"):
        data[5] = data[5] + 2
        data[6] = data[6] + 4
        data[7] = data[7] + 2
    elif (boon == "Res"):
        data[2] = data[2] + 2
        data[4] = data[4] + 2
        data[7] = data[7] + 4
    else:
        print("Invalid Boon. Please follow the format: HP, Str, Mag, Skl, Spd, Lck, Def, Res.")
        return False

    temp = Unit(data)
    ##temp.print_unit()

    if (sex == "M"):
        Fathers.append(temp)
    elif (sex == "F"):
        Mothers.append(temp)

        for i in Children:
            if i.get_parent() == temp.get_name():
                i.set_stats(temp.get_stats())
                i.set_name("Kana")

    return True


def pair_units(Father, Mother):
    pass


def test_pair(Father, Mother):
    F = str(Father)
    M = str(Mother)

    f = []
    m = []
    o = []

    for i in Fathers:
        tempname = str(i.get_name())
        if tempname == F:
            f = i.get_stats();

    for i in Mothers:
        tempname = i.get_name()
        if tempname == M:
            m = i.get_stats();

    for i in range(0, len(f) - 1, 2):
        o.append(int(f[i + 1]) + int(m[i + 1]) + 1)
        pass
    ##print(o)
    return o
    pass

def get_info(search):
    found=0
    for i in Mothers:
        if (search in (i.get_name())):
            i.print_unit()
            found = 1
        pass
    for i in Fathers:
        if (search in (i.get_name())):
            i.print_unit()
            found = 1
        pass
    for i in Children:
        if (search in (i.get_name())):
            i.print_unit()
            found = 1
        pass
    for i in Classes:
        if (search in (i.get_name())):
            i.print_class()
            found = 1
        pass
    for i in Items:
        if (search in (i.get_name())):
            i.print_item()
            found = 1
        pass
    if found == 0:
        print("Search target not found. Was it misspelt?")


## Debugging Code

containsCorrin = addCorrin("Lck", "Spd", "M")

## Program Loop

isRunning=True

while isRunning==True:
    cmd=raw_input("> ")
    if cmd=="Exit":
        isRunning=False
        pass
    if "!dt" in cmd:
        concat=""
        input=cmd.split()
        for i in range(1,len(input),1):
            if(i > 1):
                concat = concat + " "
            concat = concat + input[i]
        get_info(concat)


