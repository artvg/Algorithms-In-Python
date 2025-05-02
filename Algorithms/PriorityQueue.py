# Priority Queue 

class PriorityQueue:
    def __init__(self):
        self.queue = []  # Will store items as (item, priority) tuples

    def enqueue(self, item, priority):
        new_element = (item, priority)  # Create a tuple
        self.queue.append(new_element)  # Add to queue
        self.queue.sort(key=lambda x: x[1])  # Sort by priority (smallest first)
        # self.queue.sort(key=lambda x: x[1], reverse=True) # for (largest first)


    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # First item has the highest priority
        else:
            return None  # Queue is empty

    def peek(self):
        if not self.is_empty():
            return self.queue[0]  # First item is top priority
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

# Testing the Priority Queue
if __name__ == "__main__":
    print("\n=== Priority Queue Test ===")

    # Create a priority queue 
    pq = PriorityQueue()

    # Enqueue some tasks
    print("Adding tasks to queue...")
    pq.enqueue("Finish Homework", 1)
    pq.enqueue("Play Video Games", 3)
    pq.enqueue("Eat Lunch", 2)
    pq.enqueue("Reply to Emails", 5)

    # Print the current queue
    print("Current Queue:", pq.queue)

    # Peek at the highest priority item
    print("Peek at top priority:", pq.peek())

    # Dequeue the highest priority item
    print("Dequeueing highest priority item:", pq.dequeue())
    print("Queue after dequeuing:", pq.queue)

    # Dequeue another item
    print("Dequeueing next highest priority item:", pq.dequeue())

    # Check if queue is empty
    print("Is the queue empty?", pq.is_empty())

    # Final state of the queue
    print("Final Queue State:", pq.queue)
