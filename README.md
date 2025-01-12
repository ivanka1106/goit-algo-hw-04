# Sorting Algorithms Comparison

## Overview
This project compares three sorting algorithms:
1. Insertion Sort
2. Merge Sort
3. Timsort (Python's built-in sorting function)

## Results
### Complexity Analysis
| Algorithm       | Best Case      | Average Case     | Worst Case      | Space Complexity |
|------------------|----------------|------------------|-----------------|------------------|
| Insertion Sort  | \(O(n)\)       | \(O(n^2)\)       | \(O(n^2)\)      | \(O(1)\)         |
| Merge Sort      | \(O(n \log n)\)| \(O(n \log n)\)  | \(O(n \log n)\) | \(O(n)\)         |
| Timsort         | \(O(n)\)       | \(O(n \log n)\)  | \(O(n \log n)\) | \(O(n)\)         |

### Performance
- Insertion Sort: Best for small arrays or partially sorted data.
- Merge Sort: Efficient for larger arrays.
- Timsort: Most efficient due to its hybrid nature.

### Graphs
Graphs demonstrate Timsort's efficiency across various datasets.

## Conclusion
Timsort's combination of Merge Sort and Insertion Sort makes it the most efficient in real-world scenarios.