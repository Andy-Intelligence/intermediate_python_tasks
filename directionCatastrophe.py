
similar = {
    'NORTH':'SOUTH',
    'SOUTH':'NORTH',
    'WEST':'EAST',
    'EAST':'WEST',

}


def pathReducer(givenDirection):
    finalDirection = []
    


    for i in range(0, len(givenDirection)):
        if finalDirection:
            if finalDirection[-1] == similar[givenDirection[i]]:
                finalDirection.pop()

            else:
                finalDirection.append(givenDirection[i])

        else:
            finalDirection.append(givenDirection[i])

    return print(finalDirection)


pathReducer(["NORTH", "NORTH", "WEST", "NORTH", "EAST", "NORTH", "NORTH"])

