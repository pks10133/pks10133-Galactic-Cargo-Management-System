from bin import Bin
from object import Object, Color
from avl import AVLTree
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        self.bins = AVLTree()  # AVL tree for bins, sorted by ID
        self.objects = AVLTree()      # AVLTree for object, sorted by ID
        self.bins_byID = AVLTree()  # AVLTree for fast access by bin_id

    def add_bin(self, bin_id, capacity):
        bin_add =  Bin(bin_id, capacity)
        self.bins.insert(capacity, bin_add)
        self.bins_byID.insert(bin_id, bin_add)

    def add_object(self, object_id, size, color):
        best_bin_id = None
        best_bin = None

        
        if color in [Color.BLUE, Color.YELLOW]:
            # Find the largest bin that can fit the object
            best_bins_Tree = AVLTree()
            best_bins = self._smallest_fit(size)
            if not best_bins:
               raise NoBinFoundException()
            for bin in best_bins:
                best_bins_Tree.insert(bin.bin_id, bin)  
            
            if color == Color.BLUE:
                best_bin = best_bins_Tree.find_min()   # Least id
              
            else:  #Colour is Yellow
                best_bin = best_bins_Tree.find_max()   # Greatest id
                
                    
        elif color in [Color.RED, Color.GREEN]:
            # Find the smallest bin that can fit the object
            best_bins_Tree = AVLTree()
            best_bins = self.find_largest_fit(size)
            if not best_bins:
               raise NoBinFoundException()
            
            for bin in best_bins:
                best_bins_Tree.insert(bin.bin_id, bin)   

            if color == Color.RED:  
                best_bin = best_bins_Tree.find_min()   # Least id

            else:  #Colour is Green
                best_bin = best_bins_Tree.find_max()   # Greatest id
                
                
                    

        if best_bin is None:
                    raise NoBinFoundException()
        
        best_bin_id = best_bin.bin_id

        if best_bin:
                # Access the node associated with the bin's capacity in bins tree
                bin_node = self.bins.find_node(best_bin.capacity)

        if bin_node:
            # Note the remaining bins other than best_bin
            remaining_bins = [b for b in bin_node.values if b.bin_id != best_bin_id]

            # Remove the best_bin from the bin_node's values
            self.bins.delete(best_bin.capacity)  # Remove capacity node from the bins tree

            # If there are remaining bins, reinsert them one by one
            for remaining_bin in remaining_bins:
                self.bins.insert(best_bin.capacity, remaining_bin)

        # Add the object to the selected bin
        best_bin.add_object(size, object_id)

        # Reinsert with the updated capacity to keep bins tree balanced
        self.bins.insert(best_bin.capacity, best_bin)  


        # Store object_id in the AVL tree, with bin_id as the value
        self.objects.insert(object_id, best_bin_id)
            


        
    def _largest_fit(self, node, size, best_fit=None, best_cap = None):
    
        while node is not None:
            if node.key >= size:
                # If the current node's key fits, consider it and move to the left subtree
                best_fit = node.values  # Update best_fit to current node's values
                node = node.right
            else:
                # Otherwise, move right to find bins that can fit
                node = node.right

        return best_fit
    
    

    # Wrapper function to initiate the recursion from the root node
    def find_largest_fit(self, size):

        return self._largest_fit(self.bins.root, size)


    
        
        

    def _smallest_fit(self, size):
        # Start searching from the root of the AVL tree
        node = self.bins.root
        best_fit = None

        while node is not None:
            if node.key >= size:
                # If the current node's key fits, consider it and move to the left subtree
                best_fit = node.values  # Update best_fit to current node's values
                node = node.left
            else:
                # Otherwise, move right to find bins that can fit
                node = node.right

        return best_fit

     
    def delete_object(self, object_id):
        # Find the bin where the object is stored
        bin_id = self.objects.find(object_id)
        if  bin_id == None :
            return
        
        # Find the bin from the bins_byID tree
        bin = self.bins_byID.find(bin_id)

        if bin:
            # Access the node associated with the bin's capacity in bins tree
            bin_node = self.bins.find_node(bin.capacity)
    
        if bin_node:
            # Note the remaining bins other than best_bin
            remaining_bins = [b for b in bin_node.values if b.bin_id != bin_id]

            # Remove the best_bin from the bin_node's values
            self.bins.delete(bin.capacity)  # Remove capacity node from the bins tree

            # If there are remaining bins, reinsert them one by one
            for remaining_bin in remaining_bins:
                self.bins.insert(bin.capacity, remaining_bin)

            # Add the object to the selected bin
        bin.remove_object(object_id)

         # Reinsert with the updated capacity to keep bins tree balanced
        self.bins.insert(bin.capacity, bin)  # Insert the bin for its new capacity

        self.objects.delete(object_id)
        

    def object_info(self, object_id):
        # Find the bin ID for the given object ID
        bin_id = self.objects.find(object_id)
        if bin_id is None:
            return None
        return bin_id
   


    def bin_info(self, bin_id):
        bin = self.bins_byID.find(bin_id)
        if bin is None:
            return None
        return bin.get_capacity_info()


