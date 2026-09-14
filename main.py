import json                                                  # built-in module used to read/write our data as JSON files
from resource import Resource
from student import Student
from borrowing import Borrowing
from borrowingsystem import BorrowingSystem

RESOURCES_FILE = "resources.json"                             # where all Resource objects get saved
STUDENTS_FILE = "students.json"                                # where all Student objects get saved
BORROWINGS_FILE = "borrowings.json"                             # where all Borrowing records get saved

all_resources = []                                          # holds every Resource object created in this session
all_students = []                                            # holds every Student object registered in this session
system = BorrowingSystem()                                   # manages all borrowing/returning logic


def load_data():
    # Reads all three JSON files (if they exist) and rebuilds the in-memory lists.
    # If a file doesn't exist yet (e.g. first time running the app), we just start with empty lists instead of crashing.
    global all_resources, all_students
    try:
        with open(RESOURCES_FILE, "r") as f:
            data = json.load(f)
            all_resources = [Resource.from_dict(item) for item in data]
    except FileNotFoundError:                                 # normal on first run - there's nothing saved yet
        all_resources = []
    except json.JSONDecodeError:                              # file exists but is empty/broken - don't crash, just start clean
        print(f"Warning: {RESOURCES_FILE} was empty or corrupted. Starting fresh.")
        all_resources = []

    try:
        with open(STUDENTS_FILE, "r") as f:
            data = json.load(f)
            all_students = [Student.from_dict(item) for item in data]
    except FileNotFoundError:
        all_students = []
    except json.JSONDecodeError:
        print(f"Warning: {STUDENTS_FILE} was empty or corrupted. Starting fresh.")
        all_students = []

    try:
        with open(BORROWINGS_FILE, "r") as f:
            data = json.load(f)
            system.borrowings = [Borrowing.from_dict(item) for item in data]
    except FileNotFoundError:
        system.borrowings = []
    except json.JSONDecodeError:
        print(f"Warning: {BORROWINGS_FILE} was empty or corrupted. Starting fresh.")
        system.borrowings = []


def save_resources():                                         # writes the current all_resources list to file
    with open(RESOURCES_FILE, "w") as f:
        json.dump([r.to_dict() for r in all_resources], f, indent=2)


def save_students():                                          # writes the current all_students list to file
    with open(STUDENTS_FILE, "w") as f:
        json.dump([s.to_dict() for s in all_students], f, indent=2)


def save_borrowings():                                        # writes the current borrowings list to file
    with open(BORROWINGS_FILE, "w") as f:
        json.dump([b.to_dict() for b in system.borrowings], f, indent=2)


def find_resource(resource_id):                               # looks through all_resources for a matching ID, returns None if not found
    for r in all_resources:
        if r.resource_id == resource_id:
            return r
    return None


def find_student(student_id):                                 # looks through all_students for a matching ID, returns None if not found
    for s in all_students:
        if s.student_id == student_id:
            return s
    return None


load_data()                                                  # load any previously saved data before the menu starts

while True:                                                  # keeps the menu running until the user chooses to exit
    print("=================================")
    print("      SCHOOL LIBRARY SYSTEM")
    print("=================================")
    print("1. Add Resource")
    print("2. Display All Resources")
    print("3. Search Resource (by ID or Name)")
    print("4. Register Student")
    print("5. Display Registered Students")
    print("6. Borrow Resource")
    print("7. Return Resource")
    print("8. Display Currently Borrowed Resources")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':                                        # user wants to add a new resource to the library
        resource_id = input("Enter Resource ID: ").strip()
        if not resource_id:                                    # validation - an empty ID isn't allowed
            print("Resource ID cannot be empty.")
            continue
        if find_resource(resource_id):                          # validation - no two resources should share an ID
            print(f"A resource with ID '{resource_id}' already exists.")
            continue
        name = input("Enter Resource Name: ").strip()
        if not name:                                            # validation - an empty name isn't allowed
            print("Resource name cannot be empty.")
            continue
        category = input("Enter Resource Category: ").strip()
        new_resource = Resource(resource_id, name, category)
        all_resources.append(new_resource)                     # store the new resource in the master list
        save_resources()                                        # write the updated list to file immediately
        print(f"Resource '{name}' added successfully.")

    elif choice == '2':                                      # user wants to see every resource currently in the system
        if not all_resources:
            print("No resources available.")
        else:
            for resource in all_resources:
                resource.display_details()

    elif choice == '3':                                       # user wants to find a specific resource by ID or name
        search_term = input("Enter Resource ID or Name to search: ").strip()
        found_resources = []
        for resource in all_resources:
            if resource.resource_id == search_term or resource.name.lower() == search_term.lower():   # matches on either ID or name, case-insensitive for name
                found_resources.append(resource)
        if not found_resources:
            print("No matching resources found.")
        else:
            for resource in found_resources:
                resource.display_details()

    elif choice == '4':                                       # user wants to register a new student
        student_id = input("Enter Student ID: ").strip()
        if not student_id:                                      # validation - an empty ID isn't allowed
            print("Student ID cannot be empty.")
            continue
        if find_student(student_id):                            # validation - no duplicate student IDs
            print(f"A student with ID '{student_id}' is already registered.")
            continue
        name = input("Enter Student Name: ").strip()
        if not name:                                            # validation - an empty name isn't allowed
            print("Student name cannot be empty.")
            continue
        email = input("Enter Student Email: ").strip()
        course = input("Enter Student Course: ").strip()
        entrance_year = input("Enter Student Entrance Year: ").strip()
        new_student = Student(student_id, name, email, course, entrance_year)
        all_students.append(new_student)                        # store the new student in the master list
        save_students()                                          # write the updated list to file immediately
        print(f"Student '{name}' registered successfully.")

    elif choice == '5':                                       # user wants to see every registered student - NEW, wasn't connected before
        if not all_students:
            print("No students registered.")
        else:
            for student in all_students:
                student.display_details()

    elif choice == '6':                                       # user wants to borrow a resource - NEW, wasn't connected before
        resource_id = input("Enter Resource ID to borrow: ").strip()
        student_id = input("Enter Student ID: ").strip()
        resource = find_resource(resource_id)
        student = find_student(student_id)

        if not resource:                                        # validation - can't borrow something that doesn't exist
            print(f"No resource found with ID '{resource_id}'.")
            continue
        if not student:                                          # validation - unregistered students can't borrow
            print(f"No student found with ID '{student_id}'.")
            continue
        if student.has_reached_max_borrow():                     # validation - enforce the 2-item borrow limit
            print(f"'{student.name}' has already reached the maximum of 2 borrowed resources.")
            continue

        try:
            due_days = int(input("Enter number of days until due: "))   # this is where letters instead of numbers would normally crash the app
        except ValueError:
            print("Please enter a valid whole number for days.")
            continue

        success = system.borrow_resource(resource, student_id, due_days)   # borrowingsystem.py already checks availability and due_days > 0
        if success:
            student.add_borrowed_resource(resource_id)
            save_resources()
            save_students()
            save_borrowings()

    elif choice == '7':                                       # user wants to return a resource - NEW, wasn't connected before
        resource_id = input("Enter Resource ID to return: ").strip()
        student_id = input("Enter Student ID: ").strip()
        resource = find_resource(resource_id)
        student = find_student(student_id)

        if not resource:
            print(f"No resource found with ID '{resource_id}'.")
            continue
        if not student:
            print(f"No student found with ID '{student_id}'.")
            continue

        success = system.return_resource(resource, student_id)
        if success:
            student.remove_borrowed_resource(resource_id)
            save_resources()
            save_students()
            save_borrowings()

    elif choice == '8':                                       # user wants to see everything currently borrowed - NEW, wasn't connected before
        system.display_borrowings()

    elif choice == '0':                                       # user wants to exit the application
        print("Goodbye!")
        break

    else:                                                     # user typed something that isn't a valid menu option - previously this just did nothing silently
        print("Invalid choice. Please enter a number between 0 and 8.")