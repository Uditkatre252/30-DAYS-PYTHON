import numpy
import pandas
import webbrowser
# # print(numpy.__version__)
# lst = [1,2,3,4,5]
# np_array = numpy.array(lst)
# print(np_array)

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

for url in url_lists:
    webbrowser.open_new_tab(url)