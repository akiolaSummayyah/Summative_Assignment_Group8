from resource import Resource
from student import Student
from borrowingsystem import BorrowingSystem

all_resources = []                                          # holds every Resource object created in this session
all_students = []                                            # holds every Student object registered in this session
system = BorrowingSystem()                                   # manages all borrowing/returning logic

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
        resource_id = input("Enter Resource ID: ")
        name = input("Enter Resource Name: ")
        category = input("Enter Resource Category: ")
        new_resource = Resource(resource_id, name, category)
        all_resources.append(new_resource)                     # store the new resource in the master list
        print(f"Resource '{name}' added successfully.")

    elif choice == '2':                                      # user wants to see every resource currently in the system
        if not all_resources:
            print("No resources available.")
        else:
            for resource in all_resources:
                resource.display_details()

    elif choice == '3':                                       # user wants to find a specific resource by ID or name
        search_term = input("Enter Resource ID or Name to search: ")
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
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        email = input("Enter Student Email: ")
        course = input("Enter Student Course: ")
        entrance_year = input("Enter Student Entrance Year: ")
        new_student = Student(student_id, name, email, course, entrance_year)
        all_students.append(new_student)                        # store the new student in the master list
        print(f"Student '{name}' registered successfully.")