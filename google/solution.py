from itertools import combinations


def max_rectangle_area(points):
    # Convert points to a set for O(1) lookup
    point_set = set(map(tuple, points))
    max_area = 0
    print(point_set)

    # Iterate over every pair of points
    for (x1, y1), (x2, y2) in combinations(points, 2):
        if x1 != x2 and y1 != y2:
            # Check if the other two points exist
            if (x1, y2) in point_set and (x2, y1) in point_set:
                # Calculate the area of the rectangle
                area = abs(x2 - x1) * abs(y2 - y1)
                max_area = max(max_area, area)

    return max_area


# List of points
points = [
    [2, 1],
    [8, 1],
    [2, 4],
    [8, 4],
    [-8, 1],
    [2, -2],
    [-8, -2],
    [-2, 8],
    [3, 3],
    [-7, 3],
    [-2, -2],
    [2, 6],
    [-6, 0],
]

# Find the maximum rectangle area
max_area = max_rectangle_area(points)
print(f"The largest rectangle area is: {max_area}")
