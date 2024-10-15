# pks10133-Galactic-Cargo-Management-System

Project Overview
The Galactic Cargo Management System (GCMS) is designed to address the challenges faced by interstellar shipping companies in efficiently managing and packing cargo into space cargo bins. In the vast expanse of the galaxy, each cargo bin has a specific capacity, and shipments vary in sizes and colors. Proper cargo management is essential for smooth operations and to avoid costly delays. The GCMS assigns unique integer IDs to both bins and objects, handling cargo based on color to implement specific packing algorithms.

Background
In the GCMS, cargo is categorized by color, which dictates the handling algorithm to be used for packing. The system implements two primary algorithms for packing cargo based on color:

    Compact Fit Algorithm:
        Blue Cargo (Compact Fit, Least ID): Assigns cargo to the bin with the smallest remaining capacity sufficient to hold the item. If multiple bins qualify, the one with the least ID is chosen.
        Yellow Cargo (Compact Fit, Greatest ID): Similar to blue cargo but selects the bin with the greatest ID in case of ties.

    Largest Fit Algorithm:
        Red Cargo (Largest Fit, Least ID): Assigns cargo to the bin with the largest remaining capacity. If multiple bins have the same capacity, the one with the least ID is selected.
        Green Cargo (Largest Fit, Greatest ID): Uses the same algorithm but prefers the bin with the greatest ID when there are ties.

Modeling
The system is designed to manage n bins, each with an integer capacity and ID, along with m objects, each having a size, ID, and color. The algorithms used to manage the cargo are as follows:

    Largest Fit Algorithm: This well-known approach selects the bin with the largest remaining capacity when adding an object. The implementation uses variable names ending with _lfa.

    Compact Fit Algorithm: This algorithm selects the bin with the smallest remaining capacity that can accommodate the object being added. The implementation uses variable names ending with _cfa.

Requirements
The GCMS includes the following functionalities:

    add_bin(bin_id, capacity): Adds a new bin with the specified ID and capacity.
    add_object(object_id, size, color): Adds a new object with the specified ID, size, and color, utilizing the appropriate algorithm based on the color.
    delete_object(object_id): Deletes the specified object from its assigned bin.
    object_info(object_id): Prints the ID of the bin where the object is placed.
    bin_info(bin_id): Returns a tuple with the remaining capacity of the bin and a list of object IDs stored in the bin.

Technical Specifications

    Programming Language: Python
    Constraints:
        No use of dictionaries or sets; internal data structures must be implemented from scratch.
        Space complexity of O(n + m) and time complexity of O(log(n) + log(m)) for specific functions.
