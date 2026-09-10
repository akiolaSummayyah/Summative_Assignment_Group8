from borrowing import Borrowing

class BorrowingSystem:
     # This class manages the borrowing system, allowing students to borrow and return resources, as well as check for overdue items.
    def __init__(self):
        self.borrowings = []

    def borrow_resource(self, resource, student_id, due_days):
        # The use of this method is to allow a student to borrow a resource. It checks if the resource is available and creates a new borrowing record if it is.
        if not resource.is_available:
            print(f"Sorry, '{resource.name}' is currently unavailable.")
            return False 

        if due_days <= 0:
            print("Number of days must be greater than zero.")
            return False

        borrowing = Borrowing(resource.resource_id, student_id, due_days)
        self.borrowings.append(borrowing)
        resource.is_available = False
        print(f"'{resource.name}' has been borrowed successfully. Due in {due_days} days.")
        return True
    
    def return_resource(self, resource, student_id):
        # This method allows a student to return a borrowed resource. It checks if the resource is currently borrowed by the student and marks it as returned if found.
        for borrowing in self.borrowings:
            if borrowing.resource_id == resource.resource_id and borrowing.student_id == student_id and not borrowing.is_returned:
                borrowing.mark_returned()
                resource.is_available = True
                print(f"'{resource.name}' has been returned successfully.")
                return True

        print("No active borrowing record found for this resource and student, check the resource ID and student ID and try again.")
        return False

    def display_borrowings(self):
        # This method displays all borrowing records, including their status (borrowed, returned, or overdue).
        if not self.borrowings:
            print("No borrowed items found.")
            return

        for borrowing in self.borrowings:
            print(borrowing.display())

    def display_overdue(self):
        # And here is the display_overdue method, which checks for any overdue borrowings and displays them. If there are no overdue items, it informs the user accordingly.
        overdue_found = False
        for borrowing in self.borrowings:
            if borrowing.is_overdue():
                print(borrowing.display())
                overdue_found = True

        if not overdue_found:
            print("No overdue items.")



