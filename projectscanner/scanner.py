import os
import json

class ProjectScanner:
    def __init__(self, root_dir=None, batch_size=10, max_length=255, relative_path=True):
        self.root_dir = root_dir or os.getcwd()
        self.batch_size = batch_size
        self.max_length = max_length
        self.relative_path = relative_path
        self.all_items = self._get_all_items()
        self.current_index = 0

    def _get_all_items(self):
        relative_path = self.relative_path
        # Generate a flat list of all files and directories
        all_items = []
        for root, dirs, files in os.walk(self.root_dir):
            for name in dirs + files:
                full_path = os.path.join(root, name)
                if relative_path:
                    full_path = os.path.relpath(full_path, self.root_dir)
                all_items.append(self.truncate_name(full_path))
        return all_items

    def truncate_name(self, name):
        # Truncate name if it exceeds max_length
        return name if len(name) <= self.max_length else name[:self.max_length - 3] + "..."

    def scan_batch(self):
        # Calculate the range for the next batch
        start_index = self.current_index
        end_index = start_index + self.batch_size

        # Slice the batch from all items
        batch_items = self.all_items[start_index:end_index]

        # Update the current index
        self.current_index = end_index if end_index < len(self.all_items) else len(self.all_items)

        return json.dumps({"batch": batch_items})

    def next_batch(self):
        # Simply call scan_batch() to get the next batch
        return self.scan_batch()

    def prev_batch(self):
        # Move the cursor backward and return the previous batch
        new_start_index = max(0, self.current_index - 2 * self.batch_size)
        self.current_index = new_start_index
        return self.scan_batch()

""" Example usage
if __name__ == "__main__":
    # Initialize scanner with deeper directory structure
    scanner = ProjectScanner(batch_size=4)

    # Scan and print the first batch
    print("First Batch:")
    print(scanner.next_batch())

    # Assuming there are more items, scan and print the second batch
    print("Second Batch:")
    print(scanner.next_batch())

    # Go back to the previous batch and print it
    print("Back to First Batch:")
    print(scanner.prev_batch())
"""