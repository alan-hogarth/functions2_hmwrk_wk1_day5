# WRITE YOUR FUNCTIONS HERE

# def get_pet_shop_name(title):
#     name_result = None
#     for shop_name in title.values():   
#         name_result = shop_name
    
#     return name_result

def get_pet_shop_name(input_dictionary):
    result = input_dictionary["name"]
    return(result)

def get_total_cash(sum):
    return sum["admin"]["total_cash"]

# 
def add_or_remove_cash(dictionary, add_cash):
    dictionary["admin"]["total_cash"] += add_cash
#    adds and removes




# def get_pets_by_breed(shop_dict, dog_breed):
#     pets_by_breed = []
#     for pet in shop_dict["pets"]:
#     if pet["breed" ] == dog_breed:
#         pets_by_breed.append(pet)   
#     return pets_by_breed
    
    

