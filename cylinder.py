#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program calculated volume of clinder

import math


def calculate_volume(radius, height):
    # This function alculated volume of clinder
    # process
    volume = round(math.pi * radius ** 2 * height, 2)

    return volume


def main():
    # this is the main function
    # this is he main function
    print("This program calculated the volume of a cylinder.")
    print("Please enter the radius and the height.")
    radius_user = input("\nThe radius is (mm) : ")
    height_user = input("The height is (mm) : ")

    try:
        radius_user = float(radius_user)
        height_user = float(height_user)
        # call functions
        volume = calculate_volume(radius_user, height_user)
        print(
            "\nThe volume of a cylinder with a radius {0} mm and a height of {1} mm {2} mm³.".format(
                radius_user, height_user, volume
            )
        )
    except (Exception):
        print("Invalid input")

    print("\nDone.")


if __name__ == "__main__":
    main()
