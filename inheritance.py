class Parent():
    def __init__(self, last_name, eye_color):
        print "Parent Constructor Called"
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, num_of_toys):
        print "Child Constructor Called"
        Parent.__init__(self, last_name, eye_color)
        self.num_of_toys = num_of_toys

# billy_cyrus = Parent("Cyrus", "blue")
# print billy_cyrus.eye_color

miley_cyrus = Child("Cyrus", "blue", 5)
print miley_cyrus.last_name
print miley_cyrus.num_of_toys