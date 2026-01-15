import logging
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
    def jump(self.register_a, self.register_b):
        jump = False
        ending_register = 0
        if self.register_a > self.register_b:
            jump = True
            ending_register = self.register_a
            return("Jump successful ending register ", self.register_a)
        else:
            jump = False
            return("Jump unsuccessful, try again")
    def multiply(self.register_a, num):
        try:
            result = 0
            for i in range(num):
                result = self.register_a + self.register_a
            return result
        except ValueError as e:
            return("{e} results in a Value Error, try again")
    def divide(self.register_a, num):
        result = 0
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename = "E:\\pyhton\\Lumberjack.log",
                            level = logging.DEBUG,
                            format = LOG_FORMAT)
        logger = logging.getLogger
        logging
        try:
            while self.register_a > 0:
                for i in range(num):
                    result = self.register_a - self.register_a
            return result
        except ValueError as e:
            logger.
            return("{e} is a number that is equal to or less than zero, please try again.")
    def bitwise_and(self.register_a, self.register_b):
        if self.register_a == 1 and self.register_b == 1:
            return 1
        else:
            return 0
    def bitwise_or(self.register_a, self.register_b):
        if self.register_a == 1 or self.register_b == 1:
            return 1
        else:
            return 0
    