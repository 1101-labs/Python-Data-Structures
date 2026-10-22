
class MiniStack:
    def __init__(self):
        
        self.numbers = [10, 45, 65, 33, 22]



    def push(self, item):

        self.numbers.append(item)

        print(f"{item} has been added")

    def pop(self):

        try:
            print(f"{self.numbers[-1]} has been removed")

            self.numbers.pop()
        except IndexError:
            print("List is empty")

    
    def peek(self):
        try:
            print(self.numbers[-1])
        except IndexError:
            print("List is empty")
        

    def is_empty(self):
        if len(self.numbers) == 0:
            print("Empty")
        else:
            print("List not empty")

    def size(self):
        return len(self.numbers)


    def clear(self):
        self.numbers.clear()



def main():
    stack = MiniStack()

    while True:
        print("""

        1. Add number
        2. Remove number
        3. Check top number
        4. Check if empty
        5. Check number of elements
        6. Clear
        7. Exit

        """)

        
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Enter an integer")
            continue
        

        if choice == 1:
            try:
                value = int(input("Enter the number: "))
            except ValueError:
                print("Enter integer number")

                continue

            stack.push(value)

        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            stack.is_empty()
        elif choice == 5:
            print("Size: ", stack.size())
        elif choice == 6:
            stack.clear()
        elif choice == 7:
            break
        else:
            print("Enter number 1-7")


if __name__ == "__main__":
    main()
