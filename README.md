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

## Main Features

### Resource Management
- **Add Resource** – Register new resources with a unique ID, name, and category (e.g. Electronics, Book, Equipment).
- **Display All Resources** – View every resource in the system along with its availability status.
- **Search Resource** – Find a resource by ID or name (case-insensitive).

### Student Management
- **Register Student** – Enrol students with a unique student ID, name, email, course, and entrance year.
- **Display Registered Students** – View all currently registered students.

### Borrowing & Returning
- **Borrow Resource** – Borrow an available resource for a specified number of days; the due date is calculated automatically.
- **Availability Check** – A resource already borrowed cannot be borrowed again until it is returned.
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
- **Automated Test Script** – `test_run.py` verifies core borrowing behaviour.

## Classes Used

- **`Resource`** – Represents a borrowable item (e.g. projector, laptop, book). Stores a resource ID, name, category, and availability status.
- **`Student`** – Represents a registered student. Stores a student ID, name, email, course, and entrance year.
- **`Borrowing`** – Represents a single borrowing transaction, linking a resource and student with a borrow date, due date, and status (Borrowed/Returned).
- **`BorrowingSystem`** – Manages the core borrowing logic: lending resources, processing returns, checking availability, and tracking all borrowing records.

## Files Used

- **`main.py`** – The entry point of the application; runs the interactive menu and connects all the other modules together.
- **`resource.py`** – Defines the `Resource` class.
- **`student.py`** – Defines the `Student` class.
- **`borrowing.py`** – Defines the `Borrowing` class.
- **`borrowingsystem.py`** – Defines the `BorrowingSystem` class, which handles borrow/return logic.
- **`resources.json`** – Stores all registered resources so data is retained between sessions.
- **`students.json`** – Stores all registered students.
- **`borrowings.json`** – Stores all borrowing records.
- **`test_run.py`** – An automated test script that verifies core borrowing behaviour.

## How to Run the Application

For example:

python main.py


1. Make sure Python 3 is installed on your machine.
2. Open a terminal in the project folder.
3. Run `python main.py`.
4. Follow the on-screen menu to add resources, register students, borrow, and return items.

## Team Contributions

**Goodness Mouka** — Core Classes & Data Structure
* Design and build the main classes (e.g., Resource, Member)
* Decide what info each class stores (name, status, borrower, due date, etc.)
* Write the basic methods each class needs (add resource, check availability, etc.)
* Recorded a video explaining the task done

**Modupe Summayah** — Borrowing System Logic
* Build the BorrowingSystem class — the part that actually handles borrowing and returning items
* Write the logic for checking if something's available, marking it borrowed, and marking it returned
* Handle overdue tracking (comparing dates)
* Recorded a video explaining the task done

**Titilayo Daniyan** — File Handling (Saving & Loading Data)
* Write the code that saves data to a file (e.g., resources.txt/.json) whenever someone borrows/returns something
* Write the code that reads the file back in when the program starts, so nothing is lost between runs
* Make sure the "Files Used" section of the README matches what she built
* Updated the test run. py and main. py
* Recorded a video explaining the task done
* Update the test plan doc, class design and test results

**Yahya Roheemot** — Testing & Documentation
 * Wrote and maintained the project README (Main Features, Classes Used, Files Used, How to Run the     Application, Teams Contribution)
* Carried out full application testing of `main.py`, covering valid and invalid inputs across all menu options (add resource, register student, borrow, return, error handling)
* Verified file handling and data persistence by checking `resources.json`, `students.json`, and `borrowings.json` after running the application
* Resolved Git merge conflicts and removed untracked `__pycache__` files
* Added a `.gitignore` file to keep the repository clean going forward
* Recorded a video explaining the task done