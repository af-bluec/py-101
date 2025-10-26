"""
Python Asynchronous Programming Demonstration

This module showcases async/await and asyncio features in Python:
- Basic async functions and await
- Async context managers
- Async iterators and generators
- Concurrent execution with asyncio
- Task management and cancellation
- Async file operations and network requests
- Producer-consumer patterns

Asynchronous programming allows for concurrent execution of tasks
without using threads, making it ideal for I/O-bound operations.
"""

import asyncio
# import aiofiles  # Comment out as it may not be available
import random
import time
from typing import AsyncIterator, AsyncGenerator, List, Optional
from dataclasses import dataclass
from contextlib import asynccontextmanager


@dataclass
class TaskResult:
    """Result of an async task execution."""
    task_id: str
    result: any
    duration: float
    success: bool
    error: Optional[str] = None


class AsyncCounter:
    """An async context manager that maintains a counter."""
    
    def __init__(self, name: str):
        self.name = name
        self.count = 0
    
    async def __aenter__(self):
        """Enter the async context."""
        print(f"Starting counter: {self.name}")
        await asyncio.sleep(0.1)  # Simulate async setup
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the async context."""
        print(f"Counter {self.name} final count: {self.count}")
        await asyncio.sleep(0.1)  # Simulate async cleanup
        return False
    
    async def increment(self):
        """Increment the counter asynchronously."""
        await asyncio.sleep(0.05)  # Simulate async work
        self.count += 1
        return self.count


class AsyncNumberGenerator:
    """An async iterator that generates numbers."""
    
    def __init__(self, start: int, end: int, delay: float = 0.1):
        self.start = start
        self.end = end
        self.delay = delay
        self.current = start
    
    def __aiter__(self):
        """Return the async iterator."""
        return self
    
    async def __anext__(self):
        """Get the next value asynchronously."""
        if self.current >= self.end:
            raise StopAsyncIteration
        
        await asyncio.sleep(self.delay)
        value = self.current
        self.current += 1
        return value


async def fetch_data(url: str, delay: float = 1.0) -> dict:
    """
    Simulate fetching data from a URL asynchronously.
    
    Args:
        url: The URL to fetch (simulated)
        delay: Simulation delay in seconds
        
    Returns:
        Simulated response data
    """
    print(f"Fetching data from {url}...")
    
    # Simulate network delay
    await asyncio.sleep(delay)
    
    # Simulate occasional failures
    if random.random() < 0.1:  # 10% failure rate
        raise asyncio.TimeoutError(f"Failed to fetch {url}")
    
    return {
        'url': url,
        'status': 200,
        'data': f'Data from {url}',
        'timestamp': time.time()
    }


async def process_item(item: any, processing_time: float = 0.5) -> any:
    """
    Process an item asynchronously.
    
    Args:
        item: Item to process
        processing_time: Time to simulate processing
        
    Returns:
        Processed item
    """
    await asyncio.sleep(processing_time)
    
    if isinstance(item, str):
        return item.upper()
    elif isinstance(item, (int, float)):
        return item ** 2
    else:
        return f"Processed: {item}"


async def fibonacci_async(n: int) -> AsyncIterator[int]:
    """
    Generate Fibonacci numbers asynchronously.
    
    Args:
        n: Number of Fibonacci numbers to generate
        
    Yields:
        Fibonacci numbers
    """
    a, b = 0, 1
    for i in range(n):
        yield a
        await asyncio.sleep(0.1)  # Simulate async work
        a, b = b, a + b


async def producer(queue: asyncio.Queue, num_items: int):
    """
    Producer coroutine that adds items to a queue.
    
    Args:
        queue: The async queue to add items to
        num_items: Number of items to produce
    """
    print("Producer started")
    
    for i in range(num_items):
        item = f"item_{i}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.2)  # Simulate production time
    
    # Signal completion
    await queue.put(None)
    print("Producer finished")


async def consumer(queue: asyncio.Queue, consumer_id: int):
    """
    Consumer coroutine that processes items from a queue.
    
    Args:
        queue: The async queue to consume from
        consumer_id: ID of this consumer
    """
    print(f"Consumer {consumer_id} started")
    
    while True:
        item = await queue.get()
        
        if item is None:
            # Put the sentinel back for other consumers
            await queue.put(None)
            break
        
        # Process the item
        processed = await process_item(item, 0.3)
        print(f"Consumer {consumer_id} processed: {item} -> {processed}")
        
        queue.task_done()
    
    print(f"Consumer {consumer_id} finished")


@asynccontextmanager
async def async_timer(operation_name: str):
    """
    Async context manager for timing operations.
    
    Args:
        operation_name: Name of the operation being timed
    """
    start_time = time.time()
    print(f"Starting {operation_name}")
    
    try:
        yield
    finally:
        end_time = time.time()
        duration = end_time - start_time
        print(f"{operation_name} completed in {duration:.2f} seconds")


async def batch_fetch_urls(urls: List[str]) -> List[TaskResult]:
    """
    Fetch multiple URLs concurrently.
    
    Args:
        urls: List of URLs to fetch
        
    Returns:
        List of task results
    """
    async def fetch_with_result(url: str, task_id: str) -> TaskResult:
        """Wrapper to capture task results."""
        start_time = time.time()
        
        try:
            result = await fetch_data(url, delay=random.uniform(0.5, 2.0))
            duration = time.time() - start_time
            
            return TaskResult(
                task_id=task_id,
                result=result,
                duration=duration,
                success=True
            )
        
        except Exception as e:
            duration = time.time() - start_time
            
            return TaskResult(
                task_id=task_id,
                result=None,
                duration=duration,
                success=False,
                error=str(e)
            )
    
    # Create tasks for concurrent execution
    tasks = [
        fetch_with_result(url, f"task_{i}")
        for i, url in enumerate(urls)
    ]
    
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks, return_exceptions=False)
    return results


async def demonstrate_async_file_operations():
    """Demonstrate async file operations (simulated)."""
    print("\n=== Async File Operations (Simulated) ===")
    
    # Since aiofiles might not be available, simulate async file operations
    filename = "/tmp/async_test.txt"
    
    # Simulate async file writing
    print("Simulating async file writing...")
    await asyncio.sleep(0.1)  # Simulate async I/O
    
    # Use regular file operations but with async simulation
    with open(filename, 'w') as f:
        f.write("Hello from async file!\n")
        f.write("This is line 2\n")
        f.write("And this is line 3\n")
    
    print(f"File written to {filename}")
    
    # Simulate async file reading
    print("Simulating async file reading...")
    await asyncio.sleep(0.1)  # Simulate async I/O
    
    with open(filename, 'r') as f:
        content = f.read()
        print(f"File content:\n{content}")
    
    # Clean up
    import os
    try:
        os.remove(filename)
        print("Temporary file cleaned up")
    except FileNotFoundError:
        pass


async def demonstrate_task_cancellation():
    """Demonstrate task cancellation."""
    print("\n=== Task Cancellation Demo ===")
    
    async def long_running_task(task_name: str) -> str:
        """A task that takes some time to complete."""
        try:
            for i in range(10):
                print(f"{task_name}: step {i + 1}/10")
                await asyncio.sleep(0.5)
            return f"{task_name} completed successfully"
        
        except asyncio.CancelledError:
            print(f"{task_name} was cancelled")
            raise
    
    # Start multiple tasks
    task1 = asyncio.create_task(long_running_task("Task1"))
    task2 = asyncio.create_task(long_running_task("Task2"))
    
    # Let them run for a bit
    await asyncio.sleep(2)
    
    # Cancel task2
    task2.cancel()
    
    try:
        result1 = await task1
        print(f"Task1 result: {result1}")
    except asyncio.CancelledError:
        print("Task1 was cancelled")
    
    try:
        result2 = await task2
        print(f"Task2 result: {result2}")
    except asyncio.CancelledError:
        print("Task2 was cancelled (expected)")


async def main():
    """Main async function demonstrating various async features."""
    
    print("=== Python Async Programming Demo ===")
    
    # Basic async context manager
    print("\n1. Async Context Manager:")
    async with AsyncCounter("demo_counter") as counter:
        for i in range(5):
            count = await counter.increment()
            print(f"Count: {count}")
    
    # Async iterator
    print("\n2. Async Iterator:")
    async for number in AsyncNumberGenerator(1, 6, 0.2):
        print(f"Generated number: {number}")
    
    # Async generator
    print("\n3. Async Generator (Fibonacci):")
    async for fib in fibonacci_async(8):
        print(f"Fibonacci: {fib}")
    
    # Concurrent URL fetching
    print("\n4. Concurrent URL Fetching:")
    urls = [
        "https://api.example1.com/data",
        "https://api.example2.com/data",
        "https://api.example3.com/data",
        "https://api.example4.com/data",
        "https://api.example5.com/data"
    ]
    
    async with async_timer("Batch URL fetching"):
        results = await batch_fetch_urls(urls)
        
        for result in results:
            if result.success:
                print(f"✓ {result.task_id}: {result.result['url']} "
                      f"({result.duration:.2f}s)")
            else:
                print(f"✗ {result.task_id}: {result.error} "
                      f"({result.duration:.2f}s)")
    
    # Producer-consumer pattern
    print("\n5. Producer-Consumer Pattern:")
    queue = asyncio.Queue(maxsize=5)
    
    # Create producer and consumer tasks
    producer_task = asyncio.create_task(producer(queue, 8))
    consumer_tasks = [
        asyncio.create_task(consumer(queue, i))
        for i in range(3)
    ]
    
    # Wait for producer and consumers to complete
    await producer_task
    await asyncio.gather(*consumer_tasks)
    
    # Async file operations
    await demonstrate_async_file_operations()
    
    # Task cancellation
    await demonstrate_task_cancellation()
    
    print("\n=== Async Programming Demo Complete ===")


if __name__ == "__main__":
    # Run the async main function
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
    except Exception as e:
        print(f"Demo failed with error: {e}")
