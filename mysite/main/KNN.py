import math

def k_nearest_neighbours(k: int, criteria: list, data: list[list], test: list):
    '''
    A function for getting the k nearest neighbours of 'test' in relation to 'data'.
    The length of 'data' should be one longer than 'test' and the first entry of each row should be its criteria.\n
    Example:\n
    knn = k_nearest_neighbours(3, ['A', 'B'], [['A', 1, 0.5], ['B', -2, 3], ['B', 1, 2]], [0.5, 3])
    '''

    distances = [math.dist(test, row[1:]) for row in data]
    if 0 in distances: raise Exception("That data already exists.")

    min_k_ind = sorted(range(len(distances)), key=lambda sub: distances[sub])[:k]

    criteria_dict = {key: 0.0 for key in criteria}

    for i in min_k_ind:
        criteria_dict[data[i][0]] += 1 / distances[i]
    
    biggest_val = max(criteria_dict, key=criteria_dict.get)
    
    return biggest_val
