class TreeNode(object):
    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, child):
        self.children.append(child)

    def is_ancestor(self, node_to_test):
        """
        Check if this node is ancestor of other.
        :param node_to_test:
        :return: True if node_to_test has children as other
        """
        if not node_to_test or not self.value:
            return False
        if self.value == node_to_test.value:
            return True
        else:
            if self.children:
                for child in self.children:
                    if child.is_ancestor(node_to_test):
                        return True
        return False
