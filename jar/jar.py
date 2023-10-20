class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit amount must be a non-negative integer.")
        if self._cookies + n > self._capacity:
            raise ValueError("Adding cookies would exceed the jar's capacity.")
        self._cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdrawal amount must be a non-negative integer.")
        if self._cookies < n:
            raise ValueError("Not enough cookies in the jar to withdraw.")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies