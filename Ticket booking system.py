#available seats for booking
available_seats=['1a','1b','2a','2b','3a','3b','4a','4b','5a','5b','5e','6a','7a','7b','8a','9a','9b']
#printing words
start="\nwelcome sir/madam would you like to start the booking ?(yes/no):"
seats="\nhow many seats are you booking today"
seats+="\nenter the no.of seats:"
name="\nwhat is your name:"
seat_number="\nwhich seat you want to book?"
booked_seats="The booked tickets are:"
type_travel="\nTrain or Bus:"
#code for the process
print("\nwelcome to everywhere travel")
v=[]
a=input(start)
a.lower()
if a=="yes":
    typ=input(type_travel)
    typ.lower()
    if typ=="bus":
        print("\nBus Ticket Booking")
    elif typ=="train":
        print("\nTrain Ticket Booking")
    while True:
        b=int(input(seats))
        c=input(name)
        for i in range(b):
            print("\nAvailable seats")
            print(available_seats)
            d=input(seat_number)
            if d in available_seats:
                v.append(d)
                available_seats.remove(d)
            else:
                print("sorry the seat number not available")
        break
        print("you can enter the another seat number:")
    print(c.upper(),booked_seats)
    for i in v:
        print(i)
    print("\nwe will redirecting now to paymant page...")
    print("\nThanks for booking in everywhere travel")
    print("\nHave a nice journey",c)
else:
    print("\nThanks for approaching everywhere travel")