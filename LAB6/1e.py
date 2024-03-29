import re

def find_replace(text,pattern,replacement):
    return re.sub(pattern,replacement,text)

text="hello hi how are you"
pattern="hi"
replacement="hey"
print(find_replace(text,pattern,replacement))
