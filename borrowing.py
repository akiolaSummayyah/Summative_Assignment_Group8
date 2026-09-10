from datetime import datetime, timedelta

class Borrowing:
    # The class represents a borrowing record, containing information about the resource borrowed, the student who borrowed it, the borrow date, due date, return date, and whether it has been returned or not.
    def __init__(self, resource_id, student_id, due_days, borrow_date=None):
        self.resource_id = resource_id
        self.student_id = student_id
        self.borrow_date = borrow_date if borrow_date else datetime.now()
        self.due_date = self.borrow_date + timedelta(days=due_days)
        self.return_date = None
        self.is_returned = False

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
     
        