def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for num in a:
        if num not in cache:
            cache[num] = None
        if (num * -1) in cache:
            cache[num*-1] = num
            cache[num] = num * -1

    result = []
    for num in cache:
        if num > 0 and cache[num] is not None:
            result.append(num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
