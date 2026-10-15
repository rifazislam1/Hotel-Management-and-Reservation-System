from datetime import datetime

# ------------------------- HOTEL DATA -----------------------------------

rooms = {
    101:{'type':'Single','price':1500,'status':'Available','guest':None},
    102:{'type':'Single','price':1500,'status':'Available','guest':None},
    103:{'type':'Single','price':1500,'status':'Available','guest':None},
    201:{'type':'Double','price':2500,'status':'Available','guest':None},
    202:{'type':'Double','price':2500,'status':'Available','guest':None},
    203:{'type':'Double','price':2500,'status':'Available','guest':None},
    301:{'type':'Deluxe','price':4000,'status':'Available','guest':None},
    302:{'type':'Deluxe','price':4000,'status':'Available','guest':None}
}

reservations = {}
next_reservation_id = 1001


# -------------------------- DISPLAY ROOMS -----------------------------

def display_rooms():
    print("\n =========== ROOM DETAILS =============")
    print(f"{'Room':<10}{'Type':<12}{'Price/Night':<15}{'Status':<15}")
    print("-"*52)

    for room_no , room in rooms.items():
        print(f"{room_no:<10}"
              f"{room['type']:<12}"
              f"Rs.{room['price']:<11}"
              f"{room['status']:<15}"
              )

#--------------------------- AVAILABLE ROOMS ---------------------------

def available_rooms():
    print("\n=========== AVAILABLE ROOMS ==============")
    found = False

    for room_no,room in rooms.items():
        if room['status']=='Available':
            print(
                f"Room:{room_no}|"
                f"Type:{room['type']}|"
                f"Price:{room['price']} per night"
            )
            found = True
    if not found:
         print("Sorry,no rooms are available.")



#------------------------- MAKE RESERVATION -----------------------------

def make_reservation():
    global next_reservation_id

    print("\n============== ROOM RESERVATION ================")
    available_rooms()

    try:
        room_no = int(input("\n Enter room number: "))

        if room_no not in rooms:
            print("Invalid room number.")
            return

        if rooms[room_no]["status"] != "Available":
            print("This room is already booked or occupied.")
            return

        name = input("Enter guest name: ").strip()
        if not name:
            print("Guest name cannot be empty.")
            return

        phone = input("Enter phone number: ").strip()
        if not phone:
            print("Phone number cannot be empty.")
            return

        check_in = input("Enter check_in date (YYYY-MM-DD): ")
        check_out = input("Enter check_out date (YYYY-MM-DD): ")

        in_date = datetime.strptime(check_in,"%Y-%m-%d")
        out_date = datetime.strptime(check_out,"%Y-%m-%d")

        if out_date <= in_date:
            print("Check-out date must be after check-in date.")
            return

        nights = (out_date - in_date).days
        price = rooms[room_no]['price']
        total = nights*price

        reservation_id = next_reservation_id
        next_reservation_id += 1

        guest = {
            "name":name,
            "phone":phone,
            "check_in":check_in,
            "check_out":check_out,
            "nights":nights,
            "total":total,
            "reservation_id":reservation_id
        }

        reservations[reservation_id] = {
            "room_no": room_no,
            "guest": guest.copy(),
            "status":"Reserved"
        }

        rooms[room_no]["status"] = "Reserved"
        rooms[room_no]["guest"] = guest.copy()

        print("\nReservation Successful!")
        print(f"Reservation ID : {reservation_id}")
        print(f"Guest Name     : {name}")
        print(f"Room Number    : {room_no}")
        print(f"Check-in       : {check_in}")
        print(f"Check-out      : {check_out}")
        print(f"Total Nights   : {nights}")
        print(f"Total Amount   : Rs. {total}")
    except ValueError:
        print("Invalid input.Please enter valid dates and numbers.")


#--------------------------- CHECK IN -----------------------------------

def check_in_guest():
    print("\n============= GUEST CHECK-IN =================")
    try:
        reservation_id = int(input("Enter reservation ID: "))
        if reservation_id not in reservations:
            print("Reservation not found.")
            return

        reservation = reservations[reservation_id]

        if reservation["status"] != "Reserved":
            print("This reservation cant be checked in.")
            return

        room_no = reservation["room_no"]

        reservation["status"] = "Checked In"
        rooms[room_no]["status"] = "Occupied"

        print("Guest checked in successfully!")
        print(f"Guest Name: {reservation['guest']['name']}")
        print(f"Room Number: {room_no}")

    except ValueError:
        print("Please enter a valid reservation ID.")


#----------------------------- CHECK OUT ---------------------------------

def check_out_guest():
 print("\n============== GUEST CHECK-IN ===================")

 try:
     reservation_id = int(input("Enter reservation ID: "))

     if reservation_id not in reservations:
         print("Reservation not found.")
         return
     
     reservation = reservations[reservation_id]

     if reservation["status"] != "Checked In":
         print("Guest must be checked in before checkout.")
         return

     room_no = reservation["room_no"]
     guest = reservation["guest"]

     print("\n========== FINAL BILL ==========")
     print(f"Guest Name    : {guest['name']}")
     print(f"Room Number   : {room_no}")
     print(f"Room Type     : {rooms[room_no]['type']}")
     print(f"Price/Night   : Rs. {rooms[room_no]['price']}")
     print(f"Total Nights  : {guest['nights']}")
     print(f"Total Amount  : Rs. {guest['total']}")
     print("================================")

     reservation["status"] = "Checked Out"
     rooms[room_no]["status"] = "Available"
     rooms[room_no]["guest"] = None

     print("Checkout completed successfully!")
     print("Room is now available for a new guest.")

 except ValueError:
        print("Please enter a valid reservation ID.")

# ---------------- VIEW RESERVATIONS ----------------

def view_reservations():
    print("\n========== ALL RESERVATIONS ==========")

    if not reservations:
        print("No reservations found.")
        return

    for reservation_id, reservation in reservations.items():
        guest = reservation["guest"]

        print("-" * 40)
        print(f"Reservation ID : {reservation_id}")
        print(f"Guest Name     : {guest['name']}")
        print(f"Phone          : {guest['phone']}")
        print(f"Room Number    : {reservation['room_no']}")
        print(f"Check-in       : {guest['check_in']}")
        print(f"Check-out      : {guest['check_out']}")
        print(f"Total Amount   : Rs. {guest['total']}")
        print(f"Status         : {reservation['status']}")

    print("-" * 40)


# ---------------- SEARCH RESERVATION ----------------

def search_reservation():
    print("\n========== SEARCH RESERVATION ==========")

    try:
        reservation_id = int(input("Enter reservation ID: "))

        if reservation_id not in reservations:
            print("Reservation not found.")
            return

        reservation = reservations[reservation_id]
        guest = reservation["guest"]

        print(f"\nReservation ID: {reservation_id}")
        print(f"Guest Name: {guest['name']}")
        print(f"Phone: {guest['phone']}")
        print(f"Room Number: {reservation['room_no']}")
        print(f"Check-in: {guest['check_in']}")
        print(f"Check-out: {guest['check_out']}")
        print(f"Total Amount: Rs. {guest['total']}")
        print(f"Status: {reservation['status']}")

    except ValueError:
        print("Please enter a valid reservation ID.")


# ---------------- CANCEL RESERVATION ----------------

def cancel_reservation():
    print("\n========== CANCEL RESERVATION ==========")

    try:
        reservation_id = int(input("Enter reservation ID: "))

        if reservation_id not in reservations:
            print("Reservation not found.")
            return

        reservation = reservations[reservation_id]

        if reservation["status"] != "Reserved":
            print("Only reservations that have not checked in can be cancelled.")
            return

        room_no = reservation["room_no"]

        reservation["status"] = "Cancelled"
        rooms[room_no]["status"] = "Available"
        rooms[room_no]["guest"] = None

        print("Reservation cancelled successfully.")

    except ValueError:
        print("Please enter a valid reservation ID.")


# ---------------- MAIN MENU ----------------

def main():
    while True:
        print("\n" + "=" * 45)
        print("       HOTEL MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Display All Rooms")
        print("2. Display Available Rooms")
        print("3. Make a Reservation")
        print("4. Guest Check-In")
        print("5. Guest Check-Out and Billing")
        print("6. View All Reservations")
        print("7. Search Reservation")
        print("8. Cancel Reservation")
        print("9. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            display_rooms()
        elif choice == "2":
            available_rooms()
        elif choice == "3":
            make_reservation()
        elif choice == "4":
            check_in_guest()
        elif choice == "5":
            check_out_guest()
        elif choice == "6":
            view_reservations()
        elif choice == "7":
            search_reservation()
        elif choice == "8":
            cancel_reservation()
        elif choice == "9":
            print("Thank you for using the Hotel Management System!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 9.")


# ---------------- RUN PROGRAM ----------------

if __name__ == "__main__":
    main()
     
        

   



