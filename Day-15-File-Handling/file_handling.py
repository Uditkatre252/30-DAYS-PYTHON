# import os
#
# os.remove('C:/Users/uditk/OneDrive/Desktop/files/r_file.txt.txt')

# # creating a file and overwrite if already exist
# f = open('C:/users/uditk/onedrive/Desktop/files/udit.txt','w')
# f.write('Hello World')
# f.close()

# read file
w = open('C:/users/uditk/onedrive/Desktop/files/udit.txt','a+')
w.write('Hello World\n')
w.seek(0)
print(w.read())
w.close()

