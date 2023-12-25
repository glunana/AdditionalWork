class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        current = self.head
        while current:
            print(f"<->{current.data}", end="")
            current = current.next
        print("<->None")

    def addElementsOnEvenPositions(self):
        current = self.head
        while current and current.next:
            new_element = input("Введіть новий елемент для парної позиції: ")
            new_node = Node(new_element)
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            current = new_node.next
            print(f"Додано новий елемент на парну позицію: {new_node.data}")

    def insert_at_end(self):
        num_elements = int(input("Введіть кількість елементів для початкового списку: "))
        for _ in range(num_elements):
            data = input("Введіть елемент: ")
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node

initial_list = List()
initial_list.insert_at_end()

print("Початковий список:")
initial_list.display()

initial_list.add_elements_on_even_positions()

print("Список після додавання елементів на парні позиції:")
initial_list.display()
