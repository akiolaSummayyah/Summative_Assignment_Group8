class Student:                                      # represents a registered student who can borrow resources from the library
    def __init__(self, student_id, name, email, course, entrance_year, borrowed_resource=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.course = course
        self.entrance_year = entrance_year
        self.borrowed_resource = borrowed_resource if borrowed_resource is not None else []                    # this starts as an empty list and will be filled in as a student borrows resources

    def display_details(self):                                           # shows this student's info in a readable format
        print(f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}, Course: {self.course}, Entrance Year: {self.entrance_year}")

    def add_borrowed_resource(self, resource_id):                               # adds a resource to the student's borrowed list
        self.borrowed_resource.append(resource_id) 

    def remove_borrowed_resource(self, resource_id):                            # removes a resource from the student's borrowed list
        if resource_id in self.borrowed_resource:
            self.borrowed_resource.remove(resource_id)   
    def has_reached_max_borrow(self):                            # checks if the student has reached the maximum borrow limit
        return len(self.borrowed_resource) >= 2
    def to_dict(self):                                              # turns this student into a plain dictionary so it can be written to a file
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "course": self.course,
            "entrance_year": self.entrance_year,
            "borrowed_resource": self.borrowed_resource
        }

    @staticmethod
    def from_dict(data):                                          # rebuilds a Student object from a dictionary that was loaded from a file
        return Student(
            data["student_id"], data["name"], data["email"],
            data["course"], data["entrance_year"], data.get("borrowed_resource", [])
        )