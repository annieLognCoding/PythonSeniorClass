class MyClass:
    # Class variable shared by all instances
    class_variable = 'shared_value'
    
    def __init__(self, attribute1, attribute2):
        """
        Constructor: Initializes the new instance of the class.
        :param attribute1: Assigned to instance variable attribute1.
        :param attribute2: Assigned to instance variable attribute2.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def my_method(self, parameter):
        """
        Example of an instance method: Operates on instance variables and parameters.
        :param parameter: Example parameter to demonstrate method functionality.
        """
        # Code that manipulates instance variables using 'self'
        print(f"Method called with parameter: {parameter}")
        print(f"Accessing instance variable: {self.attribute1}, {self.attribute2}")
        
    @staticmethod
    def my_static_method(parameter):
        """
        Example of a static method: Does not access any instance or class variables.
        :param parameter: Example parameter to demonstrate static method functionality.
        """
        # Static method code here
        print(f"Static method called with parameter: {parameter}")

# Instantiate the class
my_object = MyClass('value1', 'value2')

# Call an instance method
my_object.my_method('testing')

# Access and print a class variable
print(MyClass.class_variable)

# Call a static method using the class name
MyClass.my_static_method('static parameter')