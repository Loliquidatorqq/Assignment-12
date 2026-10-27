def my_sort(numbers):
    numbers = numbers.copy()
    count = 0

    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            count += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers, count


list1 = [5, 2, 8, 1, 4]
list2 = [10, 3, 7, 2, 9, 1, 6, 5, 8, 4]
list3 = [15, 3, 12, 7, 1, 20, 5, 8, 13, 2, 17, 9, 4, 11, 6]

sorted_numbers, comparisons = my_sort(list1)
print("Sorted list:", sorted_numbers)
print("Comparisons:", comparisons)

sorted_numbers, comparisons = my_sort(list2)
print("Sorted list:", sorted_numbers)
print("Comparisons:", comparisons)

sorted_numbers, comparisons = my_sort(list3)
print("Sorted list:", sorted_numbers)
print("Comparisons:", comparisons) 
