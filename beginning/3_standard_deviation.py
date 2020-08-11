def standard_deviation(numbers):
    from math import sqrt
    def list_of_numbers(numbers):
        list_of_numbers = list(map(float, numbers.split(' ')))
        sorted_numbers = sorted(list_of_numbers)
        len_numbers = len(list_of_numbers)

        return list_of_numbers, sorted_numbers, len_numbers

    def mean(list_of_numbers):
        return sum(list_of_numbers) / len(list_of_numbers)


    list_of_numbers, sorted_numbers, len_numbers = list_of_numbers(numbers)
    mean = mean(list_of_numbers)

    away_from_mean = [x - mean for x in sorted_numbers]
    sum_of_variance = [x*x for x in away_from_mean]
    sum_of_variance = sum(sum_of_variance)
    variance = sum_of_variance/len_numbers
    standard_deviation = sqrt(variance)

    return standard_deviation

numbers = input("Input numbers, separator (' ') : ")
print(standard_deviation(numbers))

# 15 16 18 19 22 24 29 30 34