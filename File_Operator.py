def create(file):
    try:
        file = open(file,"x")
    except FileExistsError:
        print("file is already created") 
     
## add entry
def add_entry(f):
    file = open("journal.txt","a")
    file.write(f)
    print("\nEntry added successfully!")
     
## write 
def write(f):
    file = open("journal.txt","a")
    file.write(f)
    
## View all Entry
def view_entry():
    try:
        print("Output (If the file exixts):\nYour Journal Entries:\n","-"*40)
        file = open("journal.txt","r")
        print(file.read())
    except FileNotFoundError:
        print("\nNo journal entries found. Start by adding a new entry!")
    except Exception as e:
        print("Error found")
     

print("Welcome to Personal Journal Manager!\n")
print("Please select an option: \n")

## Search entry
def search_entry(keyword):
    found = False
    file = open("journal.txt","r")
    line = file.readlines()
    for i in line:
        if keyword.lower() in i.lower():
            print("\nMatching Entries: \n","-"*40,"\n",i)
            found = True   
        if not found:
            print("Output (If no match is found):\n")  
            print("No entries were found for the keyword: ",keyword) 
    file.close()
## delete entry                
def delete_entry(ans):
    try:
        if ans == "yes":
            file = open("Journal.txt","w")
            file.write()
            file.close()
    except:
        print("error")
    else: 
        print("\nOutput (If the file does not exist):\nNo journal entries to delete.")    

while True:

    print("1. Add a New Entry\n2. View All Entries\n3. Search for an Entry\n4. Delete All Entries\n5. Exit")
    choice = int(input("User Input: "))
   
    match choice:
        case 1:
            f = input("Enter items which you want to add in file: \n")      ### Add entry
            a = add_entry(f)
        case 2:                     ## View entry
            v = view_entry()      
        case 3:                     ## Search entry
            keyword = input("\nEnter a keyword or date to search: ")    
            s = search_entry(keyword)   
        case 4:                      ## delete entry
            ans = input("Are you sure you want to delete all entries? (yes/no): ").lower()
            delete_entry(ans)
        case 5:     
            print("Output:\nThank you for using Personal Journal Manager.Goodbye!")
        case _:
            print("\nOutput:\nInvalid option. Please select a valid option from the menu.")