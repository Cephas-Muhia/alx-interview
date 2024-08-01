#!/usr/bin/python3
"""
This module provides a function to determine if all lockboxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    Args:
        boxes (list): A list of lists where each sublist represents keys in a box.
        
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        key = keys.pop()
        for k in boxes[key]:
            if k < n and not opened[k]:
                opened[k] = True
                keys.append(k)

    return all(opened)

