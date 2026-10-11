print("===========================")
print("SHOPPING DISCOUNT CALCULTOR")
print("===========================\n")
pe = 0
valid = 0
while valid <= 100000:
    try:
        p=int(input("Enter the total cost to be paid:"))
        d = int(input("Enter discout percentage in whole numbers: "))   
    except ValueError:
        print("Type numbers only.")
    except ZeroDivisionError:
        print("Bill amount or discount amount can't be zero")
    else:
         print("Pay ",p / d," units")
    finally:
        print("This bill finished")
    mon = str(input("More customer (yes / no):"))
    if mon == "yes":
        pe = pe + 1
        continue
    elif mon == "no":
        pe = pe + 1
        break 
    else:
        print("invalid input")
        pe = pe + 1
print("Total customers served:",pe)
