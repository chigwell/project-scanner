[![PyPI version](https://badge.fury.io/py/project-scanner.svg)](https://badge.fury.io/py/project-scanner)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/project-scanner)](https://pepy.tech/project/project-scanner)

# Project Scanner

`ProjectScanner` is a Python package designed to scan your project's directory and file structure, providing a batch-wise navigational approach. It's especially useful for analyzing large projects with deep directory structures, allowing users to paginate through directories and files effectively.

## Installation

To install `ProjectScanner`, use pip:

```bash
pip install project-scanner
```

## Usage

### As a Python Module

You can use `ProjectScanner` as a module in your Python scripts.

Example:

```python
from projectscanner import ProjectScanner

# Initialize the scanner with the root directory of your project
scanner = ProjectScanner(root_dir="path/to/your/project", batch_size=10, max_length=255)

# Scan and print the first batch of items
print("First Batch:")
print(scanner.next_batch())

# Assuming there are more items, scan and print the next batch
print("Next Batch:")
print(scanner.next_batch())

# Go back to the previous batch and print it
print("Previous Batch:")
print(scanner.prev_batch())
```

### Configuration

You can customize the behavior of `ProjectScanner` by adjusting the initialization parameters:

- `root_dir`: The root directory of your project (default is the current working directory).
- `batch_size`: The number of items (files or directories) to include in each batch (default is 10).
- `max_length`: The maximum character length for file or directory names before truncation (default is 255).
- `relative_path`: Set to `True` to use relative paths for items, or `False` for absolute paths (default is `True`).

## Output Example

When you run `ProjectScanner`, it provides you a batch of directory and file names in your project's structure. Here is an example output:

```
First Batch:
["dir1", "dir2", "file1.txt", "file2.txt"]
Next Batch:
["dir3/subdir1", "dir3/subdir2", "file3.txt", "dir4"]
...
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/chigwell/project-scanner/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)
