#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a program to calculate the area and the perimeter of a rectangle

import math


def main():
    width = input("Enter the width of the rectangle")
    length = input("Enter the length of the rectangle")
    area = (int(width)*int(length))
    perimeter = (2*(int(length)+int(width)))
    print("The area is {}mm²".format(area))
    print("The perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
