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
  
def get_pets_by_breed(pet_list, find_pets):
    breed = []
    for cat in pet_list["pets"]:
        if cat["breed"] == find_pets:
            breed.append(cat)
    return breed 

def find_pet_by_name(pet_list, here_boy):
    for pet_name in pet_list["pets"]:
        if pet_name["name"] == here_boy:
            return pet_name
    return None
    

# def remove_pet_by_name(pet_list, subtract):
#     find_pet = find_pet_by_name(pet_list, subtract)
#     for pet_name in pet_list["pets"]:
#         if pet_name["name"] == find_pet:
#             pet_name.pop(find_pet)

def add_pet_to_stock(pet_list, new_pet):
    pet_list["pets"].append(new_pet)

    
def get_customer_cash(cust_list):
    return cust_list["cash"]

def remove_customer_cash(cust_list, remove_cash):
    cust_list["cash"] -= remove_cash

# def get_customer_pet_count(cust_list, value):
#     count = []
#     for pet_count in cust_list:
#         if pet_count["name"] == value:
#             count.append(pet_count)
#     return count
            
# def add_pet_to_customer(cust_list, value):

    

