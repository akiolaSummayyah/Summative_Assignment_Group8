from datetime import datetime, timedelta

class Borrowing:
    # The class represents a borrowing record, containing information about the resource borrowed, the student who borrowed it, the borrow date, due date, return date, and whether it has been returned or not.
    def __init__(self, resource_id, student_id, due_days, borrow_date=None, return_date=None, is_returned=False):
        self.resource_id = resource_id
        self.student_id = student_id
        self.borrow_date = borrow_date if borrow_date else datetime.now()
        self.due_date = self.borrow_date + timedelta(days=due_days)
        self.return_date = return_date
        self.is_returned = is_returned

    def mark_returned(self, return_date=None):
         # the use of this method is to mark the borrowing record as returned, setting the return date to the current date or a specified date.
         self.return_date = return_date if return_date else datetime.now()
         self.is_returned = True

    def is_overdue(self):
         # This method checks if the borrowing is overdue by comparing the current date with the due date. If the item has been returned, it is not considered overdue.
         if self.is_returned:
             return False
         return datetime.now() > self.due_date

    def display(self):
         # The use of this method is to display the borrowing record's details, including the resource ID, student ID, borrow date, due date, and status (borrowed, returned, or overdue).
         if self.is_returned:
             status = "Returned"
         elif self.is_overdue():
             status = "Overdue"
         else:
             status = "Borrowed"
         return (f"Resource ID: {self.resource_id}, Student ID: {self.student_id}, "
                 f"Borrow Date: {self.borrow_date.strftime('%Y-%m-%d')}, "
                 f"Due Date: {self.due_date.strftime('%Y-%m-%d')}, Status: {status}")

    def to_dict(self):                                        # turns this borrowing record into a plain dictionary so it can be written to a file
        return {
            "resource_id": self.resource_id,
            "student_id": self.student_id,
            "borrow_date": self.borrow_date.strftime('%Y-%m-%d %H:%M:%S'),
            "due_date": self.due_date.strftime('%Y-%m-%d %H:%M:%S'),
            "return_date": self.return_date.strftime('%Y-%m-%d %H:%M:%S') if self.return_date else None,
            "is_returned": self.is_returned
        }

    @staticmethod
    def from_dict(data):                                      # rebuilds a Borrowing object from a dictionary that was loaded from a file
        borrow_date = datetime.strptime(data["borrow_date"], '%Y-%m-%d %H:%M:%S')
        due_date = datetime.strptime(data["due_date"], '%Y-%m-%d %H:%M:%S')
        due_days = (due_date - borrow_date).days                # works out how many days apart borrow_date and due_date were, so the constructor still works the same way
        return_date = datetime.strptime(data["return_date"], '%Y-%m-%d %H:%M:%S') if data["return_date"] else None
        return Borrowing(data["resource_id"], data["student_id"], due_days, borrow_date, return_date, data["is_returned"])