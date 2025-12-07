"""
PROJECT 3 — Tuple-Based Coordinate System

Trains tuples + looping.

Requirements:
1. Ask user for number of coordinate points
2. For each point, take input like: "x y" Convert to a tuple (x, y)
3. Store all tuples in a list
4. Print:
    - all points
    - point with largest distance from origin (0,0)
        - distance formula: sqrt(x² + y²)
    - point closest to the origin

You must use tuples for the coordinates.
"""
import math

num_points = int(input('Enter number of points: '))
points = []

for _ in range(num_points):
    x_str, y_str = input('Enter point (x y): ').split()
    x, y = int(x_str), int(y_str)
    points.append((x, y))

print('All points:')
for p in points:
    print(p)

def distance(p):
    return math.sqrt(p[0]**2 + p[1]**2)

farthest = max(points, key=distance)
closest = min(points, key=distance)

print(f'Point farthest from origin: {farthest}')
print(f'Point closest to origin: {closest}')