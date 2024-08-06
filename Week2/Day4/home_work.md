## Day 4: Advanced Data Structures

1. Implement a `TaskManager` class using a priority queue (heapq):
   - Methods:
     - `add_task(description, priority)`
     - `get_next_task()`
     - `view_all_tasks()`

2. Use a `defaultdict` to create a word frequency counter for a given text file:
   - Ignore punctuation and convert all words to lowercase
   - Print the 10 most common words and their frequencies
   - Save the full word frequency data to a CSV file

3. Implement set operations for managing user groups:
   - Create sets for different user groups (e.g., admin, editor, viewer)
   - Implement functions to:
     - Add a user to a group
     - Remove a user from a group
     - Find users in multiple groups
     - Find users in one group but not another

4. Use an `OrderedDict` to create a simple caching system:
   - Implement a function that retrieves data from a "slow" source (simulate with time.sleep)
   - Cache the results in an OrderedDict, limiting the cache to a fixed size (e.g., 5 items)
   - When the cache is full, remove the oldest item before adding a new one