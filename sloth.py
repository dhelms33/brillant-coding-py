import animal
class Sloth:
    def __init__(self, name, color, species, favorite_food):
        self.name = name
        self.color = color
        self.species = species, 
        self.favorite_food = favorite_food
        self.arr = arr
    
  #  @value.setter
    def set_species(self):
        self.species = "Linneaus' two-toed sloth"
    
    def set_name(self):
        self.name = "Martin"
    
    def start_dancing(self):
        return("Alright " + self.name + "is dancing!")
    
    def bubble_sort_arr(self, arr):
        i, j = 0
        mid = len(arr)/2
        for i in range(len(arr-1)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
if __name__ == "__main__":
    user_input = input("Please use this to define the attributes, mainly the name, of the slot")
    obj_instance = Sloth(user_input)
    dance_sloth = obj_instance.start_dancing()