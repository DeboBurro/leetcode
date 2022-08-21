
def findDataLocation(locations, movedFrom, movedTo):
    '''
    return the locations in ascending order
    '''
    locations = set(locations)
    for fm, to in zip(movedFrom, movedTo):
        locations.remove(fm)
        locations.add(to)
    return sorted(list(locations))

locations = [1, 7, 6, 8]
movedFrom = [1, 7, 2]
movedTo = [2, 9, 5]

print(findDataLocation(locations, movedFrom, movedTo)) # [5, 6, 8 , 9]