startTime = time.clock()
index = 0
bestRoute = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60, 72, 84, 96]
print bestRoute
for eachStep in bestRoute:

    # if the next grid visited is equal to current grid + 1, then it must be located to the right
    try:
        if bestRoute[index + 1] == bestRoute[index] + 1:
            while True:
                if round(time.clock(), 2) < round(startTime + 0.5 * index, 2):
                    # sphero.roll(50, 0, 1, True)
                    print 'right'
                else:
                    break

        # if the next grid visited is equal to current grid + 1, then it must be located to the left
        elif bestRoute[index + 1] == bestRoute[index] - 1:
            while True:
                if round(time.clock(), 2) < round(startTime + 0.5 * index, 2):
                    # sphero.roll(50, 180, 1, True)
                    print 'left'
                else:
                    break

        # if the next grid visited is equal to current grid + 12, then it must be located downwards
        elif bestRoute[index + 1] == bestRoute[index] - 12:
            while True:
                if round(time.clock(), 2) < round(startTime + 0.5 * index, 2):
                    # sphero.roll(50, 270, 1, True)
                    print 'up'
                else:
                    break

        # if the next grid visited is not equal to any of the earlier options, it must be located upwards
        elif bestRoute[index + 1] == bestRoute[index] + 12:
            while True:
                if round(time.clock(), 2) < round(startTime + 0.5 * index, 2):
                    # sphero.roll(50, 270, 1, True)
                    print 'down'
                else:
                    break
        index += 1
    # the end of the route
    except IndexError:
        pass