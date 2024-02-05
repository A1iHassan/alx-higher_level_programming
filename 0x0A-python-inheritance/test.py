#!/usr/bin/python3

base = __import__('7-base_geometry').BaseGeometry

b = base()
b.integer_validator("name", -7)
