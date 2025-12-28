class Lowlevel:
    def __init__(self, input_a, input_b):
        self.input_a = input_a
        self.input_b = input_b
    def load_a(self.input_a):
        register_a = self.input_a
        return("register a assigned to " + register_a )
    def jump_negative(self.input_a, self.input_b):
        jump_negative_bool = False
        if (self.input_a - self.input_b) < 0:
            destination = abs(self.input_a-self.input_b)
            return("jumped to memory location ", destination)
        else:
            return("No need to jump")