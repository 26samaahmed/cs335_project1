#Author: Robbie Robertson
#Date: 02/22/25
#Class: Algorithm Engineering
#Purpse: Providing json writing functionality for the sorting algorithm module
#        Providing json reading funcitonality for the data visualization module
#        Providing functions for packing data into our json format
#        Providing functions for parsing json data
import json
import os

# Sorting algo json logs format
#list_of_sort_logs =                     #Naming Outer Key: sortingalgorithmname_number
#    "outer_key": [                     #Name of sorting algorithm that was run + underscore + number(in case the algorithm is run more than once per runtime) eg 0,1,2,..
#        "inner_key1": [1, 2, 3, 4],     #Naming Inner Key: Inner key will be the step count of the sorting algorithm when data was logged eg 0(start),5,10,15,20,....
#        "inner_key2": [5, 6, 7, 8]      #Inner Value: list of integers in their current order as the value
#                 ]
#
#

####File Variables(Treat as private)
_sorting_algorithm_name = ""
_current_step = -1
_current_order = []

##
_bubble_sort_count = 0
_quick_sort_count = 0
_merge_sort_count = 0
_insertion_sort_count = 0
_radix_sort_count = 0

####Json Functions
####Creating, Reading, Writing
def create_json(file_name, file_number):
    file_extension = ".json"
    results_directory_name = "results"
    full_file_name = file_name + "_" + str(file_number) + file_extension

    full_path = os.path.join(results_directory_name, full_file_name)

    try:
        with open(full_path, "w"):
            print("Json file " + full_path + " succesfully  created")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return full_path


def read_json(json_path):

    try:
        with open(json_path, "r") as json:
            read_data = json.load(json)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return read_data

def write_json(json_path, sorting_log_data):

    try:
        with open(json_path, "w") as json:
            print("Json file " + json + " succesfully  opened")
            json.dump(sorting_log_data, json)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return

####Input Data Functions

def start_log(name_of_algorithm):
    algo_index_number = determine_index_number()
    full_log_key = name_of_algorithm + "_" + str(algo_index_number)
    log_dictionary = {full_log_key : []}


    return log_dictionary

def input_log():


    return

def determine_index_number():

    return


####Packing data functions
####

def pack_data():

    return



####
####Parsing data functions



##################Testing Block##############################################################
new_file_path = create_json("test_file",00)
print(new_file_path)