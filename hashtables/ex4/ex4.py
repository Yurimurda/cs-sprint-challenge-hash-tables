def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    result = []
    # At first glance, the idea would be to break down 'a'
    # into 2 arrays, negative and positive numbers. Instead,
    # I will need to loop though the list's positive numbers.

    for positives in a:
        # For all the positives in the array, 
        # send them to the dictionary.
        hash_table[positives] = positives
        
    # Now that all the positives are targeted,
    # If the number isn't 0 or in the table,
    # append it to the result array as it's positive
    # counterpart.
        if positives != 0 and - positives in hash_table:
            result.append(abs(positives))



    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
