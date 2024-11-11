class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked_value = None
    def peek(self):
        if self.peeked_value is None:
            if self.iterator.hasNext():
                self.peeked_value = self.iterator.next()
        return self.peeked_value
    def next(self):
        if self.peeked_value is not None:
            next_value = self.peeked_value
            self.peeked_value = None
            return next_value
        else:
            return self.iterator.next()
    def hasNext(self):
        return self.peeked_value is not None or self.iterator.hasNext()