"""
Demonstration of asynchronous programming in Python.
Covers async/await, asyncio, and concurrent execution patterns.
"""

import asyncio
import time
from typing import List


# Basic async function
async def say_hello(name: str, delay: float):
    """Simple async function with delay."""
    await asyncio.sleep(delay)
    return f"Hello, {name}!"


async def fetch_data(id: int, delay: float):
    """Simulate fetching data asynchronously."""
    print(f"Fetching data {id}...")
    await asyncio.sleep(delay)
    print(f"Data {id} fetched!")
    return {"id": id, "data": f"Result {id}"}


# Running multiple tasks concurrently
async def fetch_all_data():
    """Fetch multiple data items concurrently."""
    print("=== CONCURRENT TASKS ===")
    
    # Create tasks
    tasks = [
        fetch_data(1, 1.0),
        fetch_data(2, 0.5),
        fetch_data(3, 1.5),
    ]
    
    # Run concurrently
    results = await asyncio.gather(*tasks)
    return results


# Using asyncio.create_task
async def demonstrate_create_task():
    """Show how to create and manage tasks."""
    print("\n=== CREATE TASK ===")
    
    # Create tasks
    task1 = asyncio.create_task(say_hello("Alice", 1.0))
    task2 = asyncio.create_task(say_hello("Bob", 0.5))
    task3 = asyncio.create_task(say_hello("Charlie", 1.5))
    
    # Wait for all tasks
    results = await asyncio.gather(task1, task2, task3)
    for result in results:
        print(result)


# Async context manager
class AsyncResource:
    """Async context manager example."""
    
    async def __aenter__(self):
        print("Acquiring async resource...")
        await asyncio.sleep(0.1)
        print("Resource acquired")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing async resource...")
        await asyncio.sleep(0.1)
        print("Resource released")
        return False
    
    async def do_work(self):
        print("Working with resource...")
        await asyncio.sleep(0.2)
        return "Work completed"


async def use_async_context_manager():
    """Demonstrate async context manager."""
    print("\n=== ASYNC CONTEXT MANAGER ===")
    async with AsyncResource() as resource:
        result = await resource.do_work()
        print(result)


# Async iterator
class AsyncCounter:
    """Async iterator example."""
    
    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.current += 1
        return self.current - 1


async def demonstrate_async_iterator():
    """Show async iteration."""
    print("\n=== ASYNC ITERATOR ===")
    async for num in AsyncCounter(1, 6):
        print(f"Count: {num}")


# Async generator
async def async_range(start: int, end: int):
    """Async generator function."""
    for i in range(start, end):
        await asyncio.sleep(0.1)
        yield i


async def demonstrate_async_generator():
    """Show async generator."""
    print("\n=== ASYNC GENERATOR ===")
    result = []
    async for num in async_range(1, 6):
        result.append(num)
    print(f"Generated: {result}")


# Timeout handling
async def slow_operation():
    """Operation that takes too long."""
    await asyncio.sleep(5)
    return "Completed"


async def demonstrate_timeout():
    """Show timeout handling."""
    print("\n=== TIMEOUT HANDLING ===")
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=1.0)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")


# Task cancellation
async def cancellable_task():
    """Task that can be cancelled."""
    try:
        print("Task started...")
        await asyncio.sleep(10)
        print("Task completed")
    except asyncio.CancelledError:
        print("Task was cancelled!")
        raise


async def demonstrate_cancellation():
    """Show task cancellation."""
    print("\n=== TASK CANCELLATION ===")
    task = asyncio.create_task(cancellable_task())
    await asyncio.sleep(0.5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Handled cancellation")


# Semaphore for limiting concurrency
async def limited_task(semaphore: asyncio.Semaphore, id: int):
    """Task with limited concurrency."""
    async with semaphore:
        print(f"Task {id} started")
        await asyncio.sleep(1)
        print(f"Task {id} completed")
        return id


async def demonstrate_semaphore():
    """Show semaphore usage."""
    print("\n=== SEMAPHORE (Limit Concurrency) ===")
    semaphore = asyncio.Semaphore(2)  # Only 2 concurrent tasks
    
    tasks = [limited_task(semaphore, i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(f"All tasks completed: {results}")


# Queue for producer-consumer pattern
async def producer(queue: asyncio.Queue, n: int):
    """Producer that adds items to queue."""
    for i in range(n):
        await asyncio.sleep(0.1)
        await queue.put(i)
        print(f"Produced: {i}")
    await queue.put(None)  # Sentinel value


async def consumer(queue: asyncio.Queue, name: str):
    """Consumer that processes items from queue."""
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        await asyncio.sleep(0.2)
        print(f"{name} consumed: {item}")
        queue.task_done()


async def demonstrate_queue():
    """Show queue usage."""
    print("\n=== ASYNC QUEUE ===")
    queue = asyncio.Queue()
    
    # Create producer and consumers
    prod = asyncio.create_task(producer(queue, 5))
    cons1 = asyncio.create_task(consumer(queue, "Consumer-1"))
    cons2 = asyncio.create_task(consumer(queue, "Consumer-2"))
    
    await prod
    await queue.join()
    
    # Stop consumers
    await queue.put(None)
    await queue.put(None)
    await asyncio.gather(cons1, cons2)


# Comparison: sync vs async
def sync_task(n: int):
    """Synchronous task."""
    time.sleep(1)
    return n * 2


async def async_task(n: int):
    """Asynchronous task."""
    await asyncio.sleep(1)
    return n * 2


async def compare_sync_async():
    """Compare synchronous and asynchronous execution."""
    print("\n=== SYNC VS ASYNC COMPARISON ===")
    
    # Synchronous execution
    start = time.time()
    results = [sync_task(i) for i in range(3)]
    sync_time = time.time() - start
    print(f"Sync results: {results}, Time: {sync_time:.2f}s")
    
    # Asynchronous execution
    start = time.time()
    tasks = [async_task(i) for i in range(3)]
    results = await asyncio.gather(*tasks)
    async_time = time.time() - start
    print(f"Async results: {results}, Time: {async_time:.2f}s")
    print(f"Speedup: {sync_time/async_time:.2f}x")


# Error handling in async
async def failing_task(should_fail: bool):
    """Task that may fail."""
    await asyncio.sleep(0.5)
    if should_fail:
        raise ValueError("Task failed!")
    return "Success"


async def demonstrate_error_handling():
    """Show error handling in async code."""
    print("\n=== ERROR HANDLING ===")
    
    tasks = [
        failing_task(False),
        failing_task(True),
        failing_task(False),
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")
        else:
            print(f"Task {i} succeeded: {result}")


async def main():
    """Main async function."""
    print("=== BASIC ASYNC/AWAIT ===")
    result = await say_hello("World", 0.5)
    print(result)
    
    # Run all demonstrations
    results = await fetch_all_data()
    print(f"Results: {results}")
    
    await demonstrate_create_task()
    await use_async_context_manager()
    await demonstrate_async_iterator()
    await demonstrate_async_generator()
    await demonstrate_timeout()
    await demonstrate_cancellation()
    await demonstrate_semaphore()
    await demonstrate_queue()
    await compare_sync_async()
    await demonstrate_error_handling()
    
    print("\n=== SUMMARY ===")
    print("Async programming allows concurrent execution")
    print("Use asyncio.gather() for parallel tasks")
    print("Use asyncio.Queue for producer-consumer patterns")
    print("Use Semaphore to limit concurrency")
    print("Always handle timeouts and cancellations")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
