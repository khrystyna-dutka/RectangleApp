import argparse

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
    parser = argparse.ArgumentParser(description="Rectangle Drawer")
    parser.add_argument("--action", type=str, choices=["add", "list"], required=True, help="Action to perform: add or list")
    parser.add_argument("--x", type=int, help="X coordinate of the rectangle")
    parser.add_argument("--y", type=int, help="Y coordinate of the rectangle")
    parser.add_argument("--width", type=int, help="Width of the rectangle")
    parser.add_argument("--height", type=int, help="Height of the rectangle")
    parser.add_argument("--color", type=str, help="Color of the rectangle")

    args = parser.parse_args()
    controller = RectangleController()

    if args.action == "add":
        if args.x is None or args.y is None or args.width is None or args.height is None or args.color is None:
            print("To add a rectangle, you must provide --x, --y, --width, --height, and --color.")
        else:
            controller.add_rectangle(args.x, args.y, args.width, args.height, args.color)
            print("Rectangle added successfully!")

    elif args.action == "list":
        print("\n--- List of Rectangles ---")
        rectangles = controller.list_rectangles()
        if rectangles:
            for i, rect in enumerate(rectangles, start=1):
                print(f"{i}. {rect}")
        else:
            print("No rectangles added yet.")


if __name__ == "__main__":
    main()
