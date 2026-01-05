class Lowlevel:
    def __init__(self, register_a, register_b):
        self.register_a = register_a
        self.register_b = register_b
    def load_a(self.register_a):
        register_a = self.register_a
        return("register a assigned to " + register_a )
    def jump_negative(self.register_a, self.register_b):
        jump_negative_bool = False
        if (self.register_a - self.register_b) < 0:
            destination = abs(self.register_a-self.register_b)
            return("jumped to memory location ", destination)
        else:
            return("No need to jump")
    def add_two(self.register_a, self.register_b):
        result = self.input + self.register_b
        return result
    def sub_two(self.register_a, self.register_b):
        result = self.register_a - self.register_b
        return result
    def increment(self.register_a, self.register_b):
        result = 0
        while self.register_a <= self.register_b:
            self.register_a += 1
            result = self.register_a
        return result
    def increment_v2(self.register_a, self.register_b):
        result = 0
        for self.register_a in range(self.register_b):
            self.register_a += 1
            result = self.register_a
        return result
    