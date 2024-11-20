# Progressive Sorting

Progressive Sorting is an unconventional and amusing sorting algorithm that combines iterative counting and element clearing to sort a list.

## How It Works
The algorithm processes a list by:
1. Iteratively counting from 0 to the occurrences of each number in the list.
2. Appending the counted number to a new list as many times as it appears.
3. Removing all occurrences of the number from the original list.
4. Repeating the process with the next integer until the list is empty.

The result is a sorted list.

## Example
Here’s how Progressive Sorting works on a sample input:

### Input:
```python
list = [9, 9, 1000, 10085, 1872, 2221, 22122]
```

### Process:
1. Count occurrences of 0, then 1, and so on.
2. Append occurrences to a new list.
3. Remove processed numbers from the original list.

### Output:
```python
[9, 9, 1000, 1872, 2221, 10085, 22122]
```

## Sample Code
See `main.py`

## Contributing
If you have ideas to make Progressive Sorting even more entertaining (or efficient, though that defeats the purpose), feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.
