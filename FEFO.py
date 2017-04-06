import csv


class Unit:
    data=[]
    supports=[]

    def __init__(self,data):
        self.data=data

    def print_unit(self):
        print("Name:",self.data[0],"Str:",self.data[1],"Mag:",self.data[2],"Skl",self.data[3],"Spd",self.data[4],"Lck",self.data[5],"Def",self.data[6],"Res",self.data[7])

    def get_name(self):
        return str(self.data[0])

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

with open('mothers.csv','r') as mothers:
    mreader=csv.reader(mothers,delimiter=',',quotechar="|")
    for row in mreader:
        temp = Unit((row[0],row[1], row[2], row[3], row[4], row[5], row[6],row[7]))
        Mothers.append(temp)

with open('fathers.csv','r') as fathers:
    freader=csv.reader(fathers,delimiter=',',quotechar="|")
    for row in freader:
        temp = Unit((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        Fathers.append(temp)

with open('children.csv','r') as children:
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

with open('supports.csv','r') as supports:

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
    print(o)
    pass

print()

## Debugging Code

"""
for f in Fathers:
   for m in Mothers:
        print(m.get_name())
        print(f.get_name())
        print(f.get_supports())
        if (m.get_name() in f.get_supports()) or (m.get_name=="Corrin") or (f.get_name=="Corrin"):
            print(m.get_name()," ",f.get_name())
            test_pair(f.get_name(),m.get_name())
            pass
"""

## Main Program Loop
is_running=False
containsCorrin=False

print("Welcome to the Fire Emblem Fates Optimization Tool!")
print("Type 'Help' for a list of available commands.")

while(is_running==True):

    while containsCorrin==False:
        print("Custom Corrin has not been added to the system. Please add it now.")
        print("Use the format '(Bane) (Boon) (Gender) without the brackets.'")
        print("Stat Formats: HP, Str, Mag, Skl, Lck, Spd, Def, Res. Sex: M or F")
        cmd=input("> ")
        split = cmd.split()
        if len(split) == 3:
            containsCorrin=addCorrin(split[0], split[1], split[2])
        else:
            containsCorrin=addCorrin("Lck","Spd","M")

    cmd=input("> ")

    if cmd=="Help":
        print("Available Commands:")
        print("Exit: Closes the Program")
        print("Optimize (Child Name): Prints best partners for that child to have the highest stat requested.")
        print("Pair (Mother) (Father): Pairs the two units and removes them from the unit pool. ")

    elif cmd=="Exit":
        is_running=False

    elif "Print" in cmd:
        split = cmd.split()
        if len(split)==2:
            if split[1]=="Mothers":
                for i in Mothers:
                    i.print_unit()
            elif split[1]=="Fathers":
                for i in Fathers:
                    i.print_unit()
            elif split[1]=="Children":
                for i in Children:
                    i.print_unit()

    elif "Result" in cmd:
        split = cmd.split()
        if len(split) == 3:
            for i in Children:
                if row[1] == "Azura":
                    for i in Fathers:
                        if i.get_name() == temp.get_parent():
                            temp.set_stats(i.get_stats())
                            temp.set_name(namebak)
                else:
                    for i in Mothers:
                        if i.get_name() == temp.get_parent():
                            temp.set_stats(i.get_stats())
                            temp.set_name(namebak)

    ## Test Pair (Father) (Mother)
    elif "Test Pair" in cmd:
        split=cmd.split()
        if len(split) == 4:
            test_pair(split[2],split[3])


    elif "Optimize" in cmd:
        split = cmd.split()
        if len(split) == 3:
            for i in Children:
                if i.get_name==split[1]:
                    ##for j in Mothers:
                    pass
                print("mem")


        else:
            print("Please provide a child name and the stat you want to optimize.")

    else:
        print("Command not recognised. See 'Help' For a list of commands.")