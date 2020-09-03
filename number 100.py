class number100:
    
    i = input("select in which type you would like to play type 1 for ODD 2 for EVEN: ")
    z = int(i)

    if z==1:
        print(my_custom_random_odd())
    
    elif z==2:
        print(my_custom_random_eve())
    else:
        print("select anyone type")
        