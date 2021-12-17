while True:
    try:
        x = int(input("Please input your num:"))
        print("perfect...")
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

