import os
import json
#
# os.remove('C:/Users/uditk/OneDrive/Desktop/files/r_file.txt.txt')

# # creating a file and overwrite if already exist
# f = open('C:/users/uditk/onedrive/Desktop/files/udit.txt','w')
# f.write('Hello World')
# f.close()

# # read file
# w = open('C:/users/uditk/onedrive/Desktop/files/udit.txt','a+')
# w.write('Hello World\n')
# w.seek(0)
# print(w.read())
# w.close()
#
# print(w)

data = {
        "name": "udit katre",
        "email": "uditkatre7@gmail.com",
    }

data_json = json.dumps(data,indent = 4)
# print(type(data_json))
# print(data_json)
data["city"] = "Bhopal"
with open("data.json","w",encoding='utf-8') as f:

    json.dump(data,f,ensure_ascii=False,indent=4)


with open("data.json","r",encoding='utf-8') as f:
    print(f.read())
