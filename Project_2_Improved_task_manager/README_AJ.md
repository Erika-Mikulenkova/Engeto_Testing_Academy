# **Engeto_Project_2: Improved Task Manager**

## Part 1 - Task manager improvement:
### Project Description:
The goal of this project was to improve the task manager from the first project so that tasks are no longer stored in an in-memory list but are instead stored in a MySQL database. The program will perform CRUD operations (Create, Read, Update, Delete). After completing the project, you will write automated tests using pytest and MySQL Workbench.

### Project Requirements:
Use of a MySQL database: Create a database table ukoly that contains: id, name, description, status (not started, completed, in progress), and creation date. You must also create the database itself where the table ukoly will be stored.

### Program Functions:
**pripojeni_db()** - Database connection  
- This function creates a connection to the MySQL database.  
- If the connection fails, it displays an error message.  

**vytvoreni_tabulky()** - Create the table if it does not exist  
- This function creates the table ukoly if it does not already exist.  
- It verifies whether the table exists in the database.  

**hlavni_menu()** – Main menu, which displays the following options:  
1. Přidat úkol (Add task)  
2. Zobrazit úkoly (Show tasks)  
3. Aktualizovat úkol (Update task)  
4. Odstranit úkol (Delete task)  
5. Ukončit program (Exit program)  

- If the user enters an invalid option, the program notifies them and asks for a new selection.

**pridat_ukol()** – Add a task  
- The user enters the task name and description.  
- Required fields: Both name and description are mandatory and cannot be empty.  

Automatic values:  
    1. The task receives its ID automatically.  
    2. Default task status: Nezahájeno (Not started)  

- After all conditions are met, the task is saved to the database.

**zobrazit_ukoly()** – Display tasks  
- Displays a list of all tasks, including: ID, name, description, status.  
- Filter: Shows only tasks with the status "Nezahájeno" (Not started) or "Probíhá" (In progress).  
- If there are no tasks, a message is shown indicating that the list is empty.
  
**aktualizovat_ukol()** – Update task status  
- The user sees a list of tasks (ID, name, status).  
- They select a task by ID.  
- They choose a new status: "Probíhá" (In progress) or "Hotovo" (Completed).  
- After confirmation, the database is updated.  
- If the user enters a non-existent ID, the program warns them and asks again.

**def odstranit_ukol()** – Delete a task  
- The user sees the list of tasks.  
- They select a task by ID.  
- After confirmation, the task is permanently removed from the database.  
- If the user enters a non-existent ID, the program warns them and asks again.

## Part 2 - Automated Tests:
### Project Description:
The second task is to write automated tests for the task manager that works with a MySQL database. The tests will verify the correct functionality of adding, updating, and deleting tasks using pytest. The tests will work with a test database. Test data will be added dynamically. The test data should also be removed afterwards — tests must not permanently change the database (test data is deleted after each test).
Each function has two tests:  
1. Positive test – Verifies correct functionality.     
2. Negative test – Verifies how the program reacts to invalid input.
