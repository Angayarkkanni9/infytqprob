#PF-Exer-35

def count_names(name_list):
    count1=0
    count2=0
    for i in range(0,len(name_list)):
        if(name_list[i].endswith("at") and name_list[i].find("at")!=0):
            count1+=1
        if(name_list[i].count("at")!=0):
            count2+=1
    #start writing your code here
    #Populate the variables: count1 and count2

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print("_at -> ",count1)
    print("%at% -> ",count2)


#Provide different names in the list and test your program
name_list=[Hat, Cat, Rabbit, Matter]
count_names(name_list)

