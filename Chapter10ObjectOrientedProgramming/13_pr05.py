#Write a class train which methals to book a ticket get status (no of seats) and fare information of trains running under indian Railways
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print("**************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("**********")
    def fareInfo(self):
        print(f"The price of the ticket is {self.fare}")
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry This train is full, Kindly try in Tatkal")
        def cancelTicket(self,seatno):
            pass
intercity=Train("Dhanbad Allepi",100,4)
intercity.getStatus() 
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()