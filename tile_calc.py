width = Decimal(input("Width of floor in metres: "))
length = Decimal(input("Length of floor in metres: "))
cost = Decimal(input("Cost of Tile in $: "))
total = width*length*cost

print (f"The cost to tile a {width}m x {length}m floor is: ${total}")