class Node:

    def __init__(self, data, ind):

        self.left = None
        self.right = None
        self.data = data
        self.ind = ind

    def insert(self, data, ind):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, ind)
                else:
                    self.left.insert(data, ind)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, ind)
                else:
                    self.right.insert(data, ind)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return -1
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return int(lkpval) - 1
            return self.right.findval(lkpval)
        else:
            return int(self.ind)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
