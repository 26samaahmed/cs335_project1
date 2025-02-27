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
    

    for i in range(n):

        #Record data here
        current_runtime = time.time()
        #current_sort_data = jhandler.pack_data(i,"bubble",(current_runtime - start_time), students)
        jhandler.append_log(json_log_path,log, i,"bubble", value_list)

        for j in range(0, n - i - 1):
            if value_list[j] > value_list[j + 1]:  # Compare integers directly
                    value_list[j], value_list[j + 1] = value_list[j + 1], value_list[j]

    print(f"Bubble Sort end: {value_list}")

"""             if students[j][1] > students[j+1][1]:
                students[j], students[j + 1] = students[j + 1], students[j] """




#-------------------------------------------------
#-------------------------------------------------


#Merge Sort
#Data Collection Functionality - TODO
def merge_sort(flights):

    current_sort_data = {}

    start_time = time.time()
    current_runtime = 0


    if len(flights) > 1:
        mid = len(flights) // 2 #Find the middle index
        left_half = flights[:mid] #Divide list into halves
        right_half = flights[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                flights[k] = left_half[i]
                i += 1
            else:
                flights[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            flights[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            flights[k] = right_half[j]
            j += 1
            k += 1


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