with open("day2.txt") as f:
    directions = [line for line in f.readlines()]

def find_position_product():
    horizontal_position = 0
    depth = 0

    for direction in directions:
        split_directions = direction.strip().split(" ")
        orientation, num = split_directions
        
        if orientation == "forward":
            horizontal_position += int(num)
        elif orientation == "down":
            depth += int(num)
        elif orientation == "up":
            depth -= int(num)
    print("Result = ", horizontal_position * depth)
