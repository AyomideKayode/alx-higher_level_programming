#!/usr/bin/python3

class Robot:
	pass
x = Robot()
y = Robot()
x.name = "Sola"
x.build_year = "1979"
y.name = "Motun"
y.build_year = "1985"
print(x.name)

print(x.__dict__)
print(y.__dict__)
