#!/usr/bin/python3

class Robot(object):
	pass

x = Robot()
Robot.brand = "Toyota"
print(x.brand)

x.brand = "Kia"  # reassignment of value
print(x.brand)
