class Element(object):
    """docstring for Element class"""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """docstring for LinkedList class"""
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """docstring for append"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:
            return None
        current = self.head
        for i in range(1, position):
            if current:
                current = current.next
            else:
                break
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        counter = 1
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                else:
                    current = current.next
        pass

    def insert_first(self, new_element):
        """docstring for insert_first"""
        new_element.next = self.head
        self.head = new_element
        pass

    def delete_first(self):
        """docstring for delete_first"""
        current = self.head
        if current:
            self.head = current.next
            return current
        else:
            return None


class Stack(object):
    """docstring for Stack class"""
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        """docstring for push"""
        self.ll.insert_first(new_element)

    def pop(self):
        """docstring for pop"""
        self.ll.delete_first()


class Queue:
    """docstring for Queue class"""
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        """docstring for enqueue"""
        self.storage.append(new_element)
        pass

    def peek(self):
        """docstring for peek"""
        return self.storage[0]

    def dequeue(self):
        """docstring for dequeue"""
        return self.storage.pop(0)


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# print "Should print 3"
print ll.head.next.next.value
# print "Should also print 3"
print ll.get_position(3).value
print ll.get_position(47)
print ll.get_position(0)

# Test insert
ll.insert(e4, 3)
# print "Should print [1, 2, 4, 3] now"
print [ll.get_position(x).value for x in range(1, 5)]

# Test delete
ll.delete(1)
# print "Should print 2 now"
print ll.get_position(1).value
# print "Should print 4 now"
print ll.get_position(2).value
# print "Should print 3 now"
print ll.get_position(3).value
