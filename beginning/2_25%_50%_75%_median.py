def list_of_numbers(numbers):
    list_of_numbers = list(map(float, numbers.split(' ')))
    sorted_numbers = sorted(list_of_numbers)
    len_numbers = len(list_of_numbers)

    return list_of_numbers, sorted_numbers, len_numbers


def median(list_of_numbers, sorted_numbers, len_numbers):
    if len_numbers % 2 != 0:
        median_50 = sorted_numbers[len_numbers // 2]
    else:
        median_50 = str(sorted_numbers[len_numbers // 2]) + " " + str(sorted_numbers[len_numbers // 2] + 1)

    median_25 = sorted_numbers[round(len_numbers * 0.25)]
    median_75 = sorted_numbers[round(len_numbers * 0.75)]
    # return median_25, median_50, median_75

    result = f"""
    Medians: 
        %25: {median_25}
        %50: {median_50}
        %75: {median_75}"""
    return result


numbers = input("Input numbers, separator (' ') : ")
list_of_numbers, sorted_numbers, len_numbers = list_of_numbers(numbers)
print(median(list_of_numbers, sorted_numbers, len_numbers))
