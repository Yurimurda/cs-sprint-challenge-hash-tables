def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here


    hash_table = {}
    result = []

# loop through the list of arrays
    for array in arrays:
# loop through the elements
        for element in array:
            if element not in hash_table:
                hash_table[element] = 0
            else:
                hash_table[element] += 1



# append result to arrays or vice versa?
    for key in hash_table:
        if hash_table[key] == len(arrays) - 1:
            result.append(key)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
