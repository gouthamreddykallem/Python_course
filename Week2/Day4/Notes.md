
## Day 4: Advanced Data Structures

### Teaching Content (30 minutes):
1. Collections Module
   - `defaultdict`
   - `Counter`
   - `OrderedDict`

2. Heapq Module
   - Heap queue algorithm
   - heappush, heappop, heapify

3. Sets and Frozen Sets
   - Creating and using sets
   - Set operations (union, intersection, difference)

### Code Example:
```python
from collections import defaultdict
import heapq

# Word frequency counter using defaultdict
def word_frequency(text):
    words = text.lower().split()
    frequency = defaultdict(int)
    for word in words:
        frequency[word] += 1
    return frequency

# Priority queue with heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

# Usage
text = "the quick brown fox jumps over the lazy dog"
print(word_frequency(text))

pq = PriorityQueue()
pq.push('task1', 5)
pq.push('task2', 1)
pq.push('task3', 3)
print(pq.pop())  # Highest priority task
```


Day 4: Advanced Data Structures
Exercise 1: Word Frequency Counter
Use a defaultdict to count the frequency of words in a given text file. Ignore case and punctuation. Print the top 10 most frequent words.
Exercise 2: Task Priority Queue
Implement a priority queue for tasks using a heapq. Each task should have a description and a priority level. Allow adding tasks, removing the highest priority task, and viewing all tasks in priority order.