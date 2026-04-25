import re

txt = 'i love doing python and java and Python is very easy language'
match = re.match('i love',txt, re.I)
print(match)

span = match.span()
print(span)

txt = 'i love doing python and java'
search = re.search('and',txt, re.I)
print(search)

matches = re.findall('and',txt, re.I)
print(matches)

txt = 'i love doing python and java and Python is very easy language'
matches_replaced = re.sub('python|Python','javascript',txt,re.I)
print(matches_replaced)