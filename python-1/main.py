#!/usr/bin/env python3

import time
import random
import sys

latency = [ 0.0, 0.0 ]

class Stack:
    def __init__(self):
        self.s = []

    def push(self, value):
        self.s.append(value)

    def pop(self):
        return self.s.pop()

    def peek(self):
        return self.s[-1]

    def empty(self):
        return len(self.s) == 0

def sort_v1(stack1, stack2, stack3):
    while not stack1.empty():
        e = stack1.pop()
        while not stack2.empty() and stack2.peek() < e:
            stack1.push(stack2.pop())
        stack2.push(e)
    while not stack2.empty():
        stack1.push(stack2.pop())

def sort_v2(stack1, stack2, stack3):
    pop1  = stack1.pop
    push1 = stack1.push
    pop2  = stack2.pop
    push2 = stack2.push
    while not stack1.empty():
        e = pop1()
        while not stack2.empty() and stack2.peek() < e:
            push1(pop2())
        push2(e)
    while not stack2.empty():
        push1(pop2())

def test_time(func, n, i, *args):
    global latency
    t = 0.0
    for x in range(n):
        start = time.perf_counter()
        func(*args)
        t += time.perf_counter() - start
    latency[i] = t / n

if __name__ == "__main__":
    N = int(sys.argv[1])

    random.seed(42)

    stack1 = Stack()
    stack2 = Stack()
    stack3 = Stack()

    for i in range(N):
        stack1.push(random.randint(0, 10))

    print(N, end=" ")
    test_time(sort_v1, 100, 0, stack1, stack2, stack3)
    test_time(sort_v2, 100, 1, stack1, stack2, stack3)
    print(latency[0], latency[1])
