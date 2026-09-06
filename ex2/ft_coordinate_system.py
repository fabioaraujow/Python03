#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        get_data = input("Enter new coordinates as floats in format 'x,y,y': ")
        split_pos = get_data.split(",")
        try:
            a, b, c = split_pos
        except ValueError:
            print("Invalid Syntax")
            continue
        coords = []
        current = ""
        try:
            for current in split_pos:
                coords.append(float(current.strip()))
            x, y, z = coords
            return (x, y, z)
        except ValueError as err:
            print(f"Error on parameter '{current.strip()}': {err}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: x = {first_pos}")
    print(f"It includes: X={first_pos[0]}, "
          f"Y={first_pos[1]}, Z={first_pos[2]}")
    pos_a = math.sqrt(((first_pos[0])**2)
                      + ((first_pos[1])**2)
                      + (first_pos[2]**2))
    print(f"Distance to center: {pos_a}")
    print("Get a second set of coordinates")
    sec_pos = get_player_pos()
    pos_b = math.sqrt(((sec_pos[0] - first_pos[0])**2)
                      + ((sec_pos[1] - first_pos[1])**2)
                      + ((sec_pos[2] - first_pos[2])**2))
    print(f"Distance between the 2 sets of coordinates: {pos_b:.4f}")
