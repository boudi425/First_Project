import random, sys, datetime, os
from Important_Functions import fasl, clear_screen, Start_of_project
class Hotel:
    No_Of_Hotels = 0
    def __init__(self, Rate=7.0, Rooms=500, Free_Wifi="✅", Resturant="❌", Parking="✅"):
        self.Rate = Rate
        self.Rooms = Rooms
        self.Free_Wifi = Free_Wifi
        self.Resturant = Resturant
        self.Parking = Parking
        Hotel.No_Of_Hotels += 1
    def Get_Hotel_details(self):
         return (f"""This is the Hotel facilites
                 The Rate is: {self.Rate}
                the Room number is {self.Rooms}
                Is There a Free Wifi :{self.Free_Wifi}
                Is There a Resturant :{self.Resturant}
                Is There a Parking :{self.Parking}
                """)
    def Get_random_Room(self):
        Random_room = random.randint(1, self.Rooms)
        return Random_room
    def Set_New_Room(self, Room_Number, Room_Type, Price, New_status="❌"):
        Access = {"Room_Type": Room_Type, "Room_Number": Room_Number,"Price" : Price,"Taken": New_status}
        return Access
        
class Giza_Hotel(Hotel):
    def __init__(self, Rate=7.0, Rooms=500, Free_Wifi="✅", Resturant="❌", Parking="✅"):
        super().__init__(Rate, Rooms, Free_Wifi, Resturant, Parking) 
        self.Rooms = 750
        self.Rate = 9.5
        self.Resturant = "✅"
        self.Hotel_Name = "Giza Hotel"
    def Get_Hotel_details(self):
        string = super().Get_Hotel_details()
        return string + f"\n This is for {self.Hotel_Name}"       
    def Get_random_Room(self):
        return super().Get_random_Room()
    def Set_New_Room(self, Room_Number, Room_Type, Price, New_status="❌"):
        return super().Set_New_Room(Room_Number, Room_Type, Price, New_status)
class Cairo_Hotel(Hotel):
    def __init__(self, Rate=7, Rooms=500, Free_Wifi="✅", Resturant="❌", Parking="✅"):
        super().__init__(Rate, Rooms, Free_Wifi, Resturant, Parking)
        self.Rooms = 1000
        self.Rate = 8.7
        self.Resturant = "✅"
        self.Parking = "❌"
        self.Hotel_Name = "Cairo Hotel"
    def Get_Hotel_details(self):
        return super().Get_Hotel_details()
    def Get_random_Room(self):
        return super().Get_random_Room()
    
    def Set_New_Room(self, Room_Number, Room_Type, Price, New_status="❌"):
        return super().Set_New_Room(Room_Number, Room_Type, Price, New_status)
    
class Mekka_Hotel(Hotel):
    def __init__(self, Rate=7, Rooms=500, Free_Wifi="✅", Resturant="❌", Parking="✅"):
        super().__init__(Rate, Rooms, Free_Wifi, Resturant, Parking)
        self.Rooms = 1500
        self.Rate = 7.7
        self.Resturant = "✅"
        self.Hotel_Name = "Mekka Hotel"
    def Get_Hotel_details(self):
        return super().Get_Hotel_details()
    def Get_random_Room(self):
        return super().Get_random_Room()
    def Set_New_Room(self, Room_Number, Room_Type, Price, New_status="❌"):
        return super().Set_New_Room(Room_Number, Room_Type, Price, New_status)
class Resrvation:
    def __init__(self):
        self.Hotels = [Giza_Hotel(), Cairo_Hotel(), Mekka_Hotel()]
        self.Giza = Giza_Hotel()
        self.Cairo = Cairo_Hotel()
        self.Rooms = [{"Bed_Type" : "Double Bed", "How_Many_Beds": "One", "How_Many_People" : "1 or 2 adutls", "Room_Service" : "✅", "Price": "25$ per night"},
                  {"Bed_Type": "Double Bed", "How_Many_Beds": "Two", "How_Many_People": "2 adults", "Room_Service": "✅", "Price": "45$ per night"},
                  {"Bed_Type": "Double", "How_Many_Beds": "3", "How_Many_People": "3 adults", "Room_Service": "✅", "Price": "65$ per night"},
                  {"Bed_Type": "Double", "How_Many_Beds": "Four", "How_Many_People": "4 adults", "Room_Service": "✅", "Price": "85$ per night"}]
    def Start(self):
        Start_of_project("Abdelrhaman Hassan", "Reservation System")
        while True:
            try:
                print("-"*30)
                print("Choose from the following options:")
                print("1- Show Hotels")
                print("2- Quit")
                response = input("> ")
                if response == "2":
                    self.Quit()
                elif response == "1":
                    self.Show_hotel_details()
            except ValueError:
                print("Please enter a number")
            except TypeError:
                print("Please Enter either 1 ot 2")
                    
    def Show_Hotels(self):
        print("Here are the Hotels")
        Total = 1
        for Number, Name in enumerate(self.Hotels, start=1):
            print(f"#{Number} Hotel Name: {Name.Hotel_Name}")
            Total += 1
        print(f"#{Total} Quit")
        while True:
            try:
                fasl()
                print("Choose from the following options:")
                Index_Choice = int(input("> "))
                if Index_Choice == Total:
                    self.Quit()
                else:
                    return Index_Choice-1
            except ValueError:
                print("Please Enter a number")
            except TypeError:
                print("Please Enter the number related to the name")
                
    def Show_hotel_details(self):
        global Hotel_Index_Choice
        Hotel_Index_Choice = self.Show_Hotels()
        fasl()
        while True:
            print("Choose from the following options:")
            print("1- Show Facilities")
            print("2- Choose a room to stay in")
            print("3- Quit")
            response = input("> ")
            if response == "1":
                print(self.Hotels[Hotel_Index_Choice].Get_Hotel_details())
            elif response == "2":
                self.Room_Type()
            elif response == "3":
                self.Quit()
            else:
                print("Please Enter a vaild answer")
    def Perpare_The_Stay_Time(self):
        fasl()
        Today_date = self.Get_todays_Date()
        print(Today_date)
        print("Enter the time you want to check in(Month, days):")
        fasl()
        while True:
            try :
                Check_in_day = self.Check_In_day()
                Check_in_Month = self.Check_In_month()
                if datetime.date(2024, Check_in_Month, Check_in_day) < datetime.date(2024, Today_date.month, Today_date.day):
                    print(f"Incorrect date to Check in the date should not be less than {Today_date}")
                else:
                    Check_in_date = datetime.datetime(2024, Check_in_Month, Check_in_day)
                    break
            except TypeError:
                print("Please Enter a vaild input")
        fasl()
        while True:
            try:
                    Check_Out_day = self.Check_Out_day()
                    Check_Out_month = self.Check_Out_month()
                    if datetime.date(2024, Check_Out_month, Check_Out_day) < datetime.date(2024, Today_date.month, Today_date.day):
                        print(f"Incorrect date to Check in the date should not be less than {Today_date}")
                    elif datetime.date(2024, Check_Out_month, Check_Out_day) < datetime.date(2024, Check_in_Month, Check_in_day):
                        print(f"Incorrect date to Check out the date should not be less than {datetime.date(2024, Check_in_Month, Check_in_day)}")
                    else:
                        Check_Out_date = datetime.datetime(2024, Check_Out_month, Check_Out_day)
                        break
            except TypeError:
                print("please enter a vaild answer")
        Adults = self.How_Many_adults()
        Child = self.How_Many_Childern()
        Date_Difference = Check_Out_date - Check_in_date
        return Date_Difference.days
    def Get_Room_details(self, room_index):
            if 0 <= room_index < len(self.Rooms):
                room = self.Rooms[room_index]
                print(f"Bed Type: {room['Bed_Type']}, \nHow Many Beds: {room['How_Many_Beds']}, \nHow Many People: {room['How_Many_People']}, \nRoom Service: {room['Room_Service']}, \nPrice: {room["Price"]}")
            else:
                print(f"Invalid room index: {room_index}")

    def Get_the_Customar_choice(self):
        print("Choose what room type you want to reserve:")
        print("1_ Single Room")
        print("2_ Double Room")
        print("3- Triple Room")
        print("4- Quad_Room")
        fasl()
        while True:
            try:
                Room_Choice = input("> ").capitalize()
                
                if Room_Choice in ["1", "2", "3", "4"]:
                    return Room_Choice 
                else:
                    print("Invalid option. Please try again.")
            except ValueError as ve:
                print(f"ValueError occurred: {ve}")
            except TypeError as te:
                print(f"TypeError occurred: {te}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")    
    def Room_Type(self):
        fasl()
        print("Choose from the following options:")
        print("1- Resrve the Room")
        print("2- Show Room Details")
        print("3- Quit")
        while True:
            response = input("> ")
            if response.isalpha():
                print("Please Enter a vaild option")
            elif int(response) > 4:
                print("Please Enter an option from (1 or 2 or 3)")
            else:
                break
        if response == "2":
            choice = self.Get_the_Customar_choice()
            if choice == "1":
                self.Get_Room_details(0)
            elif choice == "2":
                self.Get_Room_details(1)
            elif choice == "3":
                self.Get_Room_details(2)
            elif choice == "4":
                self.Get_Room_details(3)
        elif response == "1":
            self.Perpare_Rooms()
        else:
            self.Quit()
    def Perpare_Rooms(self):
        List_Of_Rooms_Number = []
        List_Of_Rooms_Type = []
        List_Of_Rooms_Acces = []
        Nights = self.Perpare_The_Stay_Time()
        How_Many_Rooms = self.Get_How_Many_Rooms()
        for Room ,Number in enumerate(range(How_Many_Rooms)):
            print(f"For Room #{Number+1}")
            Room = self.Get_the_Customar_choice()
            if Room == "1":
                List_Of_Rooms_Type.append("Single Room")
            elif Room == "2":
                List_Of_Rooms_Type.append("Double Room")
            elif Room == "3":
                List_Of_Rooms_Type.append("Triple Room")
            elif Room == "4":
                List_Of_Rooms_Type.append("Quad Room")
        #print(List_Of_Rooms_Type)
        for Room_Number in range(How_Many_Rooms):
            Room_Number = self.Hotels[Hotel_Index_Choice].Get_random_Room()
            List_Of_Rooms_Number.append(Room_Number)
        for Index in List_Of_Rooms_Number:
            print(f"Room #{Index} is free to take")
        for Room_Type ,Index in zip(List_Of_Rooms_Type ,List_Of_Rooms_Number):
                if Room_Type == "Single Room":
                    List_Of_Rooms_Acces.append(self.Hotels[Hotel_Index_Choice].Set_New_Room(Index, Room_Type, 25))
                elif Room_Type == "Double Room":
                    List_Of_Rooms_Acces.append(self.Hotels[Hotel_Index_Choice].Set_New_Room(Index, Room_Type, 45))
                elif Room_Type == "Triple Room":
                    List_Of_Rooms_Acces.append(self.Hotels[Hotel_Index_Choice].Set_New_Room(Index, Room_Type, 65))
                elif Room_Type == "Quad Room":
                    List_Of_Rooms_Acces.append(self.Hotels[Hotel_Index_Choice].Set_New_Room(Index, Room_Type, 85))
        fasl()
        print("Choose From the Following options:")
        print("1- Resrve All.")
        print("2- Know the Total Price")
        print("3- Quit")
        while True: 
            response = input("> ")
            if response == "1":
                fasl()
                for Room_Acces in List_Of_Rooms_Acces:
                    Room_Acces["Taken"] = "✅"
                for Text in List_Of_Rooms_Acces:
                        #Access = {"Room_Type": Room_Type, "Room_Number": Room_Number,"Price" : Price,"Taken": New_status}
                        print(f"Room Type : {Text["Room_Type"]}")
                        print(f"Room Number : {Text["Room_Number"]}")
                        print(f"Price : {Text["Price"]}")
                        print(f"Taken : {Text["Taken"]}")
                        print("Go to the Payment?:")
                        print("1- Yes")
                        print("2- No (Quit)")
                        fasl()
            elif response == "2":
                    fasl()
                    Total_Price = 0
                    for A in range(len(List_Of_Rooms_Acces)):
                        Price = List_Of_Rooms_Acces[A]["Price"]
                        Total_Price += Price
                    print(f"The Total Price Will be {Total_Price* Nights}$")   
                    print("resrve?:")
                    print("1- Yes")
                    print("2- No")
            elif response == "3":
                    self.Quit()
            else:
                print("Invaild input please Try again")
                continue
            while True:
                    choice = input(">").capitalize()
                    if choice == "1":
                        Total_Price = 0
                        for Price_index in range(len(List_Of_Rooms_Acces)):
                            Price = List_Of_Rooms_Acces[Price_index]["Price"]
                            Total_Price += Price
                        fasl()
                        print(f"The Total price is {Total_Price* int(Nights)}$")
                        print("Confirm Payment..")
                        print("1- Yes")
                        print("2- No")
                    elif choice == "2":
                        self.Quit()
                    else:
                        print("Invalid option")
                    while True:
                        Confirm_Payment = input("> ").capitalize()
                        if Confirm_Payment == "1":
                            fasl()
                            print("Payment successfully happened")
                            print("Have a good stay, sir")
                            self.Quit()
                        elif Confirm_Payment == "2":
                            self.Quit()
                        else:
                            print("Invalid answer")                   
    def Get_How_Many_Rooms(self):
        fasl()
        print("How many rooms you want to reserve: (MAX: 30)")
        print("For Quit Type (Quit)")
        while True:
            try:
                response = input("> ").capitalize()
                if response == "Quit":
                    self.Quit()
                elif int(response) > 30:
                    print("Please Enter a value less than 30 ")
                    #Boudi --> alpha --> True, Boudi == Quit x True
                elif response.isalpha() and response != "Quit":
                    print("Please Enter a vaild answer")
                else:
                    response = int(response)
                    return response
            except ValueError:
                print("Please Enter a number")
    def Check_In_day(self):
        while True:
            try:
                    print("Enter the day you want to check in:")
                    Check_in_day = input("> ")
                    if Check_in_day.isalpha():
                        print("Please Enter a vaild Number")
                    else:
                        Check_in_day = int(Check_in_day)
                        return Check_in_day
            except ValueError:
                print("Value Error please Enter a number")
    def Check_In_month(self):
        while True:
            try:
                    print("Enter the Month you want to check in: ")
                    Check_in_Month = input("> ")
                    if Check_in_Month.isalpha():
                        print("Please Enter a vaild Number(Like 3 for march)")
                    elif int(Check_in_Month) > 30:
                        print("Enter a vaild answer bewteen (1 - 30)")
                    else:
                        Check_in_Month = int(Check_in_Month)
                        return Check_in_Month
            except ValueError:
                print("Value Erorr please Enter a number")
    def Check_Out_day(self):
        while True:
            try:
                    print("Enter the day you want to check Out:")
                    Check_Out_day = input("> ")
                    if Check_Out_day.isalpha():
                        print("Please Enter a vaild Number")
                    elif int(Check_Out_day) > 30:
                        print("Enter a vaild answer bewteen (1 - 30)")
                    else:
                        Check_Out_day = int(Check_Out_day)
                        return Check_Out_day
            except ValueError:
                print("Value Error Please Enter a number")
    def Check_Out_month(self):
        while True:
            try:
                    print("Enter the Month you want to check Out: ")
                    Check_Out_Month = input("> ")
                    if Check_Out_Month.isalpha():
                        print("Please Enter a vaild Number(Like 3 for march)")
                    elif int(Check_Out_Month) > 12:
                        print("Enter a vaild answer bewteen (1 - 12)")
                    else:
                        Check_Out_Month = int(Check_Out_Month)
                        return Check_Out_Month
            except ValueError:
                print("Value error Please Enter a number")
    def How_Many_adults(self):
        fasl()
        print("How many adults will stay? (MAX: 30)")
        while True:
            try:
                    Adults_number = input("> ")
                    if Adults_number.isalpha():
                        print("Please Enter a vaild number.")
                    elif int(Adults_number) > 30:
                        print("Please Enter at least one or not more than 30")
                    elif int(Adults_number) < 1:
                        print("Please Enter at least 1 adult")
                    else:
                        Adults_number = int(Adults_number)
                        return Adults_number
            except ValueError:
                print("Value Error please Enter a vaild number")
    def How_Many_Childern(self):
        fasl()
        print("How many Children will stay? (MAX: 30)")
        while True:
            try:
                    Childern_Number = input("> ")
                    if Childern_Number.isalpha():
                        print("Please Enter a vaild number.")
                    elif int(Childern_Number) > 30:
                        print("Please Enter not more than 30")
                    else:
                        Childern_Number = int(Childern_Number)
                        return Childern_Number
            except ValueError:
                print("Value error please Enter a number")
    def Get_todays_Date(self):
        Today_Date = datetime.date.today()
        return Today_Date
    def Quit(self):
        print("Thanks for using the programm <3")
        sys.exit()
  