def sort_words(s):
    words=s.split()
    n=len(words)
    for i in range (n):
        for j in range(0,n-i-1):
            if words[j]>words[j+1]:
                words[j],words[j+1]=words[j+1],words[j]

    return " ".join(words)
s=input()
print(sort_words(s))
