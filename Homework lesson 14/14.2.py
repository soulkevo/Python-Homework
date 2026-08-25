class Counter:
    def __init__(self, min_value=0, max_value=10, start_value=1):
        self.min_value = min_value
        self.max_value = max_value
        self.current = start_value

    def set_current(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError
        self.current = start

    def set_max(self, max_value):
        self.max_value = max_value

    def set_min(self, min_value):
        self.min_value = min_value

    def step_up(self):
        if self.current + 1 > self.max_value:
            raise ValueError
        self.current += 1

    def step_down(self):
        if self.current - 1 < self.min_value:
            raise ValueError
        self.current -= 1

    def get_current(self):
        return self.current


counter = Counter()

counter.set_current(7)
counter.step_up()
counter.step_up()

assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()
except ValueError as ex:
    print(ex)
else:
    assert False, 'Достигнут максимум'

assert counter.get_current() == 10, 'Test2'

counter.set_current(7)
counter.step_down()
counter.step_down()

assert counter.get_current() == 5, 'Test3'

try:
    counter.set_current(-1)
except ValueError as ex:
    print(ex)
else:
    assert False, 'Достигнут минимум'

assert counter.get_current() == 5, 'Test4'