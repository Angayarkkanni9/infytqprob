#Start writing your code here
class Vehicle():
    def __init__(self):
        self.vehicle_id=None
        self.vechile_tye=None
        self.cost=None
        self.premium_amount=None
    def set_vehicle_id(self,vechile_id):
        __self.vehicle_id=vehcile_id
    def get_vehcile_id(self):
        return self.__vehicle_id
    def set_vehcile_type(self,vehicle_type):
        __self.vehicle_type=vehicle_type
    def get_vehicle_type(self):
        return self.__vehicle_type
    def set_cost(self,cost):
        __self.cost=cost
    def get_cost(self):
        return __self.cost
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    def get_premium_amount(self):
        return self.__premium_amount
    def calculate_premium_amount(self):
        if(self.__vehicle_type=="Twowheeler"):
            self.__premium_amount=self.__cost*2/100
            print(self.__premium_amount)
        elif(self.__vehicle_type=="Fourwheeler"):
            self.__premium_amount=self.__cost*6/100
            print(self.__premium_amount)
        else:
            print("vehicle type Invalid")
    def display_vehicle_details(self):
        print("vehicle_id:"+self.__vechile_id)
        print("vechile_tye:"+self.__vehicle_type)
        print("vechile_cost:"+self.__cost)
        print("vechile_premium_amount:"+self.__premium_amount)
        
car=Vehicle()
car.set_vehcile_id(123)
car.set_vehicle_type("Twowheeler")
car.set_cost(1000000)
car.set_premium_amount(1000)
calculate_premium_amount()
display_vehile_details()
            
        
        
        
