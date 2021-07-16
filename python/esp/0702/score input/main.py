from Add import Add
from Show import Show
from Delete import Delete
from Modify import Modify

functions = [Add, Show, Delete, Modify]

stu_list = []
try:
    file = open("stu_list.txt", 'r')
except:
    pass
else:
    for l in file:
        print(l.rstrip("\n").split(":"))
        stu_list.append(l.rstrip("\n").split(":"))

    file.close()

while 1:
    print("1. add scores")
    print("2. show scores")
    print("3. delete subjects")
    print("4. modify subjects")
    print("5. save and quit")
    try:
        enter = int(input("Please select function："))
    except:
        print("error Please input item number")
    else:
        if enter == 5:
            break
        else:
            stu_list = functions[enter - 1](stu_list).exe()

file = open("stu_list.txt", 'w')
for l in stu_list:
    file.write("{}:{}\n".format(str(l[0]), str(l[1])))
file.close()
