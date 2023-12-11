"""Implement of Linked List"""

class LinkedListItem:
    """Item of the linked list"""

    def __init__(self, data) -> None:
        self.data = data
        self.next_item = None
        self.prev_item = None

class LinkedList:
    """Ring double linked list"""

    def __init__(self, first_item=None) -> None:
        self.first_item = first_item
        self.size = 0
        if self.first_item is not None:
            self.first_item = first_item
            first_item.next_item = first_item
            first_item.prev_item = first_item
            self.size += 1

        # vars for __iter__, __next__
        self._current = None
        self._stop = None

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        self._current = self.first_item
        self._stop = False
        return self

    def __next__(self) -> LinkedListItem:
        if self._stop:
            raise StopIteration

        if self.first_item is None:
            self._stop = True
            return None

        item =  self._current
        if self._current.next_item == self.first_item:
            self._stop = True
        self._current = self._current.next_item
        return item

    def __getitem__(self, index) -> LinkedListItem:
        if self.first_item is None:
            raise IndexError("LinkedList is empty")

        current_item = self.first_item
        current_index = 0

        while True:
            if current_index == index:
                return current_item
            if current_item.next_item == self.first_item:
                raise IndexError("Index out of range")
            current_item = current_item.next_item
            current_index += 1

    def __contains__(self, data) -> bool:
        if self.first_item is None:
            return False

        current_item = self.first_item
        while True:
            if current_item.data == data:
                return True
            if current_item.next_item == self.first_item:
                return False
            current_item = current_item.next_item

    def append_right(self, data) -> None:
        """ Appends a new item to the end of list

        Args:
            data:  data of item to be added to the end
        """

        new_item = LinkedListItem(data)
        if self.first_item is None:
            self.first_item = new_item
            new_item.next_item = new_item
            new_item.prev_item = new_item
            self.size += 1
            return

        last_item = self.first_item.prev_item
        last_item.next_item = new_item
        new_item.next_item = self.first_item
        new_item.prev_item = last_item
        self.first_item.prev_item = new_item
        self.size += 1

    def append_left(self, data) -> None:
        """ Appends a new item to the start of list

        Args:
            data: data of item to be added to the start
        """

        new_item = LinkedListItem(data)
        if self.first_item is None:
            self.first_item = new_item
            new_item.next_item = new_item
            new_item.prev_item = new_item
            self.size += 1
            return

        self.first_item.prev_item.next_item = new_item
        new_item.prev_item = self.first_item.prev_item
        new_item.next_item = self.first_item
        self.first_item.prev_item = new_item
        self.first_item = new_item
        self.size += 1

    def append(self, data) -> None:
        """Func alias to the append_right"""
        self.append_right(data)

    def remove(self, data) -> None:
        """ Removes an item from the list

        Args:
            data: data of item to be removed
        """

        if self.first_item is None:
            return

        current_item = self.first_item
        while True:
            if self.first_item.next_item == self.first_item:
                self.first_item = None
                self.size = 0
                return
            if current_item.data == data:
                current_item.prev_item.next_item = current_item.next_item
                current_item.next_item.prev_item = current_item.prev_item
                if current_item == self.first_item:
                    self.first_item = current_item.next_item
                    self.size -= 1
                return
            if current_item.next_item == self.first_item:
                return
            current_item = current_item.next_item

    def insert(self, previous_data, data) -> None:
        """ Inserts an item after item 'previous'

        Args:
            previous_data: Element after which the data is inserted
            data: To be inserted data
        """

        new_item = LinkedListItem(data)
        if self.first_item is None:
            return
        if self.first_item.next_item == self.first_item:
            new_item.next_item = self.first_item
            new_item.prev_item = self.first_item
            self.first_item.next_item = new_item
            self.first_item.prev_item = new_item
            self.size += 1
            return

        current_item = self.first_item
        while True:
            if current_item.data == previous_data:
                new_item.next_item = current_item.next_item
                current_item.next_item.prev_item = new_item
                current_item.next_item = new_item
                new_item.prev_item = current_item
                self.size += 1
                return
            if current_item.next_item == self.first_item:
                return
            current_item = current_item.next_item

    def last(self) -> LinkedListItem | None:
        """Returns last item"""

        if self.first_item is not None:
            return self.first_item.prev_item
        return None
