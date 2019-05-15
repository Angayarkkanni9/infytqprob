def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if(food_type=="N"):
        amount=150
        if(distance_in_kms<3):
            bill_amount=amount*quantity_ordered
        elif(distance_in_kms>3 or distance_in_kms<6):
            bill_amount=(amount*quantity_ordered)*(distance_in_kms-3)*3)
        else:
            bill_amount=(amount*quantity_ordered)*(distance_in_kms*6)
    else:
        amount=120
        if(distance_in_kms<3):
            bill_amount=amount*quantity_ordered
        elif(distance_in_kms>3 or distance_in_kms<6):
            bill_amount=(amount*quantity_ordered)*(distance_in_kms-3)*3)
        else:
            bill_amount=(amount*quantity_ordered)*(distance_in_kms*6)
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
