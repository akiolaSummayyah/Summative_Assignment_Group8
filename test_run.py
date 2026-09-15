from resource import Resource                         # use the real Resource class instead of a local copy
from borrowingsystem import BorrowingSystem

project = Resource("PRJ001", "Projector", "Electronics")   # real Resource needs a category as the 3rd argument
system = BorrowingSystem()
system.borrow_resource(project, "STU001", due_days=7)
system.borrow_resource(project, "STU002", due_days=5)
system.return_resource(project, "STU001")
system.return_resource(project, "STU002")
system.display_borrowings()