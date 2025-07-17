# CLI contact book(CSV powered)
import csv
import os
FILENAME = "contacts.csv"
if not os.path.exists(FILENAME):
    with open(FILENAME,"w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name","Phone","Email"])
def add_contact():
    name = input("Name :").strip()
    phone = input("Phone :").strip()
    email = input("Email : ").strip()

    #check for duplicate  
    with open(FILENAME,"r",encoding="utf-8") as f: 
        reader = csv.DictReader(f)   
        for row in reader:
            if row['Name'].lower()  == name.lower():
                print("Contact name already exist")
            return
                
    with open(FILENAME,"a",encoding="utf-8") as f: 
        writer = csv.writer(f)  
        writer.writerow([name, phone, email])
        print("Contact added")
def view_contact():
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        rows = list(reader)
        if len(rows)<1:
            print("NO contact founds")
            return
        print("\nYour contacts :\n")
        for row in rows[1:]:
            if len(row) < 3:
                continue  # Skip rows that don't have all 3 fields
            print(f"{row[0]} | {row[1]} | {row[2]}")

        print()
def search_contact():
    term = input("Enter the name to search :").strip()
    found = False
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']}")
                found = True
            
            
    if not found:
        print("No matching contact found")

def main():
    while True:
        print("\n Contact book")
        print("1. Add Contact")
        print("2. View All Contact")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Chose an option(1-4) : ").strip()
        if choice == "1" :
            add_contact()
        elif choice =='2':
            view_contact()
        elif choice =='3':
            search_contact()
        elif choice =='4':
            print("Thanks to use our Software")
            break
        else:
            print("Invalid choice")

if __name__ ==  "__main__":
    main()


