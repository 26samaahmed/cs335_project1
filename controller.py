import json_handler as jhandler
import algorithms as algo
import gui as ui


def main_control():

    """ json_log_path = jhandler.create_json("log")
    print(f"New log's path: {json_log_path}")

    new_log = jhandler.start_log()
    print(new_log)

    new_key = algo.bubble_sort(algo.random_input(),new_log,json_log_path)
    print(new_key)

    print(new_log) """


    new_json_path = jhandler.create_json("log")     #creates the new log to be written to
    print(f"New json path: {new_json_path}")

    new_log = jhandler.start_log()
    print(new_log)

    main_run_sorts(ui.input,ui.algos,new_log,new_json_path,0)

    return 0

##Runs sorts based off of the input from the 
#sort input = list of values to be sorted
#algo_input = list of values to determine whether or not to run a given algorithm
#log = the dictionary thats acting as the current log to be written to
#json_log_path = path to the json log so program knows where it can access json
#linear_target = target if linear search to use if linear search is being used
#radix_exp = exponent to use if radix sort is being used

def main_run_sorts(sort_input, algo_input, log, json_log_path, linear_target):
    original_sort_list = sort_input

    if(algo_input[0] == 1):
        algo.linear_search(sort_input,linear_target)
        sort_input = original_sort_list

    if(algo_input[0] == 1):
        algo.bubble_sort(sort_input,log,json_log_path)
        sort_input = original_sort_list

    if(algo_input[0] == 1):
        algo.merge_sort(sort_input)         #merge sort parameters need to be updated - TODO
        sort_input = original_sort_list

    if(algo_input[0] == 1):
        algo.quick_sort_data_collect(sort_input,json_log_path)
        sort_input = original_sort_list

    if(algo_input[0] == 1):
        algo.radix_sort(sort_input,json_log_path)
        sort_input = original_sort_list

    return


###################Main Block########################
