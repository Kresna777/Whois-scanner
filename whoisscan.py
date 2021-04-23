import whois

while(True):
    url = input("nama domain website : ")
    w = whois.whois(url)

    for key,val in w.items():
        print(key,':',val)

    i = input("\nkeluar ketik 'q' : ")

    if i =='q':
        break

