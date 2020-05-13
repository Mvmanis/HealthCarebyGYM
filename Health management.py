print("****************THIS IS A HEALTH MANAGEMENT SYSTEM*********************")
select=int(input("Enter what you want\n1:Feed the data\n2:Reterive the data\n"))
print("\n")
name=input("Enter the name for whom you want to manage health system:\nHarry\nManish\nRahul\n")
print("\n")
choice=(input("Enter which plan you want\nDiet\nExercise\n"))
print("\n")
choice=choice.capitalize()
def getdate():
    import datetime
    return datetime.datetime.now()
def inform(name,choice):
    if(choice==("Diet")):
        print("Enter", name, "Breakfast,Lunch,Dinner")
        f = open(str(name + choice + ".txt"), "a")
        f.write(str("["+str(getdate())+"]"+" "))
        print("Breakfast:", end="")
        f.write("Breakfast:")
        f.write(input())
        print("Lunch:", end="")
        f.write(",Lunch:")
        f.write(input())
        print("Dinner:", end="")
        f.write(",Dinner:")
        f.write(input())
        f.write("\n")
        f.close()
    if (choice == "Exercise"):
        print("Enter", name, "exercise plan")
        f = open(str(name + choice + ".txt"), "a")
        f.write(str("["+str(getdate())+"]"+" "))
        print("Shoulder:", end="")
        f.write("Shoulder:")
        f.write(input())
        print("Triceps:", end="")
        f.write(",Triceps:")
        f.write(input())
        print("Chest:", end="")
        f.write(",Chest:")
        f.write(input())
        f.write("\n")
        f.close()
def reterive(name,choice):
    f=open(str(name+choice+".txt"),"r")
    data=f.read()
    print(data)
time=getdate()
if(select==1):
    inform(name,choice)
    while(1):
        more=input("Do you want to continue data feeding enter y/n\n")
        print("\n")
        if more==("Y") or more=="y":
             name = input("Enter the name for whom you want to manage health system:\nHarry\nManish\nRahul\n")
             print("\n")
             choice = (input("Enter which plan you want\nDiet\nExercise\n"))
             print("\n")
             choice = choice.capitalize()
             inform(name,choice)
        else:
             break
if(select==2):
 reterive(name,choice)
 while(1):
     more = input("Do you want to continue reterive data again enter y/n\n")
     print("\n")
     if more == ("Y") or more == "y":
         name = input("Enter the name for whom you want to manage health system:\nHarry\nManish\nRahul\n")
         print("\n")
         choice = (input("Enter which plan you want\nDiet\nExercise\n"))
         print("\n")
         choice = choice.capitalize()
         reterive(name, choice)
     else:
         break



# so we are going to decide all the thing which you was not able to find out




