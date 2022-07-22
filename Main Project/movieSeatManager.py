# Menu
'''
print("* * * 🎟  Ticket Purchase Center 🎟 * * * ")
print("1️⃣: Book a single seat")
print("2️⃣: Book multiple seats in a row")
print("3️⃣: Book a backrow seat")
print("4️⃣: Exit")
'''

# First create your 2d list representation 8 seats, 5 rows 
seatingChar = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
seatingNumber = [['A1','A2','A3','A4','A5','A6','A7','A8'], ['B1','B2','B3','B4','B5','B6','B7','B8'], ['C1','C2','C3','C4','C5','C6','C7','C8'], ['D1','D2','D3','D4','D5','D6','D7','D8'], ['E1','E2','E3','E4','E5','E6','E7','E8']]

# Go through each instruction 
while True:
    print("* * * 🎟  Ticket Purchase Center 🎟 * * * ")
    print("1️⃣: Book a single seat")
    print("2️⃣: Book multiple seats in a row")
    print("3️⃣: Book a whole row for seats")
    print("4️⃣: Exit")
    selection = int(input(" "))

    if selection == 1:
        r = int(input("What row would you like to sit in?(1-5): "))
        c = int(input("What seat would you like to sit in?(1-8): "))
        if seatingChar[r-1][c-1] == 1:
            print("Please choose a different seat")
        elif seatingChar[r-1][c-1] == 0:
            seatingChar[r-1][c-1] = 1
            print(f"You have seat {seatingNumber[r-1][c-1]}")
        else:
            print("Invalid input please try again")
        print("Enjoy your movie!\n")

    elif selection == 2:
        seatAmount = int(input("How many seats would you like to book? "))
        i = 0
        while i in range(seatAmount):
            r = int(input("What row would you like to sit in?(1-5): "))
            c = int(input("What seat would you like to sit in?(1-8): "))
            if seatingChar[r-1][c-1] == 1:
                print("Please choose a different seat")
            elif seatingChar[r-1][c-1] == 0:
                seatingChar[r-1][c-1] = 1
                print(f"You have seat {seatingNumber[r-1][c-1]}")
                print("Enjoy your movie!\n")
            else:
                print("Invalid input please try again")
            i += 1
               
    elif selection == 3:
        row = int(input("What row would you like to book?(1-5): "))
        if 1 in seatingChar:
            print("Sorry, this row is either booked or has seats filled in it already")
        elif 1 not in seatingChar:
            seatingChar[row-1] = 1
            print(f"You have row {row} booked")
        else:
            print("Invalid input please try again")
        print("Enjoy your movie!\n")
            
    elif selection == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid input, please try again\n")
    
