import re

txt = 'i love doing python and java'
match = re.match('i love',txt, re.I)
print(match)

span = match.span()
print(span)

