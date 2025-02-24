#Author: Robbie Robertson
#Date: 02/22/25
#Class: Algorithm Engineering
#Purpse: Providing json writing functionality for the sorting algorithm module
#        Providing json reading funcitonality for the data visualization module
#        Providing functions for packing data into our json format
#        Providing functions for parsing json data
import json
import os
from datetime import datetime
from pathlib import Path

# Sorting algo json logs format
#list_of_sort_logs =                     #Naming Outer Key: sortingalgorithmname_number
#    "outer_key": [                     #Name of sorting algorithm that was run + underscore + number(in case the algorithm is run more than once per runtime) eg 0,1,2,..
#        "inner_key1": [1, 2, 3, 4],     #Naming Inner Key: Inner key will be the step count of the sorting algorithm when data was logged eg 0(start),5,10,15,20,....
#        "inner_key2": [5, 6, 7, 8]      #Inner Value: list of integers in their current order as the value
#                 ]
#
#

####Constants
CONST_NEWLOG_NAME = "99_newlog"
CONST_JSONL_FILE_EXT = ".jsonl"


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
def create_json(file_name):
    file_extension = ".jsonl"
    logs_directory_name = "logs"

    current_time = datetime.now()
    full_file_name = file_name + "_" + str(current_time.month) + "_" + str(current_time.day) + "|" + str(current_time.hour) + ":" + str(current_time.minute) + "." + str(current_time.second) + "_" + file_extension


    results_directory = Path(logs_directory_name)
    results_directory.mkdir(parents=True, exist_ok=True)  # Create folder if it doesn't exist

# Define the file path
    file_path = results_directory / full_file_name

# Create a blank JSON file
    file_path.write_text("") 


    #full_path = os.path.join(results_directory_name, full_file_name)

#    try:
#        with open(full_path, "w"):
#            print("Json file " + full_path + " succesfully  created")
#    except Exception as e:
#        print(f"An unexpected error occurred: {e}")

    return file_path


def read_json(json_path):

    with open(json_path, "r") as file:

        read_data_list = []         #read data will be held in a list of dictionaries through of a search algorithm will be its on list inside the outer list to contain everything

        for line in file:
            try:
                read_data = json.loads(line)
                read_data_list.append(read_data)
                print(read_data)
            except json.JSONDecodeError as e:
                print(f"Skipping invalid JSON line: {line.strip()} - Error: {e}")

    return read_data_list

def write_json(json_path, sorting_log_data):

    try:
        with open(json_path, "w") as json_file:
            print("Json file " + str(json_file) + " succesfully  opened")
            json.dump(sorting_log_data, json_file)
            

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return


def append_json(json_path, data_to_append):
    
    try:
        with open(json_path, "a") as json_file:
            print("Json file " + str(json_file) + " succesfully  opened")
            json.dump(data_to_append, json_file)
            json_file.write("\n")
            

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return

def get_first_key(dictionary):
    for key in dictionary:
        return key
    raise IndexError

def print_all_dicts(list_of_dicts):

    for dict in list_of_dicts:
        print(dict)
    return
    

####Input Data Functions

""" name_of_algorithm, algo_index """
def start_log():

    full_log_key = CONST_NEWLOG_NAME
    log_dictionary = {full_log_key : []}


    return log_dictionary

def append_log(json_path, sort_dict, sort_step, sort_type, append_list_value):
    
    print(f"Sort Step {sort_step}")

    sort_step_string = str(sort_step)
    print(f"Sort Step String: {sort_step_string}")

    sort_key = sort_step_string + "_" + sort_type
    print(f"Sort Key: {sort_key}")

    #if sort_key not in sort_dict:
    #    sort_dict[sort_key] = []

    #first_key = list(sort_dict)[0]

    first_key = get_first_key(sort_dict)
    print(f"first_key:before: {first_key}")

    if(first_key == CONST_NEWLOG_NAME):
        sort_dict[sort_key] = sort_dict.pop(CONST_NEWLOG_NAME)

    #sort_dict[sort_key] = 

    first_key = get_first_key(sort_dict)
    print(f"first_key:after: {first_key}")
    #first_val = list(sort_dict.values())[0]
    #print(first_val)

    sort_dict[first_key] = append_list_value

    new_val = list(sort_dict.values())[0]

    new_dict_to_append = {sort_key : new_val}

    print(new_val)

    append_json(json_path,new_dict_to_append)

    #if isinstance(sort_dict.get(sort_key), list):
    
    #key_ref = sort_dict.get({sort_key:sort_list})
    #print(key_ref)

    #sort_dict[sort_key].append(sort_list)

    return sort_key


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

##Creates a new jsonl file log will be standard name along with time information automatically appended, second parameter 
new_json_path = create_json("log")
print(new_json_path)

#start log will create a new default jsonl entry
#new_log = start_log("merge", 00)
new_log = start_log()
print(new_log)


print("---------------------------\n")
#changes new_log to keep track of current status of  jsonl
new_key = append_log(new_json_path,new_log,0,"merge",[1,0,2,3,4,9])
print(new_log)

new_key = append_log(new_json_path,new_log,1,"merge",[0,1,2,3,4,9])
print(new_log)

new_key = append_log(new_json_path,new_log,2,"merge",[9,8,7,6,5,4,3,2,1])
print(new_log)

#read jsonl

read_dictionaries = read_json(new_json_path)
print("---------------------------\n")
print(read_dictionaries)

print("---------------------------\n")
print_all_dicts(read_dictionaries)





#write_json(new_json_path,new_log)