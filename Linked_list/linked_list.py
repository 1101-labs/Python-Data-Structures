class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


class MiniLinkedList:
    def __init__(self):

        self.head = None

        
    def append(self, value):

        new_node = Node(value)

        if self.head is None:

            self.head = new_node
            
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node


    def display(self):

        current = self.head

        if current is None:
            print("No nodes available")


        while current is not None:

            print(f"Node: {current.data}")

            current = current.next


    def length(self):

        self.count = 0
        current = self.head


        while current is not None:

            self.count += 1

            current = current.next

        print(f"Number of nodes: {self.count}")


    def contains(self, search):

        current = self.head

        while current is not None:

            if current.data == search:

                return True

            current = current.next

        return False



    def remove(self, number):
        current = self.head

        while current is not None:
            if current.data == number:

                self.head = current.next

                return
        

            elif current.next is not None and current.next.data == number:
                current.next = current.next.next

                return

            else:

                current = current.next




linked_list = MiniLinkedList()

def main():

    while True:

        print("""

        1. Add number
        2. Display numbers
        3. Check list length
        4. Search numbers
        5. Delete number
        6. Exit
        """)

        try:
            choice = int(input("Enter choice 1-6: "))
        except ValueError:
            print("Enter number 1-6")
            continue



        if choice == 1:
            try:
                num = int(input("Enter number: "))
                linked_list.append(num)
            except ValueError:
                print("Enter only integer 0-9")

        elif choice == 2:
            linked_list.display()
        elif choice == 3:
            linked_list.length()
        elif choice == 4:
            try:
                num_search = int(input("Enter the number: "))
                print(linked_list.contains(num_search))
            except ValueError:
                print("Enter only an integer 0-9")

        elif choice == 5:
            try:
                num_delete = int(input("Enter the number: "))
                linked_list.remove(num_delete)
            except ValueError:
                print("Enter only integer 0-9")

        elif choice == 6:
            break
        else:
            print("Enter numbers 1-6")



if __name__ == "__main__":
    main()



