
**Database Bonus Calculator**

This Python script provides functionality for calculating and displaying total bonuses for users based on a SQLite database. It consists of two main parts:

1. **Database Initialization and Data Insertion**: 
   - Checks if the SQLite database file `bonus.db` exists; if not, it creates it.
   - Defines two tables, `users` and `department`, if they don't already exist.
   - Inserts sample data into the `users` and "department" tables.

2. **Bonus Calculation**:
   - Connects to the SQLite database.
   - Executes a SQL query that calculates the total bonus for each user based on their salary and department's bonus rate.
   - Displays the results in descending order of total bonus.


