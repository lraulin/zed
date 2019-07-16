class SinglyLinkedListNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}: {repr(nval)}"


class SingleLinkedList:
    def __init__(self):
        self.begin = None
        self.current = None
        self.end = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current.nxt:
            raise StopIteration(self)
        else:
            return self.current.nxt

    @property
    def is_empty(self) -> bool:
        return not self.begin

    def next(self):
        self.__next__()

    def push(self, obj):
        """Appends a new value on the end of the list."""
        new_node = SinglyLinkedListNode(obj)
        self.end = self.end.nxt = new_node

    def pop(self):
        """Removes the last item and returns it."""

    def shift(self, obj):
        """Another name for push."""
        self.push(obj)

    def unshift(self):
        """Removes the first item and returns it."""
        item = self.begin
        self.begin = self.begin.nxt
        return item

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        prev = None
        for node in self:
            if node == obj:
                try:
                    prev.nxt = node.nxt
                    return self
                except AttributeError:
                    self.begin = node.nxt
                    return self

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end

    def count(self):
        """Counts the number of elements in the list."""
        self.current = self.begin
        count = 0

        for _ in self:
            count += 1

        return count

    def get(self, index):
        """Get the value at index."""
        if index < 0:
            raise IndexError
        else:
            current_index = 0
            self.current = self.begin
            while current_index != index:
                self.current = self.current.nxt
            return self.current

    def dump(self, mark=None):
        """Debugging function that dumps the contents of the list."""
        for node in self:
            print(node)
