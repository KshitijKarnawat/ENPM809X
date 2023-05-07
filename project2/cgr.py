#!/usr/bin/env python3

"""
/**
 * @file    kshitij_proj2.py
 * @author  Kshitij Karnawat (kshitij@umd.edu)
 * @brief   Implementation of Contact Graph Routing using Dijkstra's Algorithm and Heaps
 * @version 1.0
 * @date    2023-05-04
 *
 * @copyright Copyright (c) 2023
 *
 */
"""

import numpy as np
import heapq

class Contact:
    """
    Class Contact: A Class that defines the contacts in a contact graph
    """
    def __init__(self, id, start_time, end_time, source, destination, owlt):
        """
        Initialize a new Contact object.

        Args:
            id (int): The ID of the contact.
            start_time (float): The start time of the contact.
            end_time (float): The end time of the contact.
            sender (int): The ID of the sender.
            receiver (int): The ID of the receiver.
            owlt (float): The one-way light time between the sender and receiver.
        """
        self.id = id
        self.start_time = float(start_time)
        self.end_time = float(end_time)
        self.source = int(source)
        self.destination = int(destination)
        self.owlt = float(owlt)
        self.visited = False    
        self.arrival_time = np.inf
        self.visited_n = set()
        self.predecessor = None

    def __lt__(self, second):
        """
        Compare two Contact objects based on their arrival times.

        This method is used to define the ordering of elements in the min_heap.

        Args:
            other (Contact): The other Contact object to compare to.

        Returns:
            bool: True if this Contact has an earlier arrival time than the other Contact, False otherwise.
        """
        return self.arrival_time < second.arrival_time


def CGR(graph, c_root, c_dest):
    """
    Compute the Contact Graph Routing path and bounded delay time between two Contacts.

    Args:
        G (list): The list of Contact objects in the graph.
        c_root (Contact): The Contact object representing the source node.
        c_dest (Contact): The Contact object representing the destination node.

    Returns:
        tuple: A tuple containing the list of Contact IDs representing the path from c_root to c_dest, and the bounded
               delay time of the path.
    """

    # Set root arrival_time to 0 as mentioned in Earliest Time Problem 
    c_root.arrival_time = 0
    
    # Set to an arbitrary large value
    bdt = np.inf
    c_fin = None
    c_curr = c_root

    # The required path to travel from node #1 to node #12
    path = []
    
    while True:
        # Added destination to function call as it is required in a condition
        c_fin, bdt = CRP(graph, c_curr, c_fin, bdt, c_dest)
        c_curr = CSP(graph, bdt)
    
        if c_curr is None:
            break
    
    # Backtracking of contact id's
    if c_fin is not None:
        contact = c_fin

        while contact != c_root:
            path.append(contact.id)
            contact = contact.predecessor
   
    return path, bdt


def CRP(graph, c_curr, c_fin, bdt, destination):
    """
    Function to perform the Contact Relay Phase (CRP) of the CGR algorithm.

    Parameters:
        G (list): A list of Contact objects representing the contact graph.
        c_curr (Contact): The current contact object.
        c_fin (Contact): The current best candidate for the destination contact object.
        bdt (float): The current best delivery time for the message.
        destination (Contact): The destination contact object.

    Returns:
        c_fin (Contact): The updated best candidate for the destination contact object.
        bdt (float): The updated best delivery time for the message.
    """
    min_heap = []
    for contact in graph:
        # Skip c if any of the conditions are True
        if ((contact.source != c_curr.destination) or (contact.end_time < c_curr.arrival_time) or (contact.visited) or ((c_curr.visited_n) and (contact.destination in c_curr.visited_n))):
            continue
        
        # Set arrival time as current contact arrival + owlt (delay) time
        if (contact.start_time < c_curr.arrival_time):
            arrival_time = c_curr.arrival_time + contact.owlt

        # Set arrival time as contact arrival + owlt (delay) time
        else:
            arrival_time = contact.start_time + contact.owlt

        # If new arrival time is less than contact arrival time update contact arrival time and visited nodes
        if (arrival_time < contact.arrival_time):
            contact.arrival_time = arrival_time
            contact.predecessor = c_curr
            contact.visited_n = c_curr.visited_n.union({contact.destination})
            
            # Update best time if arrival time is less than best time
            if (contact.destination == destination.source) and (contact.arrival_time < bdt):
                bdt = contact.arrival_time
                c_fin = contact

            heapq.heappush(min_heap, (contact.arrival_time, contact))

    c_curr.visited = True
    
    while len(min_heap) != 0:
        _, contact = heapq.heappop(min_heap)

        # If contact is unvisited call CRP recursively
        if not contact.visited:
            return CRP(graph, contact, c_fin, bdt, destination)
    
    return c_fin, bdt


def CSP(graph, bdt):
    """
    Function to perform the Contact Selection Phase (CSP) of the CGR algorithm using a min_heap.

    Parameters:
        G (list): A list of Contact objects representing the contact graph.
        bdt (float): The current best delivery time for the message.

    Returns:
        c_curr (Contact): Root of min_heap
    """

    # Heap implementation to find the nearest contact
    min_heap = []
    for contact in graph:
        if (contact.arrival_time > bdt) or contact.visited:
            continue

        heapq.heappush(min_heap, contact)

    if len(min_heap) != 0:
        return heapq.heappop(min_heap)
    else:
        return None


def main():
    graph = [Contact(0, 0, np.inf, 1, 1, 0)]
    filename = "ContactList.txt"

    # Read file, create and store contacts
    with open(filename) as f:
        for line in f:
            id, start_time, end_time, source, destination, owlt = line.split()
            contact = Contact(id, start_time, end_time, source, destination, owlt)
            graph.append(contact)
            
    # Change these values from 0 to 190 to start from any contact and end at a node with end contact's id
    start_id = 0
    end_id = 190

    # CGR Start
    path, bdt = CGR(graph, graph[start_id], graph[end_id])
    
    # Reverse path
    path = path[::-1]

    print("Path:",path)
    print("Arrival Time:",bdt)

if __name__ == '__main__':
    main()
