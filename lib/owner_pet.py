class Pet:
    #4
    all = []
   
    #3
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    #2
    def __init__(self, name, pet_type, owner= None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        #3
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        
        #8
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("The owner must be an instance of Owner")
            owner.add_pet(self)

        Pet.all.append(self)

class Owner:
    #1
    def __init__(self, name):
        self.name = name
        self._pets = []

    #5
    def pets(self):
        return self._pets
   
    #6
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet")
        pet.owner = self 
        self._pets.append(pet)
   
    #7
    def get_sorted_pets(self):
        return sorted(self._pets, key = lambda pet: pet.name)
 
    

