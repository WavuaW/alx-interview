#!/usr/bin/python3
"""
Module for lockboxes task
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists. Each box is numbered sequentially from
        0 to n - 1 and each box may contain keys to the other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if not unlocked[key]:
            unlocked[key] = True
            keys.update(boxes[key])
    
    return all(unlocked)
