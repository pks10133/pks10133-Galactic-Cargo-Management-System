


from avl import AVLTree
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.objects = AVLTree()  # Use AVL tree to store objects (key = id, value = size)

    def add_object(self, size, obj_id):
        # Check if there is enough capacity to add the object
        if self.capacity >= size:
            self.objects.insert(obj_id, size)
            self.capacity -= size
        else:
            print("Not enough capacity to add the object.")

    def remove_object(self, obj_id):
        # Find the object size using the AVL tree
        size = self.objects.find(obj_id)
        if size is not None:
            self.objects.delete(obj_id)
            self.capacity += size
        else:
            print(f"Object with ID {obj_id} not found.")

    def get_capacity_info(self):
        # Print current capacity and keys (object IDs)
        return (self.capacity, self._get_all_keys(self.objects.root))

    def _get_all_keys(self, node):
        # This is an in-order traversal to get all keys (object IDs) from the AVL tree
        if not node:
            return []
        return self._get_all_keys(node.left) + [node.key] + self._get_all_keys(node.right)
