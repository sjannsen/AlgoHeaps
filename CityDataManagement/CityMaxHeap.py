from typing import List
from CityDataManagement.City import City
from CityDataManagement.AbstractCityHeap import AbstractCityHeap


class CityMaxHeap(AbstractCityHeap):
    """
    Class with the responsibility to create a Max-Heap-structure based on unstructured data.
    (Every Parents Key must be greater than its children Key)

    """

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        """
        Creation of a Max-City-Heap.

        :param raw_city_data:    A unsorted List of Cities
        :param recursive:    Should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
        :param floyd:       Should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.
                            For removal the approach specified in :param recursiv will be used.
        """
        super().__init__(raw_city_data, recursive, floyd)

    def heapify_up_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative upwards.
        """
        current_index = self.currentHeapLastIndex

        while self.has_parent(current_index) and self.get_city_population(current_index) > self.get_parent_population(
                current_index):
            parent_index = self.get_parent_index(current_index)
            self.swap_nodes(current_index, parent_index)
            current_index = parent_index

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        if index > 0:
            if self.get_city_population(index) > self.get_parent_population(index):
                parent_index = self.get_parent_index(index)
                self.swap_nodes(index, parent_index)
                self.heapify_up_recursive(parent_index)

    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions for a Max-Heap via Floyds Heap Construction Algorithmus.
        
        """
        if self.currentHeapLastIndex < index or index < 0:
            return

        if self.has_right_child(index) or self.has_left_child(index):

            if self.has_childs(index):
                if self.get_left_child_population(index) < self.get_right_child_population(index):
                    largest_child_index = self.get_right_child_index(index)
                else:
                    largest_child_index = self.get_left_child_index(index)

                if self.get_city_population(index) < self.get_city_population(largest_child_index):
                    self.swap_nodes(index, largest_child_index)
                    self.heapify_floyd(largest_child_index, amount_of_cities)

            elif self.has_left_child(index):
                if self.get_city_population(index) < self.get_left_child_population(index):
                    left_child_index = self.get_left_child_index(index)
                    self.swap_nodes(index, left_child_index)
                    self.heapify_floyd(left_child_index, amount_of_cities)

            else:
                if self.get_city_population(index) < self.get_right_child_population(index):
                    right_child_index = self.get_right_child_index(index)
                    self.swap_nodes(index, right_child_index)
                    self.heapify_floyd(right_child_index, amount_of_cities)

    def heapify_down_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        index = 0

        while self.has_left_child(index) or self.has_right_child(index):

            if self.has_childs(index):
                if self.get_left_child_population(index) < self.get_right_child_population(index):
                    largest_child_index = self.get_right_child_index(index)
                else:
                    largest_child_index = self.get_left_child_index(index)

                if self.get_city_population(index) < self.get_city_population(largest_child_index):
                    self.swap_nodes(index, largest_child_index)
                    index = largest_child_index

            if self.has_left_child(index) and self.get_city_population(index) < self.get_left_child_population(index):
                left_child_index = self.get_left_child_index(index)
                self.swap_nodes(index, left_child_index)
                index = left_child_index

            elif self.has_right_child(index) and self.get_city_population(index) < self.get_right_child_population(
                    index):
                right_child_index = self.get_right_child_index(index)
                self.swap_nodes(index, right_child_index)
                index = right_child_index

    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        if self.has_right_child(index) or self.has_right_child(index):

            if self.has_childs(index):
                if self.get_left_child_population(index) < self.get_right_child_population(index):
                    largest_child_index = self.get_right_child_index(index)
                else:
                    largest_child_index = self.get_left_child_index(index)
                if self.get_city_population(index) < self.get_city_population(largest_child_index):
                    self.swap_nodes(index, largest_child_index)
                    self.heapify_down_recursive(largest_child_index)

            if self.has_left_child(index) and self.get_city_population(index) < self.get_left_child_population(index):
                left_child_index = self.get_left_child_index(index)
                self.swap_nodes(index, left_child_index)
                self.heapify_down_recursive(left_child_index)

            if self.has_right_child(index) and self.get_city_population(index) < self.get_right_child_population(index):
                right_child_index = self.get_right_child_index(index)
                self.swap_nodes(index, right_child_index)
                self.heapify_down_recursive(right_child_index)

    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        city_to_be_removed = self.heapStorage[0]

        self.heapStorage[0] = self.heapStorage[self.currentHeapLastIndex]
        self.heapStorage[self.currentHeapLastIndex] = 0
        self.currentHeapLastIndex -= 1

        if self.recursive:
            self.heapify_down_recursive(0)

        else:
            self.heapify_down_iterative()

        return city_to_be_removed
