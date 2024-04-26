class Set:
    def __init__(self):
        self.elements = set()

    def add(self, element):
        self.elements.add(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            print(f"{element} is not in the set.")

    def contains(self, element):
        return element in self.elements

    def display(self):
        print("Elements in the set:")
        for element in self.elements:
            print(element)

# Demonstration
if __name__ == "__main__":
    my_set = Set()

    while True:
        print("\nSet Operations:")
        print("1. Add element")
        print("2. Remove element")
        print("3. Check membership")
        print("4. Display elements")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter element to add: ")
            my_set.add(element)
        elif choice == 2:
            element = input("Enter element to remove: ")
            my_set.remove(element)
        elif choice == 3:
            element = input("Enter element to check membership: ")
            if my_set.contains(element):
                print(f"{element} is in the set.")
            else:
                print(f"{element} is not in the set.")
        elif choice == 4:
            my_set.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
