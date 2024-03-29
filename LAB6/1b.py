import string

def remove_punctuations(s):
    return s.translate(str.maketrans('', '', string.punctuation))

# Example usage:
s = "Hello, world!"
print(remove_punctuations(s))  # Output: Hello world
