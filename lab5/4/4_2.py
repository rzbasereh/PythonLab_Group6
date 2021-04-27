# Working with directories

import os
from os import path

dir_name = 'input_files'
dist_path = os.path.join(os.getcwd(), dir_name)

if not ( path.exists(dist_path) and  path.isdir(dist_path) ):
    try: 
        os.mkdir(dist_path) 
    except OSError as error: 
        print(error)  

file = open(dist_path + "/python_lab.txt","w+")
file.write('Reza Basereh')
file.close()
