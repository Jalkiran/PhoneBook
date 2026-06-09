Contacts={}
while True:
    choice=int(input("1.Add\n2.Show\n3.Search\n4.Delete\n5.Quit\nEnter your choice:"))
    #---ADD---
    if choice==1:
        name=input("Name:").strip().title()
        number=int(input("Number:"))
        Contacts[name]=number
        print("Contact successfully added")
    #---SHOW---
    elif choice==2:
        if not Contacts:
            print('No Contacts Saved.')
        else:
            for name,number in Contacts.items():
                print(name,":",number)
    #---SEARCH---
    elif choice==3:
        search=input("Search:").strip().title()
        found=False
        for name in Contacts:
            if search in name:
                print(name,":",Contacts[name])
                found=True
        if not found :
             print("No contact found")
    #---DELETE---
    elif choice==4:
        name=input("Delete who:").strip().title()
        if name in Contacts:
            Contacts.pop(name)
            print("Deleted")
        else:
            print("Contact not found")
    #---QUIT---
    elif choice==5:
        print("Bye👋")
        break
