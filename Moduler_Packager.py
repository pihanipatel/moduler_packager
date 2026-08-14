def dati():
    while True:
        print("\nDatetime and Time Operations: \n1. Display current date and time\n2. Calculate diffrence between two dates/times\n3. Format date into custom format\n4. Stopwatch\n5. Countdown Timer\n6. Back to Main Menu ")
        choice = int(input("\nEnter your choice: "))
        match choice:
            case 1:
                import datetime
                now = datetime.datetime.now()
                print("Current Date and Time: ",now)

            case 2:         
                from datetime import datetime,timedelta
                now = datetime.now()
                d1 = input("Enter the first date (yyyy-mm-dd):")
                d2 = input("\nEnter the second date (yyyy-mm-dd): ")

                d3 = datetime.strptime(d1,"%Y-%m-%d")
                d4 = datetime.strptime(d2,"%Y-%m-%d")
                diff = d4-d3
                print("\ndifference between dates in days",diff.days," days")    
            case 3:
                from datetime import datetime
                now = datetime.now()
                today = now.strftime("%m-%d-%Y %H-%M-%S")  
                print("formated date", today)  
            case 4:
                import time
                user = input("Do you want to enter start ,stop,or reset")
                for i in range(10):
                    if user == "start":
                        t = time.sleep(1)
                        print(i)
                    elif user == "stop":
                        break
                    else:
                        t = time.sleep(1)
                        print(i)    
            case 5:
                import time
                for i in range(10):
                    print(i)
                    time.sleep(1)
            case 6:
                break
def maop():
    while True:
        print("\nMathematical Operations: \n1. Calculate Factorial\n2. Solve Compound Interest\n3. Trigonometric Calculations\n4. Area of Geometric Shapes\n5. Advanced mathematical function\n6. Back to main menu")
        chi = int(input("Enter your choice: "))
        match chi:
            case 1:    
                import math    
                f = int(input("Enter a number: "))
                fact = math.factorial(f)
                print("\nFactorial: ",fact,"\n")
                print("=" * 40)
            case 2:
                import math
                p = int(input("\nEnter principal amount: "))
                r = int(input("\nEnter rate of interest (in %): "))
                t = int(input("\nEnter time(in years): "))

                r = 1 + (r / 2)    ##r=p*(1+r/n)
                a = 2 * t       ## n*t
                m = p * math.pow(r,a)
            
                print("Compound Interest",m)
            case 3:
                import math
                t = math.sin(30)
                c = math.cos(45)
                print("Output of sin and cos operations: ",t,c)
            case 4: 
                c = math.pi * math.pow(2,2)
                print("Area of circle: ",c)
            case 5:
                import package.adc_math_func as m
                h = m.func()
            case 6:
                break
def radge():
    while True:
        print("Random Data Generations: \n1. Generate Random Number\n2. Generate Random List\n3. Create Random Password\n4. Generate Random OTP\n5. Back to Main Menu")
        chs = int(input("Enter your choice: "))
        match chs:
            case 1: 
                import random
                l = random.randint(1,10)
                print("Random number: ",l)
            case 2:
                import random
                l = ["Apple","Banana","Cherry","Mango","Blueberry"]
                random.shuffle(l)
                print("Random list: ",l)
            case 3:
                import random
                ch = ""
                length = int(input("Enter password length: "))
                l = ["p","i","o","@","k","2","7","9","0","d","!","h"]
                p = random.sample(l,length)
                for i in range(length):
                    ch += p[i]
                print("Generated Password",ch)
            case 4:
                import random
                for i in range(4): 
                    o = random.randint(1,9)
                    print( o,end=" ")
            case 5:
                break
def fiop():
    while True:
        print("File Operations: \n1. Create a new file\n2. Write to a file\n3. Read from a file\n4. Append to a file\n5. Back to main menu")
        cha =int(input("\nEnter your choice: "))
        match cha:
            case 1:
                import file as fi
                f = input("\nEnter file name: ")
                f = fi.create(f)
                print("\nFile created successfully!\n")
                print("=" * 40)
            
            case 2:
                import file as fi

                f = input("\nEnter file name: ")
                f = input("\nEnter items which you want to write in file: \n")  
                w = fi.write(f)
                print("\nData written successfully!\n")
                print("=" * 40)
            case 3:
                import file as fi

                f = input("Enter file name: ")
                v = fi.view_entry()   
                print("\nThis is a sample file.\n")
                print("=" * 40)
            case 4:
                import file as fi

                f = input("Enter file name: ")
                f = input("Enter items which you want to add in file: \n")  
                w = fi.add_entry(f)
                print("\nData appended successfully.\n")
                print("=" * 40)
            case 5:
                break
def uid():
    print("Explore Module Attributes: \n")
    m = input("Enter module name to explore: ")
    print("Available Attributes in math module: ")
    print(dir(m.__doc__))

print("=" * 40)
print("\nWelcome to Multi-Utility Toolkit\n")
print("=" * 40)
while(True):
    print("\nChoose an option: \n1. Datetime and Time Operations\n2. Mathematical Operations\n3. Random Data Generation\n4. Generate Unique Identifiers (UUID)\n5. File Operations (Custom Module)\n6. Explore Module Attributes (dir())\n7. Exit")
    ch = int(input("\nEnter your choice: "))
    match ch:
        case 1:
            dati()
        case 2:
            maop()
        case 3:
            radge()
        case 4:
            import uuid
            print("Generated UUID",uuid.uuid4())
        case 5:
            fiop()
        case 6:
            uid()
        case 7:
            print("Thank you for using the Multi-Utility Toolkit!" )
        case _:
            print("Invalid choice please choose valid number")
