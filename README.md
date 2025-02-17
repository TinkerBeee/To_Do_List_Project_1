# To-Do List Application

## Project Description
A simple 'To-Do' List application that allows users to add a new task(s), delete task(s), and view task(s). 

#### What does it do?
     = This application allows users to do the following:
        1. Add new tasks
        2. View the previously added tasks in a numbered list in order, with first task as #1
        3. Delete tasks based om user selection
        4. Exit the app    
        
     - This aplication also alerts users at the appropriate time when/if:
        1. Invalid input is entered
        2. There are no tasks to view or delete
        3. The user tries to delete a task that does not exist on the list 
        4. The user tries to select an option on the Main Menu that does not exist
    
#### Technology Used    
    This project was built using Python 3.13 to help me strenghten my understanding of Python Concepts 
    such as syntax, data types, control structures, functions, and error handling,
    all while creating a practical, interactive command line application.  
   

## How To Run
    1. Ensure Python 3 is installed on device
    2. Download ['To-do' List App Python file](https://github.com/TinkerBeee/To_Do_List_Project_1/blob/main/Project%201-%20To-Do%20List.py)
    3. Open file in Python

## How To Use
    
    STARTING FROM THE MAIN MENU: 
    
     - To ADD a task:
                1. Input the number '1' using keypad
                2. Press the 'Enter' key on keypad
                3. When prompted, type the name of the task to be added using keypad
                4. Press the 'Enter' key on keypad
        * If task was ADDED successfully, you'll see a success message AFTER pressing 'Enter' on step 4. 
        * If invalid input was entered, you'll get an ERROR message AFTER pressing 'Enter' on step 4
            
    - To VIEW current task(s): 
                1. Input the number '2' using keypad 
                2. Press the 'Enter' key on keypad
                3. Current tasks that have been previously added will be displayed in a numbered list. 
                       ** The tasks will be organized in the order they were added. (First task being #1.) 
                       ** If there are no tasks on the list, you'll get an ERROR message
               
    - To REMOVE/DELETE a task:
                1. Input the number '3' using keypad
                2. Press the 'Enter' key on keypad
    * If task list is empty, you'll recieve an ERROR message here- (AFTER pressing 'Enter' key on step 2)
    * If one or more tasks are present on the list, all current tasks will now be displayed &
        user will now be prompted to enter the number that corresponds with the task to be deleted 
                3. Follow the prompt instructions and enter the corresponding number using the keypad
                4. Press the 'Enter' key on the keypad
                        * If task DELETE/REMOVE was successful, you'll see a SUCCESS message after step 4
                        * If invalid input was entered, you'll see an ERROR message after step 4 
        
                            Example of REMOVE/DELETE task number 2: 
                                 **Display of Task list:** 
                                    [1.] Take out trash
                                    [2.] Walk the Dog
                                    [3.] Schedule dentist appointment   
         *** To DELETE/REMOVE task number [2.] Walk the dog:
                1. Input the number '2' using keypad 
                2. Press the 'Enter' key on keypad
                3. When prompted to "enter the number that corresponds with the task to be deleted", 
                   input the number '2' using keypad.  
                4. Press the 'Enter' key on the keypad
                          * SUCCESS message that task was DELETED/REMOVED  
                    

        - To EXIT application: 
            1. Input the number '4' using keypad
            2. Press the 'Enter' key on keypad
            3. You'll see a Goodbye message and application will close.

## Credits
    TinkerBeee (myself)
            &
    The Coding Temple Curriculum for inspiration 
                
                
                    
        
