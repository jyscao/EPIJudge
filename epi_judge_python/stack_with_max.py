from test_framework import generic_test
from test_framework.test_failure import TestFailure

from typing import Optional

class Stack:
    def __init__(self):
        self._stack = []

    def empty(self) -> bool:
        return len(self._stack) == 0

    def max(self) -> int:
        _, curr_max = self._stack[-1]
        return curr_max

    def pop(self) -> Optional[int]:
        if not self.empty():
            elem, _ = self._stack.pop()
            return elem
        return None

    def push(self, x: int) -> None:
        self._stack.append((
            x,
            max(self.max(), x) if not self.empty() else x,
        ))


class StackLowMem:
    def __init__(self):
        self._stack = []
        self._max_tups = []

    def empty(self) -> bool:
        return len(self._stack) == 0

    def max(self) -> int:
        return self._max_tups[-1][0]

    def pop(self) -> Optional[int]:
        if self.empty():
            return None

        self._max_tups[-1][1] -= 1
        if self._max_tups[-1][1] == 0:
            self._max_tups.pop()

        return self._stack.pop()

    def push(self, x: int) -> None:
        if (self.empty() and not self._max_tups) or (x > self._max_tups[-1][0]):
            self._max_tups.append([x, 1,])
        else:
            self._max_tups[-1][1] += 1
        self._stack.append(x)


def stack_tester(ops):
    try:
        # s = Stack()
        s = StackLowMem()

        for (op, arg) in ops:
            if op == 'Stack':
                # s = Stack()
                s = StackLowMem()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
