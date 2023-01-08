from abc import ABC, abstractmethod
from typing import List
from CityDataManagement.City import City


class AbstractCityHeap(ABC):
    """
    Abstract Class with the responsibility to offer the common methods of both a Min and Max heap.

    This class is divided into two parts:

    -Abstract Methods Block (Methods necessary for both a min and a max heap but with different implementations)

    -Shared Methods Block (Methods identical for both a min and a max heap)


    Param:
    ------
    rawCityData: List[City]: raw unsorted List of City Objects

    recursiv: bool: should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
    
    floyd: bool: should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.

    Hint:   
    -----
    Think of the index of all elements in the heap as an array. Array: ([0],[1],[2],[3]...)
    The root is located at index 0, so it`s children must be on Index 1 and 2 and so on...
    """

    heapStorage: List[City] = [0]  # empty List of City Objects
    maximumHeapCapacity = 0
    currentHeapLastIndex = 0  # current last Index of the Heap based on the inserted City Objects, this is also the current Size of the Heap
    rawCityData: List[City]

    recursive: bool = False
    floyd: bool = False

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        self.rawCityData = raw_city_data
        self.maximumHeapCapacity = len(self.rawCityData)  # set Maximum Heap Capacity to the amount of City Objects
        self.heapStorage = self.heapStorage * self.maximumHeapCapacity

        self.recursive = recursive
        self.floyd = floyd

        self.insert_raw_city_data_into_heap()

    # ----Abstract Methods Block (Methods necessary for both a min and a max heap but with different implementations)--

    @abstractmethod
    def heapify_up_iterative(self):
        """
        Establish heap conditions iterative upwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_up_recursive(self, index):
        """
        Establish heap conditions recursive upwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions via Floyds Heap Construction Algorithmus
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_down_iterative(self):
        """
        Establish heap conditions iterative downwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_down_recursive(self, index):
        """
        Establish heap conditions recursive downwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def remove(self):
        """
        Remove a City from the Heap.
        """
        ...
        raise NotImplementedError

    # ------Shared Methods Block (Methods identical for both a min and a max heap)------

    def insert_raw_city_data_into_heap(self):
        """
        Insertion of all cities into the Heap.
        """

        if self.floyd:
            self.build_heap_via_floyd()
        else:
            for i in self.rawCityData:
                self.insert(i)

    def insert(self, city):
        """
        Insert a single City into the Heap.
        """
        if self.heapStorage[0] == 0:
            print("Insert root")
            self.heapStorage[0] = city
            return

        # TODO: replace by is full function
        if self.currentHeapLastIndex >= self.maximumHeapCapacity - 1:
            return

        self.currentHeapLastIndex += 1
        self.heapStorage[self.currentHeapLastIndex] = city

        if self.recursive:
            self.heapify_up_recursive(self.currentHeapLastIndex)
        else:
            self.heapify_up_iterative()

    def build_heap_via_floyd(self):
        """
        Build a Heap via Floyds Heap Construction Algorithm from a unsorted List Of Cities.
        """
        self.heapStorage = self.rawCityData
        self.currentHeapLastIndex = self.maximumHeapCapacity - 1

        index = self.currentHeapLastIndex
        while 0 <= index < self.maximumHeapCapacity:
            self.heapify_floyd(index, self.maximumHeapCapacity)
            index -= 1


    def get_root_city(self):
        """
        Return the City at the Root
        """
        return self.heapStorage[0]

    def get_parent_index(self, index):
        """
        Return the index of the parent node. 
        """
        return (index - 1) // 2

    def get_left_child_index(self, index):
        """
        Return the index of the left child. 
        """
        return 2 * index + 1

    def get_right_child_index(self, index):
        """
        Return the index of the right child. 
        """
        return 2 * index + 2

    def has_parent(self, index) -> bool:
        """
        Check if the node has a parent. Return:

            True    = Has parent

            False   = No parent
        """
        parent_index = self.get_parent_index(index)
        return parent_index >= 0

    def has_left_child(self, index):
        """
        Check if the Node has a left Child. Return:

            True    = Has leftChild

            False   = No leftChild

        Hint:
        -----
        The Index of the Child can be used for this purpose.
        """
        left_child_index = self.get_left_child_index(index)
        if left_child_index > self.currentHeapLastIndex:
            return False
        else:
            return True

    def has_right_child(self, index):
        """
        Check if the Node has a right Child. Return:

            True    = Has rightChild

            False   = No rightChild

        Hint:
        -----
        The Index of the Child can be used for this purpose.
        """
        right_child_index = self.get_right_child_index(index)
        if right_child_index > self.currentHeapLastIndex:
            return False
        else:
            return True

    def has_childs(self, index):
        return self.has_left_child(index) and self.has_right_child(index)

    def get_city_population(self, index: int):
        """
        Return the Population of a City with the given index in the heap.
        """
        return self.heapStorage[index].population

    def get_parent_population(self, index):
        """
        Returns the population of the parent.

        Hint:
        -----
        We need the position of the parent in the StorageArray to extract the population from this position.
        """
        parent_index = self.get_parent_index(index)
        return self.heapStorage[parent_index].population

    def get_left_child_population(self, index):
        """
        Return of the population of the left child.

        Hint:
        -----
        We need the position of the child in the StorageArray to extract the population from this position.
        """
        left_child_index = self.get_left_child_index(index)
        return self.heapStorage[left_child_index].population

    def get_right_child_population(self, index):
        """

        Return of the population of the right child.
        Hint:
        -----
        We need the position of the child in the StorageArray to extract the population from this position.
        """
        right_child_index = self.get_right_child_index(index)
        return self.heapStorage[right_child_index].population

    def check_if_heap_is_full(self):
        """
        Check if the heap has reached its maximum capacity. Return:

            True    = Full

            False   = Not full
        """
        return self.currentHeapLastIndex == self.maximumHeapCapacity - 1

    def swap_nodes(self, first_node_index, second_node_index):
        """
        Swap two nodes specified by their index.
        """
        first_node = self.heapStorage[first_node_index]
        second_node = self.heapStorage[second_node_index]

        self.heapStorage[first_node_index] = second_node
        self.heapStorage[second_node_index] = first_node

    def get_heap_data(self) -> List[City]:
        """
        Return the sorted List of City Objects

        return
        ------
        List[City]:
        """
        return self.heapStorage
