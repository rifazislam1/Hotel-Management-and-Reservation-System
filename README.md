# Hotel-Management-and-Reservation-System

# 🏨 Hotel Management and Reservation System

A command-line **Hotel Management and Reservation System** developed using Python. This project helps manage hotel rooms, guest reservations, check-ins, check-outs, billing, and reservation records through a simple menu-driven interface.

It is a beginner-friendly project that demonstrates the practical use of Python functions, dictionaries, loops, conditional statements, exception handling, and date calculations.

## ✨ Features

- 🛏️ **Display All Rooms** — View room numbers, room types, prices, and availability status.
- ✅ **View Available Rooms** — Display only rooms that are available for booking.
- 📝 **Make Reservations** — Book a room by entering guest details and stay dates.
- 🧾 **Automatic Bill Calculation** — Calculate the total cost based on room price and number of nights.
- 🔑 **Guest Check-In** — Update the reservation and room status when a guest checks in.
- 🚪 **Guest Check-Out** — Generate the final bill and make the room available again.
- 📋 **View All Reservations** — Display all reservation records.
- 🔍 **Search Reservations** — Find a reservation using its reservation ID.
- ❌ **Cancel Reservations** — Cancel reservations before check-in.
- ⚠️ **Input Validation** — Handle invalid menu choices, room numbers, reservation IDs, and date formats.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Module:** `datetime`
- **Interface:** Command Line / Terminal
- **Data Storage:** Python dictionaries (in-memory)

## 🛏️ Room Details

The system includes eight predefined rooms.

| Room Numbers | Room Type | Price per Night |
|---|---|---:|
| 101–103 | Single | ₹1,500 |
| 201–203 | Double | ₹2,500 |
| 301–302 | Deluxe | ₹4,000 |

## 📂 Project Structure

```text
Hotel-Management-System/
│
├── Hotel_Management_and_Reservation_System.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer.

Check whether Python is installed:

```bash
python --version
```

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Hotel-Management-System.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Hotel-Management-System
   ```

3. Run the program:

   ```bash
   python Hotel_Management_and_Reservation_System.py
   ```

   If necessary, use `python3` instead of `python`.

## ▶️ How to Use

After running the program, a menu appears with the following options:

```text
=============================================
       HOTEL MANAGEMENT SYSTEM
=============================================
1. Display All Rooms
2. Display Available Rooms
3. Make a Reservation
4. Guest Check-In
5. Guest Check-Out and Billing
6. View All Reservations
7. Search Reservation
8. Cancel Reservation
9. Exit
=============================================
Enter your choice (1-9):
```

Choose an option from `1` to `9` to perform the required operation.

### Making a Reservation

1. Select option `3`.
2. Choose an available room.
3. Enter the guest's name and phone number.
4. Enter the check-in and check-out dates in `YYYY-MM-DD` format.
5. The system calculates the total number of nights and the reservation amount.
6. A unique reservation ID is generated and displayed.

### Guest Check-In and Check-Out

- **Check-in:** Enter the reservation ID to mark the guest as checked in and the room as occupied.
- **Check-out:** Enter the reservation ID to display the final bill, complete the checkout, and make the room available again.

## 💡 Example: Reservation and Billing

Suppose a guest books a Single room for three nights.

```text
Reservation Successful!
Reservation ID : 1001
Guest Name     : Rahul
Room Number    : 101
Check-in       : 2026-10-15
Check-out      : 2026-10-18
Total Nights   : 3
Total Amount   : Rs. 4500
```

The calculation is:

**Total Amount = Price per Night × Number of Nights**

For this example:

₹1,500 × 3 = ₹4,500

*Note: This is an illustrative example. The actual reservation ID and output depend on the program's current state and the entered details.*

## 🧠 Main Functions

| Function | Purpose |
|---|---|
| `display_rooms()` | Displays all hotel rooms. |
| `available_rooms()` | Lists rooms available for booking. |
| `make_reservation()` | Creates a reservation and calculates the bill. |
| `check_in_guest()` | Processes guest check-in. |
| `check_out_guest()` | Processes checkout and displays the final bill. |
| `view_reservations()` | Displays all reservations. |
| `search_reservation()` | Searches for a reservation by ID. |
| `cancel_reservation()` | Cancels an eligible reservation. |
| `main()` | Runs the menu and handles user choices. |

## 🎯 Learning Objectives

This project helps beginners understand:

- Creating and calling Python functions.
- Storing structured information using dictionaries.
- Using loops and conditional statements.
- Handling invalid input with `try-except`.
- Working with dates using the `datetime` module.
- Calculating booking costs.
- Managing room and reservation statuses.
- Building a menu-driven application.

## ⚠️ Limitations

- Reservation data is stored in memory and is lost when the program exits.
- The system uses predefined rooms and prices.
- It does not use a database or graphical user interface.
- It does not include online payments or user authentication.
- Room availability is managed by the program's current status rather than a full date-based booking calendar.

## 🔮 Future Improvements

- Add permanent storage using SQLite or MySQL.
- Build a graphical user interface using Tkinter.
- Add hotel staff login and authentication.
- Prevent overlapping reservations for the same room.
- Add payment status and invoice generation.
- Allow administrators to add, edit, and remove rooms.
- Generate reports on bookings and hotel revenue.

## 🤝 Contributing

Suggestions and contributions are welcome!

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## 📄 License

This project is available for educational and learning purposes. You can add an [MIT License](https://opensource.org/license/mit) if you want others to reuse and modify the code under its terms.

---

**If you find this project useful, consider giving the repository a ⭐ on GitHub!**

*Developed as a Python programming project to practice hotel room management and reservation handling.*
