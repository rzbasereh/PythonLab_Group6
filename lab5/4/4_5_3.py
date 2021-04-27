
import re

with open("sqspell.php") as file:
    lines=file.readlines()

    for line in lines:
        x = re.match("^[^#]",line)
        if x:
            print(line)
