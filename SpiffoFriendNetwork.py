class SpiffoFriendNetwork:
    def __init__(self, id, message):
        self.id = id
        self.message = message
    def create_dict(user_input):
        dict_user = dict(user_input)
        for item in range(len(user_input)):
           ui = user_input.split()
            key = self.id[0]
            value = self.message[-1]
            for range in ui:
                user_dict[key] += {value}
        return user_dict
    def add_job_title(name):
        if len(name) == 0 or len(name) < 0:
            return("name must be bigger than zero")
        try:
            return(f"{name} + has a job as a data engineer")
        except ValueError as e:
            return("Must enter a string for name")
    