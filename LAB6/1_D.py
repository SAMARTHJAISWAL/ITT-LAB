def merged_mail(name,domain):
    mail=[]
    for i in range (len(name)):
        email=name[i]+"@"+domain[i]
        mail.append(email)
    return mail
name=["samarth","triya","aryan"]
domain=["edu.org","nvidia.us","king.com"]
print(merged_mail(name,domain))
