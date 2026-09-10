class Resource:                                           # represents a single borrowable item (e.g. a book) in the library
    def __init__(self, resource_id, name, category, is_available=True):
        self.resource_id = resource_id
        self.name = name
        self.category = category
        self.is_available = is_available                     # defaults to True - a new resource starts out available

    def mark_borrowed(self):                                  # called when a student successfully borrows this resource
        self.is_available = False

    def mark_returned(self):                                 # called when a student successfully returns this resource
        self.is_available = True

    def display_details(self):                               # shows this resource's info in a readable format
        print(f"Resource ID: {self.resource_id}, Name: {self.name}, Category: {self.category}, Availability: {'Available' if self.is_available else 'Not Available'}")    