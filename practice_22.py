def diagonal_stars(number):
    for i in range(0,number+1):
        for j in range(i):
            print(".",end="")
        print("*")
    

number=6    
diagonal_stars(number)
