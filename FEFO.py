import csv

class Unit:
    data=[]

    def __init__(self,data):
        self.data=data

    def print_unit(self):
        print("Name: ",self.data[0],"Str: ",self.data[1],"Mag: ",self.data[2],"Skl",self.data[3],"Spd",self.data[4],"Lck",self.data[5],"Def",self.data[6],"Res",self.data[7])

    def get_name(self):
        return self.data[0]

    def set_name(self,name):
        self.data[0]=name

    def get_stats(self):
        return self.data

    def set_stats(self,data):
        self.data=list(data)

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

## Main Program Loop
is_running=True


print("Welcome to the Fire Emblem Fates Optimization Tool!")
print("Type 'Help' for a list of available commands.")

while(is_running==True):

    cmd=input("> ")

    if cmd=="Help":
        print("Available Commands:")
        print("Exit: Closes the Program")
        print("Optimize (Child Name): Prints best partners for that child to have the highest stat requested.")
        print("Pair (Mother) (Father): Pairs the two units and removes them from the unit pool. ")

    if cmd=="Exit":
        is_running=False

    if "Optimize" in cmd:
        split = cmd.split()
        if len(split) == 3:
            for i in Children:
                ##if i.get_name==split[1]:
                    ##for j in Mothers:
                print("mem")


        else:
            print("Please provide a child name and the stat you want to optimize.")