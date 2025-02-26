import json_handler as jhandler
import algorithms as algo


def main_control():

    json_log_path = jhandler.create_json("log")
    print(f"New log's path: {json_log_path}")

    new_log = jhandler.start_log()
    print(new_log)

    new_key = algo.bubble_sort(algo.random_input(),new_log,json_log_path)
    print(new_key)

    print(new_log)


    return 0


###################Main Block########################


main_control()
