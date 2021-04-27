import re

#finding GNU
with open("GPL-3") as file:
    m=file.readlines()

    for line in m:
        x = re.search("^GNU",line)
        if x:
            print(line)
