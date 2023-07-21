
def possible_bipartition(dislikes):
    if not dislikes:
        return False
    
    dog = {}
    
    for each_node in dislikes:
        if each_node not in dog:
            neighbors = [each_node]
            next_neighbor = []
            curr_dog = True

            while neighbors:
                out = neighbors.pop(0)
                if out in dog:
                    # Check if current dog is intended dog
                    if dog[out] != curr_dog:
                        return False
                else:
                    dog[out] = curr_dog
                    for i in dislikes[out]:
                        next_neighbor.append(i)

                if neighbors == []:
                    curr_dog = not curr_dog
                    neighbors, next_neighbor = next_neighbor, neighbors
    return True

# Test 1 - True
dislikes = { 
    "Fido": [],
    "Nala": ["Cooper", "Spot"],
    "Cooper": ["Nala", "Bruno"],
    "Spot": ["Nala"],
    "Bruno": ["Cooper"]
}
print(f'Test 1: {possible_bipartition(dislikes)}')

# Test 2 - False
dislikes = {
    "Fido": [],
    "Nala": ["Cooper", "Spot"],
    "Cooper": ["Nala", "Spot"],
    "Spot": ["Nala", "Cooper"]
}
print(f'Test 2: {possible_bipartition(dislikes)}')

#test 3 - Empty graph
dislikes = {}
print(f'Test 3: {possible_bipartition(dislikes)}')