import csv

##Weapons: Name, Rank, Mt, Hit, Crit, Avoid, Rng, Value, Desc
##Healing: Name, Rank, Hit, Range, Uses, Worth, Exp, Desc
##Consumable: Name, Uses, Worth, Description

# item: name, value, desc
class Item:
    name=""
    value=0
    desc=""

    def __init__(self,name,value,desc):
        self.name=name
        self.value=value
        self.desc=desc
        pass
    pass

# weapon: rank, mt, hit, crit, avo, rng
# parent: item
class Weapon(Item):
    
    rank="" # Rank
    mt=0 # Might (Damage)
    hit=0 # Hit %
    crit=0 # Crit %
    avo=0 # Avoidance %
    rng="" # Range

    def __init__(self,name,value,desc,rank,mt,hit,crit,avo,rng):

        # Set properties to provided
        self.rank=rank
        self.mt=mt
        self.hit=hit
        self.crit=crit
        self.avo=avo
        self.rng=rng

# consumable: (nil)
# parent: item
class Consumable(Item):

    # not implemented
    pass

# support: (nil)
# parent: item
class Support(Item):


    def __init__(self,data,parent):
        Unit.__init__(self,data)
        self.parent=parent

# unit: data, supports
class Unit:

    # Data Indexes:
    # 0: Name
    # 1: Str
    # 2: Mag
    # 3: Skl
    # 4: Spd 
    # 5: Lck
    # 6: Res

    data=[] # Data Array
    supports=[] # Supports Array

    # __init__(data: list): void
    def __init__(self,data):
        self.data=data

    # print_unit(void): void
    def print_unit(self):
        print("Name:",self.data[0],"Str:",self.data[1],"Mag:",self.data[2],"Skl",self.data[3],"Spd",self.data[4],"Lck",self.data[5],"Def",self.data[6],"Res",self.data[7])

    # get_name(void): string
    def get_name(self):
        return str(self.data[0])

    # set_name(string): void
    def set_name(self,name):
        self.data[0]=name

    def get_stats(self):
        return self.data

    def set_stats(self,data):
        self.data=list(data)

    def get_supports(self):
        return self.supports

    def set_supports(self,supports):
        self.supports=supports

    def get_pairing_score(self,other):
        out = [0,0,0,0,0,0,0]
        input = other.get_stats()
        for i in self.data:
            out[i]=self.data[i]+1
            out[i]=out[i]+input[i]+1

        for i in out:
            avg=0
            avg=avg+out[i]
            avg=avg/len(out)

        return avg
class Child(Unit):
    parent = ""
    secondary = ""

    def __init__(self,data,parent):
        Unit.__init__(self,data)
        self.parent=parent

    def get_parent(self):
        return self.parent

    def set_secondary(self,secondary):
        self.secondary=secondary

    def get_secondary(self):
        return self.secondary

Fathers=[]
Mothers=[]
Children=[]

with open('data/mothers.csv','r') as mothers:
    mreader=csv.reader(mothers,delimiter=',',quotechar="|")
    for row in mreader:
        temp = Unit((row[0],row[1], row[2], row[3], row[4], row[5], row[6],row[7]))
        Mothers.append(temp)

with open('data/fathers.csv','r') as fathers:
    freader=csv.reader(fathers,delimiter=',',quotechar="|")
    for row in freader:
        temp = Unit((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        Fathers.append(temp)

with open('data/children.csv','r') as children:
    creader=csv.reader(children,delimiter=',',quotechar="|")
    for row in creader:
        temp = Child((row[0],0,0,0,0,0,0,0),row[1])
        namebak=temp.get_name()
        if row[1]=="Azura":
            for i in Mothers:
                if i.get_name()==temp.get_parent():
                    temp.set_stats(i.get_stats())
                    temp.set_name(namebak)
        else:
            for i in Fathers:
                if i.get_name()==temp.get_parent():
                    temp.set_stats(i.get_stats())
                    temp.set_name(namebak)

        Children.append(temp)

with open('data/supports.csv','r') as supports:

    sreader=csv.reader(supports,delimiter=',',quotechar="|")
    for row in sreader:

        for i in Mothers:
            n1=str(row[0])
            n2=str(i.get_name())
            if n1==n2:
                r = row[1].split()
                i.set_supports(r)

        for i in Fathers:
            n1 = str(row[0])
            n2 = str(i.get_name())
            if n1==n2:
                r = row[1].split()
                i.set_supports(r)

        for i in Children:
            n1 = str(row[0])
            n2 = str(i.get_name())
            if n1==n2:
                r = row[1].split()
                i.set_supports(r)


with open('data/weapons.csv','r') as weapons:
    wreader=csv.reader(weapons,delimiter=',',quotechar="|")
    for row in wreader:
        pass


def addCorrin(bane, boon, sex):
    ## Str,Mag,Skl,Spd,Lck,Def,Res
    data=["Corrin",0,0,0,0,0,0,0]

    if (bane=="HP"):
        data[1] = data[1] - 1
        data[2] = data[2] - 1
        data[5] = data[5] - 1
        data[6] = data[6] - 1
        data[7] = data[7] - 1
    elif(bane=="Str"):
        data[1] = data[1] - 3
        data[3] = data[3] - 1
        data[6] = data[6] - 1
    elif (bane=="Mag"):
        data[2] = data[2] - 3
        data[4] = data[4] - 1
        data[7] = data[7] - 1
    elif (bane=="Skl"):
        data[1]=data[1]-1
        data[3]=data[3]-3
        data[6]=data[6]-1
    elif (bane=="Spd"):
        data[4]=data[4]-3
        data[3]=data[3]-1
        data[6]=data[6]-1
    elif (bane=="Lck"):
        data[1]=data[1]-1
        data[2]=data[2]-1
        data[5]=data[5]-3
    elif (bane=="Def"):
        data[5]=data[5]-1
        data[6]=data[6]-3
        data[7]=data[7]-1
    elif (bane=="Res"):
        data[2]=data[2]-1
        data[4]=data[4]-1
        data[7]=data[7]-3
    else:
        print("Invalid Boon. Please follow the format: HP, Str, Mag, Skl, Spd, Lck, Def, Res.")
        return False

    if (boon=="HP"):
        data[1] = data[1] + 1
        data[2] = data[2] + 1
        data[5] = data[5] + 2
        data[6] = data[6] + 2
        data[7] = data[7] + 2
    elif(boon=="Str"):
        data[1] = data[1] + 4
        data[3] = data[3] + 2
        data[6] = data[6] + 2
    elif (boon=="Mag"):
        data[2] = data[2] + 4
        data[4] = data[4] + 2
        data[7] = data[7] + 2
    elif (boon=="Skl"):
        data[1]=data[1] + 2
        data[3]=data[3] + 4
        data[6]=data[6] + 2
    elif (boon=="Spd"):
        data[4]=data[4] + 4
        data[3]=data[3] + 2
        data[6]=data[6] + 2
    elif (boon=="Lck"):
        data[1]=data[1] + 2
        data[2]=data[2] + 2
        data[5]=data[5] + 4
    elif (boon=="Def"):
        data[5]=data[5] + 2
        data[6]=data[6] + 4
        data[7]=data[7] + 2
    elif (boon=="Res"):
        data[2]=data[2] + 2
        data[4]=data[4] + 2
        data[7]=data[7] + 4
    else:
        print("Invalid Boon. Please follow the format: HP, Str, Mag, Skl, Spd, Lck, Def, Res.")
        return False

    temp = Unit(data)
    temp.print_unit()

    if(sex == "M"):
        Fathers.append(temp)
    elif(sex=="F"):
        Mothers.append(temp)

        for i in Children:
            if i.get_parent() == temp.get_name():
                i.set_stats(temp.get_stats())
                i.set_name("Kana")

    return True
    pass

def pair_units(Father,Mother):
    pass

def test_pair(Father,Mother):

    F=str(Father)
    M=str(Mother)

    f=[]
    m=[]
    o=[]

    for i in Fathers:
        tempname=str(i.get_name())
        if tempname == F:
            f=i.get_stats();

    for i in Mothers:
        tempname=i.get_name()
        if tempname == M:
            m=i.get_stats();

    for i in range(len(f)-1) :
         o.append(int(f[i+1])+int(m[i+1])+1)
         pass
    ##print(o)
    return o
    pass

print()

## Debugging Code

containsCorrin=addCorrin("Lck","Spd","M")

for f in Fathers:
   oo=[]

   for m in Mothers:
        print(f.get_name(),",",m.get_name())
        print(f.get_supports())
        if ((m.get_name() in f.get_supports()) or (m.get_name=="Corrin") or (f.get_name=="Corrin")):
            print(m.get_name()," ",f.get_name())
        else:
            print("Not compatible.")
