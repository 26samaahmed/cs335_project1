#Author: Robbie Robertson
#Date: 02/22/25
#Class: Algorithm Engineering
#Purpse: File holds sorting funcitons and pushes data to json_handler


import random
import time
import json_handler as jhandler

###########################
####Sorting Algorithms#####

#Sorting algorithms must save/capture this data:
#   -list
#   -step(index)
#   -time stamp for each step

#-------------------------------------------------

#Bubble Sort
#Data Collection Functionality -DONE

def bubble_sort(value_list,log, json_log_path):
    print(f"Bubble Sort start: {value_list}")

    n = len(value_list)

    current_sort_data = {}

    start_time = time.time()
    current_runtime = 0
    step_count = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            step_count += 1

            if value_list[j] > value_list[j + 1]:  # Compare integers directly
                    value_list[j], value_list[j + 1] = value_list[j + 1], value_list[j]

            current_runtime = time.time() - start_time
            jhandler.append_log(json_log_path,log, step_count,"bubble",current_runtime, value_list)      #Records data here

    print(f"Bubble Sort end: {value_list}")


#-------------------------------------------------
#-------------------------------------------------


#Merge Sort
#Data Collection Functionality - TODO
def merge_sort_orig(value_list,log,json_log_path,):

    current_sort_data = {}

    start_time = time.time()
    current_runtime = 0


    if len(value_list) > 1:
        mid = len(value_list) // 2 #Find the middle index
        left_half = value_list[:mid] #Divide list into halves
        right_half = value_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        current_runtime = time.time() - start_time
        jhandler.append_log(json_log_path,log, i,"bubble",current_runtime, value_list)      #Records data here, original value order

        while i < len(left_half) and j < len(right_half):

            if left_half[i][1] < right_half[j][1]:
                value_list[k] = left_half[i]
                i += 1
            else:
                value_list[k] = right_half[j]
                j += 1
            k += 1

            current_runtime = time.time() - start_time
            jhandler.append_log(json_log_path,log, i,"bubble",current_runtime, value_list)      #Records data here

        while i < len(left_half):
            value_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            value_list[k] = right_half[j]
            j += 1
            k += 1



def merge_sort(value_list, log, json_log_path, start_time=None):
    if start_time is None:
        start_time = time.time()  # Initialize start time only once

    if len(value_list) > 1:
        mid = len(value_list) // 2
        left_half = value_list[:mid]
        right_half = value_list[mid:]

        # Log before splitting
        current_runtime = time.time() - start_time
        jhandler.append_log(json_log_path, log, -1, "mergesplit", current_runtime, value_list)

        merge_sort(left_half, log, json_log_path, start_time)
        merge_sort(right_half, log, json_log_path, start_time)

        i = j = k = 0

        # Log before merging two halves
        current_runtime = time.time() - start_time
        jhandler.append_log(json_log_path, log, -1, "mergestart", current_runtime, value_list)

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                value_list[k] = left_half[i]
                i += 1
            else:
                value_list[k] = right_half[j]
                j += 1
            k += 1

            # Log during merging step
            current_runtime = time.time() - start_time
            jhandler.append_log(json_log_path, log, k, "mergecombine", current_runtime, value_list)

        while i < len(left_half):
            value_list[k] = left_half[i]
            i += 1
            k += 1

            # Log remaining elements from left half
            current_runtime = time.time() - start_time
            jhandler.append_log(json_log_path, log, k, "mergeleft", current_runtime, value_list)

        while j < len(right_half):
            value_list[k] = right_half[j]
            j += 1
            k += 1

            # Log remaining elements from right half
            current_runtime = time.time() - start_time
            jhandler.append_log(json_log_path, log, k, "mergeright", current_runtime, value_list)

        # Log after full merge
        current_runtime = time.time() - start_time
        jhandler.append_log(json_log_path, log, -1, "mergecomplete", current_runtime, value_list)



#-------------------------------------------------
#-------------------------------------------------


#Quick Sort
#Data Collection functionality - TODO
def quick_sort(arr, side_string, step, start_time, json_log_path):

    current_sort_data = {}

    current_runtime = (time.time()) - start_time

    step += 1

    sort_type_string = "quick-" + side_string

    current_sort_data = jhandler.pack_data(step, sort_type_string, current_runtime, arr)
    jhandler.append_json(json_log_path, current_sort_data)

    if len(arr) <= 1:
        return arr
    

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left, "left", step, start_time,json_log_path) + middle + quick_sort(right, "right", step, start_time,json_log_path)


def quick_sort_data_collect(arr,json_log_path):

    start_time = time.time()

    quick_sort_result = quick_sort(arr, "start" , 0, start_time,json_log_path)

    total_runtime = (time.time()) - start_time

    current_sort_data = jhandler.pack_data(999,"quick-complete",  total_runtime, quick_sort_result)
    jhandler.append_json(json_log_path,current_sort_data)

    return 

#-------------------------------------------------
#-------------------------------------------------
#Radix Sort
def counting_sort(arr, exp):


    

    n = len(arr)
    output = [0] * 10
    count = [0] * 10

    #Count occurences of each digit in the current place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    #Update count [i] so that it contains actual position in the output []
    for i in range(1, 10):
        count[i] += count[i-1]  #Cumulative sum for stable sorting

    
    #Build the output array by placing elements in correct order
    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1   #Decrement count to handle duplicates


    #Copy sorted output back to the original array
    for i in range(n):
        arr[i] = output[i]  #Overwrite original array with sorted values


def radix_sort(arr,json_log_path):
    #Least significant Digit Approach (LSD)
    #Find the maximum number to determine the number of digits
    max_num = max(arr)
    exp = 1


    #Step for logging data for the first step
    current_sort_data = {}

    start_time = time.time()
    current_runtime = 0

    step_count = 0
    total_time = 0

    current_sort_data = jhandler.pack_data(step_count,"radix", 0 ,arr)
    jhandler.append_json(json_log_path,current_sort_data)


    #Continue sorting for each digit place value
    while max_num // exp > 0:
        counting_sort(arr,exp)
        exp *= 10

        #Step for logging data for all iterations of radix sort
        step_count += 1
        total_time = (time.time()) - start_time

        current_sort_data = jhandler.pack_data(step_count, "radix",total_time,arr)
        jhandler.append_json(json_log_path,current_sort_data)
    return arr


#-------------------------------------------------
#-------------------------------------------------
#Linear Search Algorithm
def linear_search(L, T):
    for index in range(len(L)):
        if L[index] == T:
            return index
    return -1

def linear_search_data_collect(list, target_element,json_log_path):

    start_time = time.time()
    search_result = linear_search(list,target_element)
    end_time = time.time()
    run_time = end_time - start_time

    data_tuple = (run_time, search_result, list)

    jhandler.pack_data(search_result, "linear" ,run_time, list)         #for linear search we will replace the step with the index of the succesful 
    jhandler.append_json(json_log_path,list)

    return  data_tuple

#-------------------------------------------------
#-------------------------------------------------


####Testing Function

##Generates a random list(of random size 0 - 98) of integers to be sorted
def random_input():
    randomly_generated_input_values = []

    random_size = random.randint(0,98)

    for i in range(random_size):
        randomly_generated_input_values.append(random.randint(0,100))

    return randomly_generated_input_values