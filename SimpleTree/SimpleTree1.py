# https://skillsmart.ru/algo/15-121-cm/z9h53ee284.html

class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:
    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is not None:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode
        else:
            self.Root = NewChild

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)

    def GetAllNodes(self):
        # ~ O(n^2)
        nodes = []
        if self.Root is not None:
            nodes = [self.Root]
            for i in nodes:
                for j in i.Children:
                    nodes.append(j)
        return nodes

    def FindNodesByValue(self, val):
        nodes = []
        if self.Root is not None:
            for node in self.GetAllNodes():
                if node.NodeValue == val:
                    nodes.append(node)
        return nodes
    
    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode.Parent is not None:
            self.DeleteNode(OriginalNode)
            OriginalNode.Parent = NewParent
            NewParent.Children.append(OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        count = 0
        for i in self.GetAllNodes():
            if not len(i.Children):
                count += 1
        return count

    def NodeLevel(self, node):
        lvl = 0
        while node.Parent is not None:
            lvl = node.Parent
            count += 1
        return lvl
