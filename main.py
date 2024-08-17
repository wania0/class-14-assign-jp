# use hr_db;

# # Group BY
# # Write a query to get the number of employees who has the same job title.
# SELECT 
#     COUNT(EMPLOYEE_ID) AS number_of_employees, JOB_ID
# FROM
#     employees
# GROUP BY JOB_ID;

# # list down the lowest salary of the employee of every manager and also display the manager_id.
# SELECT 
#     MIN(SALARY) AS lowest_salary, MANAGER_ID
# FROM
#     employees
# GROUP BY MANAGER_ID;

# # list down the total salaries of every deparment # NOTE: salary should be in ascending order
# SELECT 
#     SUM(SALARY) AS total_salary, DEPARTMENT_ID
# FROM
#     employees
# GROUP BY DEPARTMENT_ID
# ORDER BY total_salary;

# # list down the average salaries of every department exluding IT Deparment
# SELECT 
#     AVG(SALARY) AS average_salary, JOB_ID
# FROM
#     employees
# WHERE
#     JOB_ID != 'IT_PROG'
# GROUP BY JOB_ID;

# # fetch the top 3 department who is taking the highest salary among all other deparment
# SELECT 
#     MAX(SALARY) AS maximum_salary, DEPARTMENT_ID
# FROM
#     employees
# GROUP BY DEPARTMENT_ID
# ORDER BY maximum_salary DESC
# LIMIT 3;


# -- # Write a query to get employee ID, last name, and date of first department (where he was working in, table name "job_history") of the employees."
# -- SELECT 
# --     e.EMPLOYEE_ID,
# --     e.LAST_NAME,
# --     MIN(jh.START_DATE) AS first_department_start_date
# -- FROM
# --     employees e
# --         LEFT JOIN
# --     job_history jh ON e.EMPLOYEE_ID = jh.EMPLOYEE_ID
# -- GROUP BY e.EMPLOYEE_ID , e.LAST_NAME;

# # find the department that contains more than 10 employees
# SELECT 
#     COUNT(*) AS employee_count, DEPARTMENT_ID
# FROM
#     employees
# GROUP BY DEPARTMENT_ID
# HAVING employee_count > 10;

# # Find the number of employees in each department.
# SELECT 
#     COUNT(*) AS number_of_employees, department_id
# FROM
#     employees
# GROUP BY department_id;

# -- Calculate the average salary for each job title.
# SELECT 
#     JOB_ID, AVG(SALARY)
# FROM
#     employees
# GROUP BY JOB_ID;

# -- List the total salary expenditure for each department.
# SELECT 
#     DEPARTMENT_ID, SUM(SALARY) AS total_salary
# FROM
#     employees
# GROUP BY DEPARTMENT_ID;

# -- Find the maximum salary in each department.
# SELECT 
#     DEPARTMENT_ID, MAX(SALARY) AS maximum_salaray
# FROM
#     employees
# GROUP BY DEPARTMENT_ID;

# -- Count the number of employees hired in each year.
# SELECT 
#     COUNT(*) AS employee_count, YEAR(HIRE_DATE) AS year
# FROM
#     employees
# GROUP BY YEAR(HIRE_DATE);

# -- Determine the number of employees with the same manager.
# SELECT 
#     MANAGER_ID, COUNT(*) AS employee_count
# FROM
#     employees
# GROUP BY MANAGER_ID;

# -- Find the average commission percentage for each department.
# SELECT 
#     DEPARTMENT_ID, AVG(COMMISSION_PCT) AS average_comission
# FROM
#     employees
# GROUP BY DEPARTMENT_ID;

# -- Calculate the total duration (in days) that each employee spent in their job(s) from the `job_history` table.

# -- Find the highest salary offered for each job title.
# SELECT 
#     JOB_ID, SUM(salary) AS highest_salary
# FROM
#     employees
# GROUP BY JOB_ID;

# -- join
# -- List all employees along with their department names.
# SELECT 
#     e.FIRST_NAME, e.LAST_NAME, d.DEPARTMENT_NAME
# FROM
#     employees AS e
#         JOIN
#     departments AS d ON e.DEPARTMENT_ID = d.DEPARTMENT_ID;

# -- Find all employees and their job titles.




