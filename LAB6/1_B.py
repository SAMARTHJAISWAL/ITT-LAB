import string

test_string = "Hello, world! This is a test string with punctuation."
result = ''.join(char for char in test_string if char not in string.punctuation)
print(result)
