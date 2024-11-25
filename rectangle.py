# Програма для побудови прямокутників (без GUI)

# Model
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def __str__(self):
        return (f"Rectangle: x={self.x}, y={self.y}, width={self.width}, "
                f"height={self.height}, color={self.color}")


# Controller
class RectangleController:
    def __init__(self):
        self.model = []

    def add_rectangle(self, x, y, width, height, color):
        rectangle = Rectangle(x, y, width, height, color)
        self.model.append(rectangle)

    def list_rectangles(self):
        return self.model


# Main function
def main():
    controller = RectangleController()

    while True:
        print("\n--- Rectangle Drawer ---")
        print("1. Add Rectangle")
        print("2. List Rectangles")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                x = int(input("Enter x: "))
                y = int(input("Enter y: "))
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                color = input("Enter color (e.g., red, #FF0000): ")

                controller.add_rectangle(x, y, width, height, color)
                print("Rectangle added successfully!")
            except ValueError:
                print("Invalid input. Please enter numeric values for x, y, width, and height.")
        elif choice == "2":
            print("\n--- List of Rectangles ---")
            rectangles = controller.list_rectangles()
            if rectangles:
                for i, rect in enumerate(rectangles, start=1):
                    print(f"{i}. {rect}")
            else:
                print("No rectangles added yet.")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
