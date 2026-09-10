
from borrowingsystem import BorrowingSystem


class Resource:
    def __init__(self, resource_id, name, is_available=True):
        self.resource_id = resource_id
        self.name = name
        self.is_available = is_available

project = Resource("PRJ001", "Projector")
system = BorrowingSystem()
system.borrow_resource(project, "STU001", due_days=7)
system.borrow_resource(project, "STU002", due_days=5)
system.return_resource(project, "STU001")
system.return_resource(project, "STU002")
system.display_borrowings()





                         