# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(dictionary):
    result = dictionary["name"]
    return(result)

def get_total_cash(sum):
    return sum["admin"]["total_cash"]
 
def add_or_remove_cash(dictionary, add_cash):
    dictionary["admin"]["total_cash"] += add_cash

#    adds and removes

def get_pets_sold(find_pets):
    return find_pets["admin"]["pets_sold"]

def increase_pets_sold(dictionary, add_pets):
    dictionary["admin"]["pets_sold"] = add_pets

def get_stock_count(count):
    stock_count = len(count["pets"])
    return stock_count
  
def get_pets_by_breed(pet_list, find_breed):
    breed = []
    for cat in pet_list["pets"]:
        if cat["breed"] == find_breed:
            breed.append(cat)
    return breed 

def find_pet_by_name(pet_list, pet_name):
    for pet in pet_list["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None
    

def remove_pet_by_name(pet_list, pet_name):
    for pet in pet_list["pets"]:
        if pet["name"] == pet_name:
            pet_list["pets"].remove(pet)
#    

def add_pet_to_stock(pet_list, new_pet):
    pet_list["pets"].append(new_pet)

    
def get_customer_cash(cust_list):
    return cust_list["cash"]

def remove_customer_cash(cust_list, remove_cash):
    cust_list["cash"] -= remove_cash

def get_customer_pet_count(cust_list):
    cust_list["pets"] = 0
    return cust_list["pets"]
           
# def add_pet_to_customer(cust_list, new_pet):
#     for customer in cust_list:
#         customer["pets"].append(new_pet)
    


    

