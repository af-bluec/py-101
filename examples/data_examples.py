"""
Data structures examples.

This file demonstrates usage of various data structure helper functions.
"""

from utils.data_structures import (
    flatten_list, remove_duplicates, merge_dicts, group_by_key,
    sort_dict_by_value, invert_dict, chunk_list, transpose_matrix,
    find_common_elements, rotate_list, count_elements, most_frequent_element,
    partition_list, sliding_window, cartesian_product
)


def run_data_examples():
    """Run examples of data structure utility functions."""
    
    print("=== DATA STRUCTURE UTILITY EXAMPLES ===\n")
    
    # List flattening
    print("1. List Flattening:")
    nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
    flattened = flatten_list(nested)
    print(f"Nested list: {nested}")
    print(f"Flattened: {flattened}\n")
    
    # Removing duplicates
    print("2. Remove Duplicates (preserving order):")
    with_dupes = [1, 2, 3, 2, 4, 1, 5, 3, 6]
    unique = remove_duplicates(with_dupes)
    print(f"With duplicates: {with_dupes}")
    print(f"Unique elements: {unique}\n")
    
    # Dictionary merging
    print("3. Dictionary Merging:")
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 20, "d": 4, "e": 5}
    
    merged_overwrite = merge_dicts(dict1, dict2, "overwrite")
    merged_keep_first = merge_dicts(dict1, dict2, "keep_first")
    merged_combine = merge_dicts({"x": [1, 2]}, {"x": [3, 4]}, "combine")
    
    print(f"Dict 1: {dict1}")
    print(f"Dict 2: {dict2}")
    print(f"Merged (overwrite): {merged_overwrite}")
    print(f"Merged (keep first): {merged_keep_first}")
    print(f"Merged (combine lists): {merged_combine}\n")
    
    # Grouping by key
    print("4. Group by Key:")
    students = [
        {"name": "Alice", "grade": "A", "subject": "Math"},
        {"name": "Bob", "grade": "B", "subject": "Math"},
        {"name": "Carol", "grade": "A", "subject": "Science"},
        {"name": "David", "grade": "B", "subject": "Science"},
        {"name": "Eve", "grade": "A", "subject": "Math"}
    ]
    
    grouped_by_grade = group_by_key(students, "grade")
    grouped_by_subject = group_by_key(students, "subject")
    
    print("Students:", students)
    print("Grouped by grade:")
    for grade, group in grouped_by_grade.items():
        names = [student["name"] for student in group]
        print(f"  Grade {grade}: {names}")
    print("Grouped by subject:")
    for subject, group in grouped_by_subject.items():
        names = [student["name"] for student in group]
        print(f"  {subject}: {names}")
    print()
    
    # Dictionary sorting
    print("5. Dictionary Sorting:")
    scores = {"Alice": 85, "Bob": 92, "Carol": 78, "David": 95, "Eve": 88}
    sorted_asc = sort_dict_by_value(scores)
    sorted_desc = sort_dict_by_value(scores, reverse=True)
    
    print(f"Original scores: {scores}")
    print(f"Sorted ascending: {sorted_asc}")
    print(f"Sorted descending: {sorted_desc}\n")
    
    # Dictionary inversion
    print("6. Dictionary Inversion:")
    original = {"apple": 1, "banana": 2, "cherry": 3}
    inverted = invert_dict(original)
    print(f"Original: {original}")
    print(f"Inverted: {inverted}\n")
    
    # List chunking
    print("7. List Chunking:")
    numbers = list(range(1, 21))  # [1, 2, ..., 20]
    chunks = chunk_list(numbers, 5)
    print(f"Numbers: {numbers}")
    print(f"Chunks of 5: {chunks}\n")
    
    # Matrix transposition
    print("8. Matrix Transposition:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = transpose_matrix(matrix)
    print("Original matrix:")
    for row in matrix:
        print(f"  {row}")
    print("Transposed matrix:")
    for row in transposed:
        print(f"  {row}")
    print()
    
    # Finding common elements
    print("9. Set Operations:")
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    
    common = find_common_elements(list1, list2)
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Common elements: {common}\n")
    
    # List rotation
    print("10. List Rotation:")
    original_list = [1, 2, 3, 4, 5]
    rotated_right = rotate_list(original_list, 2)
    rotated_left = rotate_list(original_list, -2)
    
    print(f"Original: {original_list}")
    print(f"Rotated right by 2: {rotated_right}")
    print(f"Rotated left by 2: {rotated_left}\n")
    
    # Element counting
    print("11. Element Counting:")
    items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counts = count_elements(items)
    most_frequent = most_frequent_element(items)
    
    print(f"Items: {items}")
    print(f"Counts: {counts}")
    print(f"Most frequent: {most_frequent}\n")
    
    # List partitioning
    print("12. List Partitioning:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens, odds = partition_list(numbers, lambda x: x % 2 == 0)
    
    print(f"Numbers: {numbers}")
    print(f"Evens: {evens}")
    print(f"Odds: {odds}\n")
    
    # Sliding window
    print("13. Sliding Window:")
    data = [1, 2, 3, 4, 5, 6, 7]
    windows = sliding_window(data, 3)
    
    print(f"Data: {data}")
    print(f"Sliding windows (size 3): {windows}\n")
    
    # Cartesian product
    print("14. Cartesian Product:")
    colors = ["red", "blue"]
    sizes = ["S", "M", "L"]
    combinations = cartesian_product(colors, sizes)
    
    print(f"Colors: {colors}")
    print(f"Sizes: {sizes}")
    print(f"Combinations: {combinations}\n")
    
    # Complex nested operations
    print("15. Complex Nested Data:")
    
    # Simulating a complex data analysis task
    sales_data = [
        {"product": "Laptop", "category": "Electronics", "sales": [1000, 1200, 800]},
        {"product": "Phone", "category": "Electronics", "sales": [800, 900, 1100]},
        {"product": "Desk", "category": "Furniture", "sales": [300, 250, 400]},
        {"product": "Chair", "category": "Furniture", "sales": [200, 300, 250]}
    ]
    
    # Group by category and calculate total sales
    by_category = group_by_key(sales_data, "category")
    
    print("Sales Analysis:")
    for category, products in by_category.items():
        total_sales = sum(sum(product["sales"]) for product in products)
        product_names = [product["product"] for product in products]
        print(f"  {category}: {product_names}, Total Sales: ${total_sales}")


if __name__ == "__main__":
    run_data_examples()
