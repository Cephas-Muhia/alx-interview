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
    opened = [False] * n  # Keep track of which boxes are opened
    opened[0] = True  # The first box is already open
    keys = [0]  # Start with the key to the first box

    while keys:
        key = keys.pop()  # Take the last key you found
        for k in boxes[key]:  # Look at all keys in the current box
            if k < n and not opened[k]:  # If the key opens a box we haven't opened yet
                opened[k] = True  # Mark that box as opened
                keys.append(k)  # Add the key to our list of keys

    return all(opened)  # If all boxes are opened, return True

