from .interface import AbstractLinkedList
from .node import *

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        
        if elements:
            for value in elements:
                self.append(value)
       
        

    def __str__(self):
        if self is None:
            return "[]"
        else:
            result = []
            for item in self:
                result.append(item.elem)
            return "{}".format(result)

    def __len__(self):
        counter = 0
        for el in self:
            counter += 1
        return counter

    def __iter__(self):
        current = self.start
        while current:
            yield current
            current = current.next
        raise StopIteration

    def __getitem__(self, index):
        if index > len(self):
            raise IndexError
        if len(self) == 0:
            raise IndexError
        for ticker, item in enumerate(self):
            if ticker == index:
                return item.elem
            
        
        

    def __add__(self, other):
        newlist = LinkedList()
        for item in self:
            newlist.append(item.elem)
        
        for item in other:
            newlist.append(item.elem)
        return newlist

        

    def __iadd__(self, other):
        for item in other:
            self.append(item.elem)
        return self

    def __eq__(self, other):
        
        print(self)
        print(other)
        if len(self) == len(other):
            for items in zip(self, other):
                if items[0].elem != items[1].elem:
                    return False
            return True
        return False
        


    def __ne__(self, other):
        return not self.__eq__(other)
        
    def append(self, elem):
        if self.start is None:
            self.start = Node(elem)
            self.end = self.start
        else:
            new_node = Node(elem)
            self.end.next = new_node
            self.end = new_node
        
            
    def count(self):
        return len(self)

    def pop(self, index=None):
        if index is None:
            index = len(self)-1
        if index >= len(self):
            raise IndexError
        if len(self) == 0:
            raise IndexError
        
        previous = None 
        current = self.start
        ticker = 0
        while current:
            
            if ticker == index:
                if previous is None:
                    self.start = self.start.next
                    return current.elem
                
                if current.next is None:
                    previous.next = None
                    self.end = previous
                    return current.elem
                
                previous.next = current.next
                return current.elem
            ticker += 1
            previous = current
            current = current.next
            
            
            
            
            
            
