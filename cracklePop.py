for x in range(100):

    if (x+1)%3==0 and (x+1)%5==0:
        print("Cracklepop")
    elif (x+1)%3==0:
        print("Crackle")
    elif (x+1)%5==0:
        print("Pop")
    else:
        print(x+1)
