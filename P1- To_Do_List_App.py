# Project Number One #

###### To-Do list Application ###### 


#Welcomes User 
print("        Welcome, User!")
print("        ")
print("What would you like to do today?")

### Functions ###

class ToDoList:     
    
    def __init__(self):  
        self.tasks = []  
    
    def main_menu(self): # function to display the Main Menu 
        print("\n=== 'To-Do' List: Main Menu ===")  # Header of Main Menu
# Menu of choice of actions available for user to select by input of corresponding numerical entry
# Display of Main Menu options for user
        print("1. ADD a NEW task to 'To-Do' List")  
        print("2. VIEW task(s) on 'To-Do' List")  
        print("3. REMOVE/DELETE task(s) from 'To-Do' List")  
        print("4. QUIT the Application")  
    

# 
# Prompts AND validates user input. ADDS user input as a NEW TASK if input == valid. If invalid input, displays error message.
    def add_task(self):  
        task = input("Enter the NEW task to ADD to your list: ")  
        if task:
            try:  
                self.tasks.append(task) 
            finally:
                print(f"SUCCESS: Got it!'{task}' has been ADDED to the 'To-Do' List!") 
        else:                                  
            print("ERROR: Oops! Entry not recognized! Task name can not be blank and only consist of letters! ")  # Alert message to user for invalid input
            
 # Validates tasks list. If task list == valid, displays list. If invalid, displays error message.            
    def view_tasks(self):   
        if not self.tasks:  
            print("ERROR: Looks like there aren't any tasks are on to your 'To-Do' List yet! Add a task to get started!")  # Alerts user of no tasks to view
        else: 
            print("Here's your CURRENT TASKS on your 'To-Do' List:")  
            for i, task in enumerate(self.tasks, start=1):  
                print(f"{i}. {task}")   
                
                
# Validates task list. If task list == empty, displays error message. If task list == valid, displays numbered list, prompts for user input, validates the input, then removes item from task list based on user input, displays success message
    def delete_task(self): 
        if not self.tasks: 
            print("ERROR: Hmmm, your 'To-Do' List is empty. Can't DELETE/REMOVE a task that isn't there, silly!")
        if self.tasks:
            self.view_tasks()
            try:  
                task_number = int(input("Which task would you like to DELETE/REMOVE? (Enter the number that corresponds to the task you want to delete):  "))  
                if 1 <= task_number <= len(self.tasks):  
                    removed_task = self.tasks.pop(task_number - 1)  
                    print(f"SUCCESS:'{removed_task}' has been REMOVED/DELETED. Phew, one less thing to worry about!")
                else:
                    print("ERROR: Hmmm, that number doesn't match any task on this 'To-Do' List.")  # Alerts user that they're trying to delete a task that doesn't exist
            except ValueError: 
                print("ERROR: Ooops! That doesn't make sense! PLease enter a number next time!")

                                   
                                   
                                    ### CALLING FUNCTIONS ###
                                    
                                    
# Main Loop
    def main(self):   
        while True:  
            self.main_menu()  
            try:  
                choice = int(input("Enter the number that corresponds to the desired action (1-4): "))
                if choice == 1:  
                    self.add_task() 
                elif choice == 2:  
                    self.view_tasks()  
                elif choice == 3:  
                    self.delete_task()  
                elif choice == 4:  
                    print("Exiting the application. See you later!")  
                    break  
                else:  
                    print("ERROR: Invalid choice. Please choose a valid option.")  # Alerts user that they selected an option on Main Menu that doesnt exist
            except ValueError:  
                print("ERROR: Entry does not exist. Please enter numerical values only!") 

if __name__ == "__main__":  
    todo_list = ToDoList()  
    todo_list.main()  