import os
import json
import csv
from encodings import utf_8


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

# data = {
#         "name": "udit katre",
#         "email": "uditkatre7@gmail.com",
#     }
#
# data_json = json.dumps(data,indent = 4)
# # print(type(data_json))
# # print(data_json)
# data["city"] = "Bhopal"
# data["age"] = '22'
# with open("data.json","w",encoding='utf-8') as f:
#
#     json.dump(data,f,ensure_ascii=False,indent=4)
#
#
# with open("data.json","r",encoding='utf-8') as f:
#     print(f.read())
#
# if 'name' in data_json:
#     print(data['name'])
#
#
# temp = '''{
#         "name": "udit katre",
#         "email": "uditkatre7@gmail.com"
# }'''
# print(temp)
# temp_dict = json.loads(temp)
# print(type(temp_dict))
# print(temp_dict)
# print(temp_dict['name'])
# print(temp_dict['email'])

# with open('C:/Users/uditk/OneDrive/Desktop/files/csv_example.csv') as f:
#    csv_reader = csv.reader(f,delimiter=',')
#    line_count = 0
#
#    for row in csv_reader:
#        print()

       # if line_count == 0:
       #     print(f'Column names are :{", ".join(row)}')
       #     line_count += 1
       # else:
       #     print(
       #         f'\t{row[0]} is doing {row[3]}. He lives in {row[1]}, {row[2]}.')
       #     line_count += 1
       # print(f'Number of lines:  {line_count}'
       #     )

# def count_number_of_lines(f):
#     f.write("this is my file\n")
#
# w = open('C:/users/uditk/onedrive/Desktop/files/r_file.txt.txt','w+')
# count_number_of_lines(w)
# print(w.read())

student ={
    "name" : "udit",
    "age" : "23",
    "gender" : "Male"
}

student_json = json.dumps(student)
print(student_json)
print(type(student_json))

with open("student.json", "w",encoding='utf_8') as f:
    json.dump(student_json,f,ensure_ascii=False,indent=4)

with open("student.json","r",encoding='utf-8') as f:
     print(f.read())