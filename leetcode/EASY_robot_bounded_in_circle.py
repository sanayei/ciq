# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:
#
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
#
# Example 1:
#
# Input: "GGLLGG"
# Output: true
# Explanation:
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:
#
# Input: "GG"
# Output: false
# Explanation:
# The robot moves north indefinitely.
# Example 3:
#
# Input: "GL"
# Output: true
# Explanation:
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

def isRobotBounded(instructions):
    x, y = 0, 0
    k = 0
    for i in instructions:
        if i == 'L':
            k = (k + 1) % 4
        elif i == 'R':
            k = (k - 1) % 4
        else:
            if k == 0:
                y += 1
            elif k == 1:
                x -= 1
            elif k == 2:
                y -= 1
            else:
                x += 1
    if x == 0 and y == 0:
        return True
    else:
        return k % 4 != 0



if __name__ == '__main__':
    instructions = 'GGLLGG'
    print(isRobotBounded(instructions))