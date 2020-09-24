def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here


    # Finding the silver lining between what appears to be 3 arrays. 
    # I have still yet to understand what the + [Arrays] are even doing
    # in the driver code. My best surmission is that I will have to loop through all 3 
    # and create a 'result' array consisting of all numbers the 3 arrays have
    # in common. While it sounds like a solid idea now, it still doesn't speak
    # for the mystery that is the + [Arrays]. It's likely relevent to the subject
    # of hashing but that's only a shot in the dark since my understanding is 
    # tenuous at best.

    hash_table = {}
    result = []

    for array in arrays:
        
        
        

        # append result to arrays or vice versa?



        return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
