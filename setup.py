import json


def gather_info():
    """
    function responsible for making a dict of all desired clothes
    repeatedly asks for user input until user specifies they are done
    asks for shipping info
    writes dict to json file called configuration.json
    """
    # initial variables; master dictionary, placeholders for user input, while loop control
    info = {}
    clothing = ""
    size = ""
    keep_adding = "yes"

    # outer while loop repeates process until user confirms their inputs
    confirmation = "no"
    while confirmation != "yes":
        # while loop storing clothes as keys, sizes as values; stops when user enters no at end
        clothing_dict = {}
        while keep_adding != "no":
            clothing = raw_input("\nPlease enter name of clothing (or partial match): ")
            size = raw_input("\nPlease enter size of clothing (OS for one size): ")
            clothing_dict[clothing] = size
            keep_adding = raw_input("\nAdd another? (no to finish/any key to continue): ")
        confirmation = raw_input("Is the info you entered correct? (yes to continue/any key to restart): ")
    info["clothing"] = clothing_dict

    return info                     # dict full of clothing user wants


def shipping_info():
    """
    function responsible for gathering shipping information
    """
    # dictionary storing all shipping info
    shipping = {}
    
    # asking user for information
    first_name = raw_input("\nPlease enter first name: ")
    last_name = raw_input("\nPlease enter last name: ")
    street = raw_input("\nPlease enter street address: ")
    city = raw_input("\nPlease enter city: ")
    state = raw_input("\nPlease enter state: ")
    zip_code = raw_input("\nPlease enter zip code: ")

    # adding information to dict
    shipping["first"] = first_name
    shipping["last"] = last_name
    shipping["street"] = street
    shipping["city"] = city
    shipping["state"] = state
    shipping["zip"] = zip_code

    # returns dictionary
    return shipping


if __name__ == "__main__":
    file_path = "./config.json"     # file path set to current working directory
    data = gather_info()            # calls gather_info() to construct clothing dict
    with open(file_path,"w") as f:  # opens json file to be written to
        json.dump(data,f)           # writes data to json file
