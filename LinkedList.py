class Vertex:
    """Vertex class.
    
    Сontains two variables:
        data == vertex value
        nextdata == pointer to next element
    """
    
    def __init__(self, data, nextdata = None):
        self.data = data
        self.nextdata = nextdata

class LinkedList: 
    """Linked list class.
    
    Сontains:
        search(item) - search element (!) by value (!)
        insertHead(item) - insert vertex at the beginning of the list
        insertTail(item) - insert vertex at the end of the list
        insertMiddle(middle, item) - insert vertex at the middle of the list
        delete(item) - remove vertex from the list (!) by value (!)
        updateData(item, updateItem) - update vertex value
    """
    
    def __init__(self):
        self.head = None
        self.lenght = 0
                
    def __str__(self):
        node = self.head
        inv = ''
        ind = 1
        
        while node is not None:
            inv += ' '.join([str(ind), ':', str(node.data), '\n'])
            node = node.nextdata
            ind += 1
        return inv
    
    def search(self, item):
        """Search element (!) by value (!)
        
        Keyword arguments:
            item - vertex value to find
        
        Return string that contains information about the index and value of the vertex else 'unknown'
        """
        
        ind = 1
        node = self.head
        
        while node is not None:
            if node.data is item:
                return ' '.join([str(ind), ': ', str(node.data)])
            node = node.nextdata
            ind += 1
        return 'unknown'
    
    def insertHead(self, item):
        """Insert vertex at the beginning of the list
        
        Keyword arguments:
            item - value to add to the beginning of the list
        """
        
        self.head = Vertex(item, self.head)
        self.lenght += 1
    
    def insertTail(self, item):
        """Insert vertex at the end of the list
        
        Keyword arguments:
            item - value to add to the end of the list
        """
        
        node = Vertex(item)
        
        if self.head is None:
            self.head = node
            self.lenght += 1
            return
        last = self.head
       
        while last.nextdata is not None:
            last = last.nextdata
        last.nextdata = node
        self.lenght += 1
    
    def insertMiddle(self, middle, item):
        """Insert vertex at the end of the list
        
        Keyword arguments:
            middle - vertex value after which to insert a new vertex
            item - value to add to the end of the list
        
        Return 'unknown middle' if the vertex with the "middle"-value is not in the list
        """
        
        if self.search(middle) != 'unknown':
            node = self.head
            
            while node is not None:
                if node.data is middle and node.nextdata is not None:
                    newnode = Vertex(item)
                    newnode.nextdata = node.nextdata
                    node.nextdata = newnode
                    break
                elif node.data is middle and node.nextdata is None:
                    self.insertAtEnd(item)
                    print(' '.join([str(middle), 'was last item, ', str(item), 'append at the end of list.']))
                    break
                
                node = node.nextdata
            return 
        else:
            return ' '.join([self.search(middle), 'middle'])
            
    def delete(self, item):    
        """Remove vertex from the list (!) by value (!)
        
        Keyword arguments:
            item - vertex value to removing from the list
        
        Return 'unknown item' if the vertex with the "item"-value is not in the list
        """
        
        if self.search(item) != 'unknown':
            node = Vertex(None, self.head)
            prev, curr = node, node.nextdata
            
            # Removing first vertex of the list 
            if (curr is not None):
                if (curr.data is item):
                    self.head = curr.nextdata
                    curr = None
                    return 
            
            # Removing second and more vertex of the list 
            while flag is True:
                if curr.data is item:
                    prev.nextdata = curr.nextdata
                    curr.nextdata = None
                    return
            
                prev, curr = curr, curr.nextdata
        else:
            return ' '.join([self.search(middle), 'item'])
    
    def updateData(self, item, updateItem):
        """Update vertex value
        
        Keyword arguments:
            item - new vertex value
            updateItem - vertex value to updating
        
        Return 'unknown item' if the vertex with the "item"-value is not in the list
        """
        
        if self.search(item) != 'unknown':
            node = self.head
            
            while node is not None:
                if node.data is item:
                    node.data = updateItem
                    break
                    
                node = node.nextdata
            return
        else:
            return ' '.join([self.search(middle), 'item'])