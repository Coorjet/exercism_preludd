class Node:
    def __init__(self, value, succeeding=None, previous=None):

        self.value = value
        self.previous = previous
        self.succeeding = succeeding


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, value):
        newNode = Node(value, None, self.last)

        if self.last:
            self.last.succeeding = newNode
        self.last = newNode

        if not self.first:
            self.first = self.last
       
    def pop(self):

       poppedVal = self.last.value
       self.last =  self.last.previous
       if self.last:
           self.last.succeeding = None
       else:
           self.first = None
       return poppedVal

    def shift(self):
        shiftedVal = self.first.value
        self.first = self.first.succeeding
        if self.first:
            self.first.previous = None
        else:
            self.last = None
        return shiftedVal


    def unshift(self, value):

        newNode = Node(value, self.first, None)
        if self.first:
            self.first.previous = newNode
        self.first = newNode
        if not self.last:
            self.last = self.first