# Working with files 

file = open("python_lab.txt","w+")
file.write('Reza Basereh')
file.close()

file = open("python_lab.txt","a+")
file.write('\n95105968')
file.close()

with open("python_lab.txt", 'r') as file:  
    entry = file.read()
    print(entry)

with open("python_lab.txt", 'r') as file:  
    lines = file.readlines()
    for line in lines:
        print(line.rstrip('\n'))
