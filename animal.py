class Animal:
    def _init_(self, type, action, instinct):
        self.type = type
        self.action = action
        self.instinct = instinct
    def do_action(is_asleep, action, is_obedient):
        if is_asleep:
            return("Cannot do action, sleeping, please don't wake.")
        elif is_obedient:
            return("doing ", action)
        else: 
            return("not doing ", action, "not obedient")