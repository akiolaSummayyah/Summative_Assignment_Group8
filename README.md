# Summative_Assignment_Group8
This Repository is for group 8 Summative assignment
Test push access - Goodie 

# Campus Resource Centre Borrowing System

## Team Members
- Modupe Summmayyah Akiola
- Goodness Ogadinma Muoka
- Roheemot Opeyemi Yahya
- Titilayo Mary Daniyan

## Project Description
The Campus Resource Centre Borrowing System is a Python application that 
allows students and staff to borrow and return resources from the campus 
resource centre, such as books, equipment, or study materials. The system 
keeps track of available items, who has borrowed what, and due dates, 
helping the resource centre manage its inventory efficiently.


# Main Features


### Resource Management
- **Add Resource** – Register new resources with a unique ID, name, and category (e.g. Electronics, Book, Equipment).
- **Display All Resources** – View every resource in the system along with its availability status.
- **Search Resource** – Find a resource by ID or name (case-insensitive).

### Student Management
- **Register Student** – Enrol students with a unique student ID, name, email, course, and entrance year.
- **Display Registered Students** – View all currently registered students.

### Borrowing & Returning
- **Borrow Resource** – Borrow an available resource for a specified number of days; the due date is calculated automatically.
- **Availability Check** – A resource that is already borrowed cannot be borrowed again until it's returned.
- **Return Resource** – Returning a resource updates its status back to available and closes out the borrowing record.
- **Display Currently Borrowed Resources** – View all borrowing records, including resource ID, student ID, borrow date, due date, and status (Borrowed/Returned).

### Data Persistence
- **JSON File Storage** – Resources, students, and borrowing records are saved to `resources.json`, `students.json`, and `borrowings.json`, so data survives between sessions.
- **Automatic Loading on Startup** – Previously saved data is restored automatically each time the app runs.
- **Immediate Saving** – Every change is written to file right away, so no data is lost if the program closes unexpectedly.

### Input Validation & Error Handling
- **Duplicate Prevention** – Resource and student IDs must be unique.
- **Empty Field Checks** – Required fields like ID and name cannot be left blank.
- **Invalid Number Handling** – Entering non-numeric input for the due date is caught without crashing the app.
- **Missing Record Handling** – Attempting to return an item with no matching borrowing record shows a clear error instead of failing silently.
- **Corrupted File Recovery** – If a data file is missing, empty, or corrupted, the system starts fresh with a warning instead of crashing.

### System Design
- **Object-Oriented Structure** – Built using separate `Resource`, `Student`, `Borrowing`, and `BorrowingSystem` classes across dedicated modules.
- **Serialization Support** – Each class supports `to_dict()` and `from_dict()` for converting objects to and from JSON.
- **Interactive Menu Loop** – A continuous numbered console menu drives the application until the user chooses to exit.
- **Automated Test Script** – `test_run.py` verifies core borrowing behaviour, including successful borrow/return cycles and blocking a resource from being borrowed while already on loan.

