def create(file):
    try:
        file = open(file,"x")
    except FileExistsError:
        print("file is already created") 
    if __name__=="__main__":
        pass   
## add entry
def add_entry(f):
    file = open("journal.txt","a")
    file.write(f)
    if __name__=="__main__":
        pass 
## write 
def write(f):
    file = open("journal.txt","a")
    file.write(f)
    if __name__=="__main__":
        pass 
## View all Entry
def view_entry():
    try:
        file = open("journal.txt","r")
        print(file.read())
    except FileNotFoundError:
        print("\nNo journal entries found. Start by adding a new entry!")
    except Exception as e:
        print("Error found")
    if __name__=="__main__":
        pass 
    return