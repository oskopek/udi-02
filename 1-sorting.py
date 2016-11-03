def sort_integers(numbers):
    def radix_sort(numbers, sd, radix=10):
        buckets = [[] for i in range(0, radix)]
        should_stop = 0
        divisor = radix**sd
        for num in numbers:
            digit = (num // divisor) % radix
            should_stop |= digit
            buckets[digit].append(num)
        if should_stop == 0:
            return numbers
        return radix_sort([n for bucket in buckets for n in bucket], sd+1)

    if not isinstance(numbers, list):
        raise ValueError("Input is not a list.")
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("Invalid input: \"{0}\" is not an int.".format(num))
        if num < 0:
            raise ValueError("Invalid input: \"{0}\" is not a positive int.".format(num))
    return radix_sort(numbers, 0)

