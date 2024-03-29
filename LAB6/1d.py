def merged_mail(name,domain):
    mail=[]
    for i  in range(len(name)):
        email=name[i]+"@"+domain[i]
        mail.append(email)
    return mail

name=["samarth","triya"]
domain=["edu.in","terrorist.org"]
print(merged_mail(name,domain))
        
