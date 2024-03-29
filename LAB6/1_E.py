import re

def find_and_replace(s,p,r):
    return re.sub(p,r,s)
s="hello hi whassup"
p="hi"
r="hey"
print(find_and_replace(s,p,r))
