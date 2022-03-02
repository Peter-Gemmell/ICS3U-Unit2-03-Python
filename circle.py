#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program calculates the circumference of a circle using constants

import constant


def main():
    # this function calculates the circumference of circle w/constants
    # input
    radius = int(input("Enter radius of a circle (mm): "))

    # process
    circumference = constant.TAU * radius

    # output
    print("Circumference is {} mm².".format(circumference))
    print("\nFinished.")


if __name__ == "__main__":
    main()
