def countingValleys(steps, path):
    up = 0
    down = 0
    valleys = 0
    for i in path:
        if i == "U":
            down -= 1
            if down == 0:
                valleys += 1
        else:
            down += 1
    return valleys
