# **Engeto_project_1: Task Manager**

## Creating a Program Using Python:
### Project Description:
In this project, the task was to create a Task Manager for managing tasks. The program should allow users to add, view, and delete tasks. Each function has a specific purpose, which is described below. All tasks are stored in the list ukoly = []. 

**def hlavni_menu()**  
This function displays the main menu, offering options to add, view, or delete a task. If the user enters an invalid option, the program notifies the user and prompts them to choose again.

**def pridat_ukol()**  
This function allows the user to enter the title and description of a new task and save it to the task list. This corresponds to option 1 in the main menu. After adding the task, the program continues by displaying the main menu again. If the user enters an empty input for Task title or Task description, the program notifies them and asks them to enter both fields again.

**def zobrazit_ukoly()**  
This function displays all tasks in the list. This corresponds to option 2 in the main menu. After displaying the tasks, the program continues by showing the main menu again.

**def odstranit_ukol()**  
This function allows the user to enter the number of the task they want to delete and removes that task from the list. This corresponds to option 3 in the main menu. After deleting the task, the program continues by displaying the main menu. The user must be able to see all existing tasks, and if they select a task that does not exist, the program must notify them.

If the user selects option 4, the program terminates.

## Test Cases:
### Project Description:
In the second part of the project, the goal was to create test cases for each function in the Task Manager project. These test cases should cover all possible execution paths as well as edge cases for each function. The test cases serve as a basis for automated tests or manual verification of program correctness. For each function (hlavni_menu, pridat_ukol, zobrazit_ukoly, odstranit_ukol), separate sets of test cases were created (positive, negative, boundary). Each test includes the following elements: Tested function, Test case name, Description, Preconditions, Test steps, Expected result, Actual result, Status, Notes, and Test type.
