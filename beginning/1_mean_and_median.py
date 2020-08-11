def mean_and_median():
    try:
        list_of_numbers = list(map(float, input("Input numbers, separator (' ') : ").split(' ')))
        mean = sum(list_of_numbers) / len(list_of_numbers)
        print(f"Mean: {mean}")
        sorted_numbers = sorted(list_of_numbers)
        len_numbers = len(list_of_numbers)

        if len_numbers % 2 != 0:
            median = sorted_numbers[len_numbers // 2]
        else:
            median = str(sorted_numbers[len_numbers // 2]) + " " + str(sorted_numbers[len_numbers // 2]+1)
        print(f"Median: {median}")

    except:
        print("""
        Please enter only numbers, separated by signal space.
        And use a single dot for decimal point.
        (e.g.: 12.2 20.3 -312.1 0 )
        """)


mean_and_median()
