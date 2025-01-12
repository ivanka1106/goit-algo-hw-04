import random
import timeit
import matplotlib.pyplot as plt

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Генерація даних
def generate_data(size, case="random"):
    if case == "random":
        return [random.randint(0, 10000) for _ in range(size)]
    elif case == "sorted":
        return list(range(size))
    elif case == "reversed":
        return list(range(size, 0, -1))

# Тестування часу виконання
def measure_time(func, data):
    # Копіюємо дані, щоб уникнути побічних ефектів
    arr = data[:]
    start = timeit.default_timer()
    func(arr)
    end = timeit.default_timer()
    return end - start

# Порівняння алгоритмів
def compare_algorithms(sizes, cases):
    results = {"insertion": [], "merge": [], "timsort": []}
    for size in sizes:
        for case in cases:
            data = generate_data(size, case)

            # Сортування вставками
            if size <= 1000:  # Сортування вставками занадто повільне на великих масивах
                results["insertion"].append(measure_time(insertion_sort, data))
            else:
                results["insertion"].append(None)

            # Сортування злиттям
            results["merge"].append(measure_time(merge_sort, data))

            # Timsort
            results["timsort"].append(measure_time(sorted, data))

    return results

# Візуалізація
def plot_results(sizes, cases, results):
    for case_index, case in enumerate(cases):
        plt.figure()
        plt.title(f"Sorting Performance ({case.capitalize()} Data)")
        plt.plot(sizes, [results["merge"][i + case_index * len(sizes)] for i in range(len(sizes))], label="Merge Sort")
        plt.plot(sizes, [results["timsort"][i + case_index * len(sizes)] for i in range(len(sizes))], label="Timsort")
        plt.plot(sizes, [results["insertion"][i + case_index * len(sizes)] if results["insertion"][i + case_index * len(sizes)] is not None else None for i in range(len(sizes))], label="Insertion Sort")
        plt.xlabel("Size of Array")
        plt.ylabel("Time (seconds)")
        plt.legend()
        plt.show()

# Основна функція
def main():
    sizes = [100, 500, 1000, 5000, 10000]
    cases = ["random", "sorted", "reversed"]

    results = compare_algorithms(sizes, cases)
    plot_results(sizes, cases, results)

if __name__ == "__main__":
    main()


""""
 Висновки:
 1. Timsort є найкращим вибором, оскільки він ефективно комбінує сортування злиттям і вставками.
 2. Timsort використовується у вбудованих функціях Python (sorted, .sort()) і дозволяє досягати оптимальної продуктивності.
 3. Для великих масивів слід використовувати Timsort або сортування злиттям, а не сортування вставками.
 """