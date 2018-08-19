import json


def gather_info():
    """
    function responsible for making a dict of all desired clothes
    repeatedly asks for user input until user specifies they are done
    asks for shipping info
    writes dict to json file called config.json
    """
    # master dictionary
    info = {}

    # while loop that gathers clothing dictionary until user is satisfied with dictionary
    confirmation = "no"
    while confirmation != "yes":
        google = google_info()
        confirmation = raw_input("\nIs the info you entered correct? (yes to continue/any key to restart): ")
    info["google"] = google

    # while loop that gathers clothing dictionary until user is satisfied with dictionary
    confirmation = "no"
    while confirmation != "yes":
        clothing = clothing_info()
        confirmation = raw_input("\nIs the info you entered correct? (yes to continue/any key to restart): ")
    info["clothing"] = clothing

    # while loop that gathers shipping dictionary until user is satisfied with dictionary
    confirmation = "no"
    while confirmation != "yes":
        shipping = shipping_info()
        confirmation = raw_input("\nIs the info you entered correct? (yes to continue/any key to restart): ")
    info["shipping"] = shipping

    # while loop that gathers billing dictionary until user is satisfied with dictionary
    confirmation = "no"
    while confirmation != "yes":
        billing = billing_info()
        confirmation = raw_input("\nIs the info you entered correct? (yes to continue/any key to restart): ")
    info["billing"] = billing

    return info


def clothing_info():
    """
    function responsible for gathering clothing info
    clothes are keys while sizes are values
    """
    # dictionary for storing all clothing info and string for controlling while loop
    clothing = {}
    keep_adding = "yes"

    # while loop repeatedly asks user for name and size until user says no 
    while keep_adding != "no":
        name = raw_input("\nPlease enter name of clothing (or partial name): ")
        size = raw_input("\nPlease enter size of clothing (OS for one size): ")
        category = raw_input("\nPlease enter category of clothing: ")
        clothing[name] = [size,category]
        keep_adding = raw_input("\nAdd another? (no to finish/any key to continue): ")

    # returns dict
    return clothing


def shipping_info():
    """
    function responsible for gathering shipping information
    """
    # dictionary storing all shipping info
    shipping = {}
    
    # asking user for information
    name = raw_input("\nPlease enter first and last name: ")
    street = raw_input("\nPlease enter street address: ")
    city = raw_input("\nPlease enter city: ")
    state = raw_input("\nPlease enter state: ")
    zip_code = raw_input("\nPlease enter zip code: ")

    # adding information to dict
    shipping["name"] = name
    shipping["street"] = street
    shipping["city"] = city
    shipping["state"] = state
    shipping["zip"] = zip_code

    # returns dict
    return shipping


def billing_info():
    """
    function responsible for gathering billing information
    """
    # dictionary storing all billing info
    billing = {}

    # asking user for information
    card_number = raw_input("\nPlease enter your credit card number: ")
    expiration = raw_input("\nPlease enter your credit card's expiration date: ")
    cvv = raw_input("\nPlease enter your credit card's cvv: ")

    # adding information to dict
    billing["number"] = card_number
    billing["expiration"] = expiration
    billing["cvv"] = cvv

    # returns dict
    return billing


def google_info():
    """
    function responsible for gathering google sign in information
    """
    # dictionary storing all google sign in info
    google = {}

    # asking user for information
    email = raw_input("\nPlease enter your email address: ")
    password = raw_input("\nPlease enter your password: ")

    # adding information to dict
    google["email"] = email
    google["password"] = password

    # returns dict
    return google


if __name__ == "__main__":
    file_path = "./config.json"     # file path set to current working directory
    data = gather_info()            # calls gather_info() to construct clothing dict
    with open(file_path,"w") as f:  # opens json file to be written to
        json.dump(data,f)           # writes data to json file
