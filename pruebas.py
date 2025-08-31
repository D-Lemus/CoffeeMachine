while True:
    try:
        donate = int(input("You want to donate a dollar to dog shelter \n\n\t1 - YES\n\t2 - NO, IN OTHER MOMENT\n> ").strip())
        if (donate == 1):
            total += 1
            print(f"Thanks, your new total is ${total}")
            break
        elif (donate == 2):
            print(f"Thanks, your total is ${total}")
            break
        else:
            print("Enter a valid number")
    except ValueError:
        print("Enter a valid number")


print("What is yor payment method?\n\n\t1 - CARD\n\t2 - CASH")
method =int(input().strip())
while True:
    try:
        if (method == 1):
            print(f"Thanks, you are to going pay ${total} with card")
            break
        elif (method == 2):
            print(f"Thanks, you are to going pay ${total} with cash")
            break
        else:
            print("Enter a valid number")
    except ValueError:
        print("Enter a valid number")

