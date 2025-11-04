import csv

file_path="C:\\Python prctice\\CODSOFT\\Contact.csv"
header=["Name","Number","Email","Address"]


def menu():
    print("\nContact Menu")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. delete Contact")
    print("6. Exit from Contact")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact()

    elif choice == 3:
        num= int(input("Enter Number: "))
        srch_contact(num)
    elif choice == 4:
        num= int(input("Enter Number: "))
        update_contact(num)
    elif choice == 5:
         num= int(input("Enter Number: "))
         del_contact(num)
    else:
        exit()


def add_contact():
    print("\n Enter Contact Details")
    name = input("Enter Name: ")
    number = int(input("Enter Number: "))
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    new_contact={"Name":name, "Number": number, "Email":email, "Address": address}

    with open(file_path, "a", newline="") as ad_cont:
        write = csv.DictWriter(ad_cont,fieldnames=header)
        write.writerow(new_contact)
    menu()


def view_contact():
    with open(file_path,"r") as rd_cont:
        read = csv.DictReader(rd_cont)
        for contacts in read:
            print(contacts)
    menu()

def srch_contact(num):
    with open(file_path,"r") as sr_cont:
        read = csv.DictReader(sr_cont)
        for contacts in read:
            if contacts["Number"] == str(num):
                print("Contact Found: ")
                print(contacts)
    menu()

def update_contact(num):
    upd=[]
    with open(file_path,"r") as u_cont:
        read=csv.DictReader(u_cont)
        for contact in read:
            if contact["Number"] == str(num):
                key = input("Enter Key to be updated(Name , Number, Email, Address) ")
                value = input("Enter Value of the updated key: ")
                contact[key]=value
            upd.append(contact)

    with open(file_path, 'w',newline="") as upd_co:
        write= csv.DictWriter(upd_co,fieldnames=header)
        write.writeheader()
        write.writerows(upd)

    menu()
def del_contact(num):
    upd=[]
    with open(file_path,'r') as delfile:
        read=csv.DictReader(delfile)
        for contact in read:
            if contact["Number"]!= str(num):
                upd.append(contact)
    with open(file_path, "w" , newline="") as delfile:
        write = csv.DictWriter(delfile,fieldnames=header)
        write.writeheader()
        write.writerows(upd)
    menu()

with open(file_path,"w",newline="") as f:
    write = csv.DictWriter(f,fieldnames=header)
    write.writeheader()

menu()
    




