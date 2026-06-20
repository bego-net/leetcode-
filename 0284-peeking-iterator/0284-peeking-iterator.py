class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_val = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.next_val

    def next(self):
        val = self.next_val

        if self.iterator.hasNext():
            self.next_val = self.iterator.next()
        else:
            self.next_val = None

        return val

    def hasNext(self):
        return self.next_val is not None