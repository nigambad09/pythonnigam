# Match Case similar to switch in JAVa
browser = input("enter the number")
match browser :
    case "chrome" :
        print("you have enterd chrome")
    case "edge" :
        print("you have enterd eddge")
    case "google":
        print("you have enterd google")
    case _ :
        print("no idea")
# break is not neeed in match