import heapq

def merge_k_lists(lists):
    """
    Зливає k відсортованих списків в один відсортований список.
    :param lists: список відсортованих списків
    :return: один відсортований список
    """
    # Створюємо мін-кучу
    heap = []
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, чи список не порожній
            # Додаємо перший елемент кожного списку у вигляді (значення, індекс списку, індекс елемента)
            heapq.heappush(heap, (lst[0], i, 0))
    
    result = []

    # Поки в купі є елементи
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)  # Витягуємо найменший елемент
        result.append(val)  
        
        # Якщо в списку є ще елементи, додаємо наступний елемент у купу
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)