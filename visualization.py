# visualizations.py
# Graph Developer: Alex Islas
# Date: 2-25-25
# Purpose: Generates an animated bar graph demonstrating the step-by-step progression of a sorting algorithm
#          on a user-provided input array, with built-in start, pause/resume, and reset buttons.

import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive widgets
import matplotlib.pyplot as plt         # Import Matplotlib for creating the animated bar graph
from matplotlib.animation import FuncAnimation  # Import for animating the sorting process
from matplotlib.widgets import Button   # Import for adding interactive buttons
import tkinter as tk                    # Import Tkinter for managing the event loop

def plot_sorting_animation(algo_name, algo_func, arr):

    # Create a Tkinter root window to manage the event loop
    root = tk.Tk()   # Create a Tkinter root window
    root.withdraw()  # Hide the root window
    
    # Create a figure and axis for the animation
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Initialize the bars with the input array values
    bars = ax.bar(range(len(arr)), arr, color='skyblue', edgecolor='black', linewidth=1)
    
    # Set axis labels and title
    ax.set_xlabel("Index", fontsize=14, labelpad=10)
    ax.set_ylabel("Value", fontsize=14, labelpad=10)
    ax.set_title(f"{algo_name} Sorting Process", fontsize=16, pad=15)
    
    # Add a light grid for readability
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, max(arr) * 1.2) # Set y-axis limit with padding
    
    # Store the original array and current state
    original_arr = arr.copy()
    current_arr = arr.copy()
    
    # Animation state variables
    paused = False  # Start paused
    
    # Define the update function for the animation
    def update(frame):
        nonlocal current_arr
        current_arr = frame               # Update the current array state
        for bar, val in zip(bars, frame): # Update bar heights
            bar.set_height(val)
        fig.canvas.draw()                 # Redraw the figure
        fig.canvas.flush_events()         # Ensure the canvas is updated
        return bars
    
    # Create animation with initial generator, paused
    generator = algo_func(current_arr.copy())
    anim = FuncAnimation(fig, update, frames=generator, save_count=len(arr)*(len(arr)-1)//2,
                         repeat=False, interval=3000, blit=False)
    anim.event_source.stop()  # Start paused

    # Button callback functions
    def start(event):
        nonlocal paused
        print("Start button clicked")
        if paused:
            anim.event_source.start() # Start the animation
            paused = False            # Set animation state to running
            pause_button.label.set_text("Pause")

    def pause_resume(event):
        nonlocal paused
        print("Pause/Resume button clicked")
        if paused:                       # If animation is paused
            anim.event_source.start()    # Start the animation
            pause_button.label.set_text("Pause")
            paused = False              # Set animation state to running
            print("Resumed animation")
        else:                            # If animation is running
            anim.event_source.stop()     # Stop the animation
            pause_button.label.set_text("Resume")
            paused = True                # Set animation state to paused
            print("Paused animation")

    def reset(event):
        nonlocal paused, current_arr
        print("Reset button clicked")
        anim.event_source.stop()             # Stop the animation
        current_arr = original_arr.copy()        # Reset the array
        for bar, val in zip(bars, original_arr): # Reset bar heights
            bar.set_height(val)
        generator = algo_func(current_arr.copy())  # New generator for reset state
        anim._init_func = lambda: bars            # Reset initialization
        anim._iter_gen = lambda: iter(generator)  # Reset generator
        paused = True
        pause_button.label.set_text("Resume")
        fig.canvas.draw()                          # Redraw the figure
    
    # Buttons to plot
    ax_start = plt.axes([0.6, 0.01, 0.1, 0.05])
    ax_pause = plt.axes([0.71, 0.01, 0.1, 0.05])
    ax_reset = plt.axes([0.82, 0.01, 0.1, 0.05])

    start_button = Button(ax_start, 'Start')
    pause_button = Button(ax_pause, 'Resume') # Starts as resume since its paused
    reset_button = Button(ax_reset, 'Reset')

    # Connect buttons
    start_button.on_clicked(start)
    pause_button.on_clicked(pause_resume)
    reset_button.on_clicked(reset)

    fig.canvas.mpl_connect('close_event', lambda event: root.quit()) # Close tkinker when closed
    plt.show()
    root.mainloop() # Start Tkinter event loop

    # Return figure and animation objects
    return fig, anim


### ------- TESTS, GENERATED BY AN AI FOR TESING -------- ###
# --- Test Case ---
if __name__ == "__main__":
    def mock_bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    yield arr

    test_arr = [5, 3, 8, 1, 9, 2, 10, 4, 7, 6]
    test_algo_name = "Bubble Sort"

    print("Generating animated bar graph for", test_algo_name)
    fig, anim = plot_sorting_animation(test_algo_name, mock_bubble_sort, test_arr)

    if fig:
        plt.figure(fig.number)
        plt.show(block=True) # Change block to true to keep the plot open until you close it
    else:
        print("Animation generation failed.")

    print("Test case completed. Animation should run until finished or window closed!")