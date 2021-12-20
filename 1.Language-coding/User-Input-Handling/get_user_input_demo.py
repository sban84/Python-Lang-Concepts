""" get user input """

toBreak = False
counter = 0
inp = ""
while toBreak != True:
    if (inp.lower() == "quit") | (counter == 3):
        print("Sorry max times exceeded", counter, " and input is  ", inp)
        toBreak = True
    else:
        inp = input("Enter a number between 1 to 10 ( type quit to exit )")
    # if 1 <= int(inp) <= 10:
    try:
        if 1 <= int(inp) <= 10:
            print("You have entered ", inp)
            print("counter", counter)
        else:
            counter += 1
            print("counter", counter)

    except ValueError as e:
        counter += 1
        print(f"counter {counter} and ValueError exception occurred {e}")
