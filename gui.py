from tkinter import *
import random
import json_handler as jhandler
import algorithms as algo

_current_input = []
_num_of_algos = 5
_current_algos = [0] * _num_of_algos
_search_element = []

def modify_globals():
    global _current_input, _current_algos, _search_element

def submit_input():
    """Submit the user input and process it."""
    if v.get() == 1:    # If the user is choosing the input
        user_input = entry_field.get()
        try:
            # Convert the input string into a list of integers
            input_list = list(map(int, user_input.split()))

            #Collects data to be passed to controller loop -> handler -> visualizer
            algo_list_values_to_sort = input_list
            print(f"Value list: {algo_list_values_to_sort}")
            algos_to_use = get_algos_to_run(v_linear,v_bubble,v_merge, v_quick, v_radix)
            main_control(algos_to_use, algo_list_values_to_sort)
            
        except ValueError:
            print("Please enter valid integers.")
    elif v.get() == 2:  # If the user wants randomized values within a specific range
        try:
            min_value = int(min_entry.get())
            max_value = int(max_entry.get())
            number_of_elements = int(num_elements_entry.get())
            random_values = random.sample(range(min_value, max_value + 1), number_of_elements)

            algo_list_values_to_sort = random_values
            algos_to_use = get_algos_to_run(v_linear,v_bubble,v_merge, v_quick, v_radix)
            main_control(algos_to_use, algo_list_values_to_sort)

            # Populate the entry field with the generated random list
            entry_field.delete(0, END)  # Clear the existing text in the entry field
            entry_field.insert(0, " ".join(map(str, random_values)))  # Insert the random list into the entry field


            # Display Output on Terminal, can be redirected to a file
            print("Random List:", random_values)
        except ValueError:
            print("Please enter valid numbers for min, max, and number of elements.")


def generate_random_values():
    """Enable/disable random value entry fields based on the selection."""
    if v.get() == 2:
        min_entry.grid()  # Show randomizer fields
        max_entry.grid()
        num_elements_entry.grid()
        min_label.grid()
        max_label.grid()
        num_elements_label.grid()
    else:
        min_entry.grid_remove()  # Hide randomizer fields
        max_entry.grid_remove()
        num_elements_entry.grid_remove()
        min_label.grid_remove()
        max_label.grid_remove()
        num_elements_label.grid_remove()

#Should pass along values from the checkboxes to determine which algos to run when submit is hit
def get_algos_to_run(linear,bubble, merge, quick, radix):

    algos_to_run = [int(linear.get()),int(bubble.get()),int(merge.get()),int(quick.get()),int(radix.get())]

    print(f"Attempted conversion of bools to int: {algos_to_run}")

    return algos_to_run


def main_control(algorithms_to_run, value_to_sort):
    print(f"Values that will be sorted: {value_to_sort}")
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

    main_run_sorts(value_to_sort,algorithms_to_run,new_log,new_json_path,0)

    return 0

##Runs sorts based off of the input from the 
#sort input = list of values to be sorted
#algo_input = list of values to determine whether or not to run a given algorithm
#log = the dictionary thats acting as the current log to be written to
#json_log_path = path to the json log so program knows where it can access json
#linear_target = target if linear search to use if linear search is being used
#radix_exp = exponent to use if radix sort is being used

def main_run_sorts(sort_input, algo_input, log, json_log_path, linear_target):
    print("Checking to see which algorithm to run")
    original_sort_list = sort_input
    print(f"Algos to run: {algo_input}")

    if(algo_input[0] == 1):
        print("Executing Linear")
        algo.linear_search(sort_input,linear_target)
        sort_input = original_sort_list

    if(algo_input[1] == 1):
        print("Executing Bubble")
        algo.bubble_sort(sort_input,log,json_log_path)
        sort_input = original_sort_list

    if(algo_input[2] == 1):
        print("Executing merge")
        algo.merge_sort(sort_input, log,json_log_path)
        sort_input = original_sort_list

    if(algo_input[3] == 1):
        print("Executing Quick")
        algo.quick_sort_data_collect(sort_input,json_log_path)
        sort_input = original_sort_list

    if(algo_input[4] == 1):
        print("Executing Radix")
        algo.radix_sort(sort_input,json_log_path)
        sort_input = original_sort_list

    return


root = Tk()
root.title("Sorting Algorithm Project 1 Team 3")
root.geometry('700x550')

Label(root, text="Welcome to Our Sorting Algorithm Visualizer", font=("Courier New", 18, "bold"), wraplength=500, justify="center").pack()
Label(root, text="Please enter a list of values to store in the array! Example: 90 45 2 1", font=("Courier New", 16), wraplength=500, justify="center", fg="pink").pack()

v = IntVar()

main_frame = Frame(root)
main_frame.pack(pady=20)

Label(main_frame, text="Input Section", font=("Courier New", 15, "bold")).grid(row=0, column=0, columnspan=2)

# Asking user to choose input method
radio_manual = Radiobutton(main_frame, text="Enter your values", font=("Courier New", 14), variable=v, value=1)
radio_manual.grid(row=1, column=0, sticky="w")

radio_random = Radiobutton(main_frame, text="Generate random values", font=("Courier New", 14), variable=v, value=2, command=generate_random_values)
radio_random.grid(row=2, column=0, sticky="w")

# Entry field for user-chosen input
entry_field = Entry(main_frame, font=("Courier New", 14))
entry_field.grid(row=3, column=0, columnspan=2, pady=10)

# Corrected label placement (column 0 instead of 1)
find_value_label = Label(main_frame, text="Value to find (if needed):", font=("Courier New", 14))
find_value_label.grid(row=4, column=0, sticky="w", padx=5)

# Entry box remains in column 1
find_value_entry = Entry(main_frame, font=("Courier New", 14), width=10)
find_value_entry.grid(row=4, column=1, sticky="w", padx=5)


# Randomizer Entry Fields (will be shown when random option is selected)
min_label = Label(main_frame, text="Minimum Value:", font=("Courier New", 14), justify='left')
min_label.grid(row=4, column=0, sticky="w")

min_entry = Entry(main_frame, font=("Courier New", 14), width=4)
min_entry.grid(row=4, column=1)

max_label = Label(main_frame, text="Maximum Value:", font=("Courier New", 14))
max_label.grid(row=5, column=0, sticky="w")

max_entry = Entry(main_frame, font=("Courier New", 14), width=4)
max_entry.grid(row=5, column=1)

num_elements_label = Label(main_frame, text="Number of Elements:", font=("Courier New", 14))
num_elements_label.grid(row=6, column=0, sticky="w")

num_elements_entry = Entry(main_frame, font=("Courier New", 14), width=4)
num_elements_entry.grid(row=6, column=1)

# Initially hide randomizer fields
min_entry.grid_remove()
max_entry.grid_remove()
num_elements_entry.grid_remove()
min_label.grid_remove()
max_label.grid_remove()
num_elements_label.grid_remove()


v_linear = BooleanVar()
v_bubble = BooleanVar()
v_merge = BooleanVar()
v_quick = BooleanVar()
v_radix = BooleanVar()

algorithm_frame = Frame(root, bd=2, relief="solid", padx=10, pady=10)
algorithm_frame.pack(padx=20, pady=20)

linear_search = Checkbutton(algorithm_frame, text="Linear Search", font=("Courier New", 14), variable=v_linear)
# if linear search is selected, we need to get the target value so add a new box to choose target value that needs to be found
linear_search_target = Entry(algorithm_frame, font=("Courier New", 14), width=4)

linear_search.grid(row=0, column=0, sticky="w", padx=10, pady=5)

bubble_sort = Checkbutton(algorithm_frame, text="Bubble Sort", font=("Courier New", 14), variable=v_bubble)
bubble_sort.grid(row=0, column=1, sticky="w", padx=10, pady=5)

merge_sort = Checkbutton(algorithm_frame, text="Merge Sort", font=("Courier New", 14), variable=v_merge)
merge_sort.grid(row=0, column=2, sticky="w", padx=10, pady=5)

quick_sort = Checkbutton(algorithm_frame, text="Quick Sort", font=("Courier New", 14), variable=v_quick)
quick_sort.grid(row=1, column=0, sticky="w", padx=10, pady=5)

radix_sort = Checkbutton(algorithm_frame, text="Radix Sort", font=("Courier New", 14), variable=v_radix)
radix_sort.grid(row=1, column=1, sticky="w", padx=10, pady=5)

submit_button = Button(root, text="Submit", font=("Courier New", 14), command=submit_input)
submit_button.pack(pady=10)

root.mainloop()