import json


def gather_info():
    """
    function responsible for making a dict of all desired clothes
    repeatedly asks for user input until user specifies they are done
    writes dict to json file called configuration.json
    """
    info = {}                           # stores clothing as keys, info as values
    clothing = ""                       # used to store user input
    size = ""                           # used to store user input
    keep_adding = "yes"                 # variable controlling looping of while loop

    while keep_adding != "no":          # while loop where everything happens
        clothing = raw_input("Please enter name of clothing (or partial match): ")
        size = raw_input("Please enter size of clothing (OS for one size): ")
        info[clothing] = size
        keep_adding = raw_input("Add another? (no to finish/any key to continue): ")

    return info                         # dict full of clothing user wants


if __name__ == "__main__":
    file_path = "./configuration.json"  # file path set to current working directory
    data = gather_info()                # calls gather_info() to construct clothing dict
    with open(file_path,"w") as f:      # opens json file to be written to
        json.dump(data,f)               # writes data to json file
