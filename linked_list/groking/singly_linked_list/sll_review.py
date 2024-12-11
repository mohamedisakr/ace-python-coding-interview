"""Module providing an implementation for singly-linked list."""
from __future__ import annotations
import copy
from typing import Any, Callable, List, Optional


class SinglyLinkedList:
    """
    This class models a singly-linked list data structure.

    A singly-linked list consists of nodes where each node has a reference 
    to the next node in the list.

    Functionality:

    - Stores nodes containing arbitrary data.
    - Supports common linked list operations like insertion, deletion search and traversal.
    """

    class Node:
        """
        A node in a singly linked list. Each node contains data and 
        a reference to the next node.

        Attributes:

            data: The data held in the node. Can be any arbitrary object.
            _next: A reference to the next node in the list.
        """

        def __init__(self, data: Any, next_node: SinglyLinkedList.Node = None) -> None:
            """
            Initialize a new Node object.

            Parameters:

            - data (Any): The data for the node. Can be any arbitrary object.
            - next_node (Node, optional): The next Node in the list. Defaults to None.            
            """
            pass

        def __str__(self) -> str:
            """
            Return a string representation of the node's data.

            Parameters:
                None

            Returns:
                str: String representation of the node's data.
            """

            pass

        def __repr__(self) -> str:
            """
            Return a string (internal) representation of the node's data.

            Parameters:
                None

            Returns:
                str: String representation of the node's data.
            """

            pass

        def data(self) -> Any:
            """
            Get the data stored in this node.

            Parameters:
                None

            Returns:
                Any: The data stored in this node. Can be any arbitrary object.
            """

            pass

        def next(self) -> SinglyLinkedList.Node:
            """
            Return the successor of the current node.

            Parameters:
                None

            Returns:
                Node: The next node in the singly-linked list.
            """

            pass

        def has_next(self) -> bool:
            """
            Check if the node has a successor.

            Parameters:
                None

            Returns:
                bool: True if the node has a next node, False otherwise.
            """

            pass

        def append(self, next_node: Optional[SinglyLinkedList.Node]) -> None:
            """
            Append a node to the current one.

            Parameters:
            next_node (Optional[Node]): The node to append after the current node, or
                                        `None` to indicate no successor.
            """

            pass

    # --- SinglyLinkedList methods ---

    def __init__(self) -> None:
        """
        Initialize a new empty SinglyLinkedList.

        Parameters:
            None

        Attributes:
            _head (Node): The head node of the list. Initialized to None.
        """

        pass

    def __len__(self):
        """
        Return the length of the linked list.

        Parameters:
            None

        Returns:
            int: The number of nodes in the linked list.
        """

        pass

    def __repr__(self) -> str:
        """
        Return the string (internal) representation of the linked list.

        Parameters:
            None

        Returns:
            str: The string representation of the linked list nodes.
        """

        pass

    def __str__(self) -> str:
        """
        Return the string representation of the linked list.

        Parameters:
            None

        Returns:
            str: The string representation of the linked list nodes.

        Functionality:
            Traverses the linked list using the traverse() method, 
            passing in repr() to convert each node to a string.
            Joins the node string representations with '->' and returns the result.
        """

        pass

    def __iter__(self):
        '''
        Iterate over the values in the linked list.

        Parameters:
            None

        Functionality:
            Iterates over the values in the linked list. The iteration starts at the beginning
            of the list and goes on until it reaches the tail of the list.
        '''

        pass

    def size(self) -> int:
        """
        Return the length of the linked list.

        Parameters:
            None

        Returns:
            int: The number of nodes in the linked list.
        """

        pass

    def is_empty(self) -> bool:
        """
        Check if the linked list is empty.

        Parameters:
            None

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """

        pass

    def insert_in_front(self, data: Any) -> None:
        """
        Add a node to the beginning of the list.

        Parameters:
        - data (Any): The data for the new node to add.
        """

        pass

    def insert_to_back(self, data: Any) -> None:
        """
        Append a node to the end of the list.

        Parameters:
        - data (Any): The data for the new node to append.

        Warning: this method requires traversing a linear number (O(n))
        of nodes.
        """

        pass

    def get(self, index):
        """
        Get the data at the given index.

        Parameters:
            index (int): The index of the element to retrieve, starting from the head of the list.

        Returns:
            Any: A deep copy of the data at the given index if found.

        Error Handling:
            Raising an IndexError if index is invalid.
        """
        pass

    def traverse(self, functor: Callable[..., Any]) -> List[Any]:
        """
        Traverse the linked list and apply a function to each node's data.

        Parameters:
            functor (Callable): The function (or functor) to apply to each node's data.

        Returns:
            List[Any]: A list containing the result of applying the function 
                    to each node's data.
        """

        pass

    def _search(self, target: Any) -> Optional[SinglyLinkedList.Node]:
        """
        Search the list for a node with the data matching `target`, and return the node found.

        Parameters:
        - target (Any): The data to search for in the list.

        Returns:
        - Optional[Node]: The node containing the target data if found, 
                            otherwise None.
        """
        pass

    def search(self, predicate:  Callable[..., Any]) -> Optional[Any]:
        """
        Search the list for the first node whose data matches the predicate function.

        Parameters:
            predicate (Callable): The predicate function to evaluate node data against.
                                Should accept a single parameter for the node data.

        Returns:
            Optional[Any]: The first element for which predicate(element) is True, 
                        or None if no match is found.
        """
        pass

    def delete(self, target: Any) -> None:
        """
        Delete the first node with the given data from the list.

        Parameters:
            target (Any): The data value to delete from the list.

        Returns:
            None

        Error Handling:
            If no match is found after full traversal, raises a ValueError.
        """

        pass

    def delete_from_front(self) -> Any:
        """
        Delete the first node in the list and return the data it held.

        Parameters:
            None

        Returns:
            The data held by the node that was deleted from the front.

        Error Handling:
            If the list is empty, raises a ValueError.
        """

        pass
