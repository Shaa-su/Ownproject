#!/usr/bin/env python3
"""
Python Code Examples and Utilities
A collection of useful Python code snippets and examples
"""

import os
import sys
import json
import datetime
from typing import List, Dict, Optional, Union
from dataclasses import dataclass
from pathlib import Path


# ============= DATA STRUCTURES =============

@dataclass
class Person:
    """Example dataclass for representing a person"""
    name: str
    age: int
    email: Optional[str] = None
    
    def greet(self) -> str:
        return f"Hello, I'm {self.name} and I'm {self.age} years old"
    
    def is_adult(self) -> bool:
        return self.age >= 18


class Calculator:
    """Simple calculator class with basic operations"""
    
    def __init__(self):
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        return self.history.copy()


# ============= UTILITY FUNCTIONS =============

def fibonacci(n: int) -> List[int]:
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def is_prime(num: int) -> bool:
    """Check if a number is prime"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def find_primes(limit: int) -> List[int]:
    """Find all prime numbers up to the given limit"""
    return [num for num in range(2, limit + 1) if is_prime(num)]


def word_count(text: str) -> Dict[str, int]:
    """Count occurrences of each word in text"""
    words = text.lower().split()
    word_dict = {}
    for word in words:
        # Remove punctuation
        word = ''.join(char for char in word if char.isalnum())
        if word:
            word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


def list_files(directory: str, extension: str = None) -> List[str]:
    """List all files in a directory, optionally filtered by extension"""
    path = Path(directory)
    if not path.exists():
        return []
    
    if extension:
        pattern = f"*.{extension.lstrip('.')}"
        return [str(file) for file in path.glob(pattern)]
    else:
        return [str(file) for file in path.iterdir() if file.is_file()]


def read_json_file(filepath: str) -> Dict:
    """Read and parse a JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filepath} not found")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return {}


def write_json_file(data: Dict, filepath: str) -> bool:
    """Write data to a JSON file"""
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error writing JSON file: {e}")
        return False


def get_current_timestamp() -> str:
    """Get current timestamp in ISO format"""
    return datetime.datetime.now().isoformat()


def format_file_size(size_bytes: int) -> str:
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


# ============= LIST COMPREHENSIONS & GENERATORS =============

def squares(n: int) -> List[int]:
    """Generate list of squares from 1 to n"""
    return [i**2 for i in range(1, n+1)]


def even_numbers(limit: int) -> List[int]:
    """Get all even numbers up to limit"""
    return [i for i in range(2, limit+1, 2)]


def filter_strings_by_length(strings: List[str], min_length: int) -> List[str]:
    """Filter strings by minimum length"""
    return [s for s in strings if len(s) >= min_length]


def number_generator(start: int, end: int, step: int = 1):
    """Generator function for numbers in range"""
    current = start
    while current < end:
        yield current
        current += step


# ============= DECORATORS =============

def timer(func):
    """Decorator to measure function execution time"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def retry(max_attempts: int = 3):
    """Decorator to retry function on failure"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}")
            return None
        return wrapper
    return decorator


# ============= CONTEXT MANAGERS =============

class FileManager:
    """Context manager for file operations"""
    
    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# ============= MAIN EXECUTION =============

def demonstrate_features():
    """Demonstrate various Python features"""
    print("=== Python Code Demonstration ===\n")
    
    # Person dataclass
    person = Person("Alice", 25, "alice@example.com")
    print(f"Person: {person.greet()}")
    print(f"Is adult: {person.is_adult()}\n")
    
    # Calculator
    calc = Calculator()
    print("Calculator operations:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"History: {calc.get_history()}\n")
    
    # Fibonacci
    fib_sequence = fibonacci(10)
    print(f"Fibonacci (10 terms): {fib_sequence}\n")
    
    # Prime numbers
    primes = find_primes(20)
    print(f"Primes up to 20: {primes}\n")
    
    # Word count
    text = "Python is great! Python is powerful and Python is fun."
    words = word_count(text)
    print(f"Word count: {words}\n")
    
    # List comprehensions
    squares_list = squares(5)
    evens = even_numbers(10)
    print(f"Squares 1-5: {squares_list}")
    print(f"Even numbers up to 10: {evens}\n")
    
    # Generator
    print("Number generator (1-5):")
    for num in number_generator(1, 6):
        print(num, end=" ")
    print("\n")
    
    # Current timestamp
    print(f"Current timestamp: {get_current_timestamp()}")
    
    # File size formatting
    print(f"File size: {format_file_size(1024 * 1024 * 5)}")


@timer
def example_timed_function():
    """Example function to demonstrate timer decorator"""
    import time
    time.sleep(1)
    return "Function completed"


if __name__ == "__main__":
    try:
        demonstrate_features()
        
        print("\n=== Testing decorators ===")
        result = example_timed_function()
        print(f"Result: {result}")
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
