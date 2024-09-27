class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize with length and width
        self.length = length
        self.width = width

    def __iter__(self):
        # Create an iterator that returns length and width in the specified format
        return iter([
            {'length': self.length},
            {'width': self.width}
        ])

# Example usage
rect = Rectangle(10, 5)

# Iterating over the Rectangle instance
for dimension in rect:
    print(dimension)
