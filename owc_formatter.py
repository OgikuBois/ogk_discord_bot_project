import os

def owcComplete(mapInput):
    ofd = open("new_owc.txt", "r+")
    wfd = open("temp_owc.txt", "w+")

    # lines = ofd.read()
    # print(lines)
    
    for x in ofd:
        output = ""
        line = x.split('\n')
        nl = line[0].split(':')
        if nl[0] == str(mapInput):
            nl = ["%", nl[0], ":", nl[1], "%"]
        else:
            if len(nl)>1:
                nl = [nl[0], ":", nl[1]]
        for i in nl:
            output += i
        output += "\n"
        wfd.write(output)

    ofd.close()
    wfd.close()

    with open("temp_owc.txt") as f:
        with open("new_owc.txt", "w") as f1:
            for line in f:
                f1.write(line)
    os.remove("temp_owc.txt")

def owcList():
    fd = open("new_owc.txt", "r")
    print(fd.read())


def owcClear():
    with open("new_owc.txt") as f:
        with open("temp_owc.txt", "w") as f1:
            for x in f:
                line = x.replace("=", "")
                print(line)
                # if line[0] == " ":
                #     line[0] = ""
                # f1.write(line)
                  
    with open("temp_owc.txt") as f:
        with open("new_owc.txt", "w") as f1:
            for line in f:
                f1.write(line)

    os.remove("temp_owc.txt")
    rfd = open("new_owc.txt", "r")
owcClear()
# owcComplete("NM1")
# owcComplete("FM1")
# owcComplete("HD1")
# owcClear()
# line = "asdf     \n a"
# if line[-1] == " ":
#     line = line.strip()
#     print("owo")
# print(line)


#$owc 


# def owcComplete():
#     owcMap = input("Enter completed map: ") #NM1

#     "~~"  + the line + "~~"

