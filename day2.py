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
    return horizontal_position * depth


def find_depth_with_aim():
    horizontal_position = 0
    depth = 0
    aim = 0

    for direction in directions:
        split_directions = direction.strip().split(" ")
        orientation, num = split_directions
        num = int(num)
        
        if orientation == "forward":
            horizontal_position += num
            depth = depth + (aim * num)
        elif orientation == "down":
            aim += num
        elif orientation == "up":
            aim -= num
    print("Result = ", horizontal_position * depth)
    return horizontal_position * depth