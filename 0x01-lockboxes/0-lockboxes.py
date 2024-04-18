#!/usr/bin/python3
'''
unlock all boxes
'''


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    seen_boxes = set([0])
    unvisited_boxes = set(boxes[0])
    unvisited_boxes.discard(0)
    while unvisited_boxes:
        current_box = unvisited_boxes.pop()
        if not (0 <= current_box < num_boxes) or current_box in seen_boxes:
            continue
        keys_in_current_box = boxes[current_box]
        for key in keys_in_current_box:
            if key != current_box:
                unvisited_boxes.add(key)
        seen_boxes.add(current_box)
    return num_boxes == len(seen_boxes)
