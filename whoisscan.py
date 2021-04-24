import whois

while(True):
    url = input("nama domain website : ")
    w = whois.query(url)

    for key,val in w.__dict__.items():
        print(key,':',val)

    i = input("\nkeluar ketik 'q' lalu enter : ")

    if i =='q':
        break

