

def sort_array(arr):
    continue_sorting = True
    while continue_sorting:
        continue_sorting = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                continue_sorting = True


if __name__ == '__main__':
    numbers_array = [1, 6, 10, 9, 8, 2, 4]
    sort_array(numbers_array)
    print(f"{numbers_array}")
