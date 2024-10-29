# Match Case similar to switch in JAVa
number = int(input("enter the number"))
match number :
    case 1 :
        print("you have enterd 1")
    case 2 :
        print("you have enterd 2")
    case 3 :
        print("you have enterd 3")
    case _ :
        print("no idea")
# break is not neeed in match