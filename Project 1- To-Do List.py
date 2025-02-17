class ToDoList:  
    
                        ### DEFINING FUNCTIONS ###
    def __init__(self):  
        self.tasks = []  
        

    def main_menu_options(self): # function to display the Main Menu 
        print("_____________________________")  
        print("\n=== To-Do List: Main Menu ===")  # Header of Main Menu
        print("_____________________________")
        print("")
        print("What would you like to do?")  
# Menu of choice of actions available for user to select by input of corresponding numerical entry
# Display of Main Menu options for user
        print("1. ADD a Task to the 'To-Do' List")  
        print("2. VIEW all Tasks on the 'To-Do' List")  
        print("3. DELETE a Task from the 'To-Do' List")  
        print("4. QUIT the Application")  
        print("_____________________________")  # End of Main Menu options


    def add_task(self):  # function to 'Add new task' 
        task = input("Enter the NEW task you wish to ADD: ")  # Prompts for user input of any value to 'Add a task'
        if task:              # checks if user input == valid 
            self.tasks.append(task)  # Adds new task 
            print(f"Success!'{task}' has been ADDED to the 'To-Do' List!")  # Display of new task added success message 
        else:                                   # if user input == no entry/invalid entry:
            print("ERROR: Entry not recognized!")  # Display of error message 
            
            
    def view_tasks(self):   # function to display current tasks  
        if not self.tasks:  # If 0 task(s) are on list:
            print("ERROR: Sorry, 0 tasks to VIEW on the 'To-Do' List!")  # Display of error message 
            print("Possible reasons for 0 task(s) on 'To-Do' List include:") 
            print("[1] = No task(s), or (0) task(s) have been ADDED to the 'To-Do' List") 
            print("[2] = ALL task(s) have been DELETED/REMOVED from 'To-Do' List") 
        else:  # If there is at least 1 task on list:
            print("Task List:")  # Header for the list of tasks to be displayed
            for i, task in enumerate(self.tasks, start=1):  # Defines the specific tasks to display starting with the first task (all)
                print(f"{i}. {task}")   # display format 

    def delete_task(self): # function to 'Delete Task' 
        if not self.tasks:  # If 0 task(s) on list:
            print("ERROR: Sorry, there are 0 tasks to DELETE from the 'To-Do' List!")
            print("Possible reasons for 0 task(s) on 'To-Do' List include: ") # Display of error message 
            print("[1] = 0 task(s) have been ADDED to the 'To-Do' List ") 
            print("[2] = ALL task(s) have been DELETED/REMOVED from 'To-Do' List")  
        else:  # If there is one or more task(s):
            self.view_tasks()  # Displays all tasks to the user (in a list format)
            try:  
                task_number = int(input("Enter the number that corresponds to the task that you wish to REMOVE/DELETE: "))  # Prompts user to enter the number that corresponds with the task to be deleted/removed
                if 1 <= task_number <= len(self.tasks):  # Checks that input == valid. Valid input == at least 1 and no higher number than the actual number count of tasks (ex: 5 tasks, makes sure that only a '1', '2', '3', '4', or '5' is entered )
                    task = self.tasks.pop(task_number - 1)  # removes task if the user input == valid. (Ex: There are 4 tasks, task #2 == task to be deleted. User input == 2. This deletes task #2)
                    print(f"Success!'{task}' has been REMOVED/DELETED from the 'To-Do' List!")  # Display of success message for deleted task
                else:    
                    print("ERROR: The task number that you entered does not exist!")  # Display of error message when input == number that does not correspond with a task (ex: There are 4 tasks, input value == 5.)
            except ValueError:  # If the wrong value type was entered for user input (Ex: user input == D, when only numerical values are accepted, specifically only '1', '2', '3', and '4')
                print("ERROR: ERROR: Invalid Entry- Numerical values only!")  # Display of error message when input is not a numerical value

### CALLING FUNCTIONS ###
# Main Loop
    def main(self):    # calling main function   
        while True:  # infinate loop until break
            self.main_menu_options()  # show Main Menu options
            try:  
                choice = int(input("Enter the number that corresponds to the desired action (1-4): ")) # prompts user to enter their choice of 1-4, depending on the desired action to be taken, valid input == single numerical value (1, 2, 3, or 4)
                if choice == 1:  
                    self.add_task() # calls function- add a task 
                elif choice == 2:  
                    self.view_tasks()  # calls function- displays current tasks
                elif choice == 3:  
                    self.delete_task()  # calls function- deletes a single task 
                elif choice == 4:  
                    print("Exiting the application. Goodbye!")  # Displays Goodbye message
                    break  # Stops loop
                else:  
                    print("Invalid choice. Please choose a valid option.")  # Display of error message when entry is invalid
            except ValueError:  
                print("Entry does not exist. Please enter numerical values only!") # Display of error message when anything other than a number is entered

if __name__ == "__main__":  
    todo_list = ToDoList()  
    todo_list.main()  