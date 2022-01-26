def move_rectangle2(rect, dx, dy):
    """Takes a rectangle object rect, returns a new rectangle object moved
    by adding dx to x coordinate, and dy to the y coordinate of rect.corner"""
    import copy
    newRect = copy.deepcopy(rect)
    newRect.corner.x += dx
    newRect.corner.y += dy
    return None
