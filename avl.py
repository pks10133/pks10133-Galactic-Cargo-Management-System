from node import Node

class AVLTree:
    def __init__(self):
        self.root = None  
    

    def insert(self, key, value):
        if not self.root:
            self.root = Node(key, value)
        else:
            self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return Node(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value) 
        else:# key already exists
            node.value = value
            node.values.append(value)
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    # def find(self, key):
    #     return self._find(self.root, key)

    # def _find(self, node, key):
    #     if not node:
    #         return None
    #     if key < node.key:
    #         return self._find(node.left, key)
    #     elif key > node.key:
    #         return self._find(node.right, key)
    #     else:
    #         return node.value

    def find_node(self, key):
        return self._find_node(self.root, key)

    def _find_node(self, node, key):
        if not node:
            return None
        if key < node.key:
            return self._find_node(node.left, key)
        elif key > node.key:
            return self._find_node(node.right, key)
        else:
            return node  # Return the entire node, not just its value

    # Your existing find method for just the value
    def find(self, key):
        node = self.find_node(key)
        return node.value if node else None

    def delete(self, key):
        if self.root:
            self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.values = temp.values
            node.right = self._delete(node.right, temp.key)
        if not node:
            return node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._get_balance(node)
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _min_value_node(self, node):
        if node.left is None:
            return node
        return self._min_value_node(node.left)
    

    def find_min(self):
        if not self.root:
            return None  # Tree is empty
        return self._min_value_nodeV(self.root).value  # Start from the root and return the value

    def _min_value_nodeV(self, node):
        while node.left:  # Keep going left until you find the minimum
            node = node.left
        return node  # Return the minimum node itself

    def find_max(self):
        if not self.root:
            return None  # Tree is empty
        return self._max_value_node(self.root).value  # Start from the root and return the value

    def _max_value_node(self, node):
        while node.right:  # Keep going right until you find the maximum
            node = node.right
        return node  # Return the maximum node itself


    def traversal(self, node):
        # This is an in-order traversal to get all keys (object IDs) from the AVL tree
        if not node:
            return []
        return self.traversal(node.left) + [node.key] + self.traversal(node.right)
