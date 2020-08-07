def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for a in arrays:
        # Loop thru each item in the array
        for i in a:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1

    result = [i for i in cache if cache[i] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
