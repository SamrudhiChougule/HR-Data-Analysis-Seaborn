HR Data Analysis Using Seaborn:.

Using Seaborn and Matplotlib to efficiently draw insights from HR data by plotting different types of graphs and charts.

Dataset:.

Source: HR Data for an MNC (employee details including department, salary, performance, and work mode).

This project analyzes employee data to identify workforce distribution, salary structures, performance trends, and anomalies that may indicate potential fraud or irregularities.

Setup:.

Place the dataset file (hr_data_mnc.csv) in the project root folder.

Install required libraries:.

pip install -r requirements.txt


(requirements.txt should include pandas, seaborn, matplotlib, numpy)

Run the notebook:.

Open HR_Analysis.ipynb in Jupyter Notebook or VS Code.

Execute all cells to generate the visualizations.

Outputs

Figures: outputs/figures/*.png (10 visualization plots)

Jupyter Notebook: HR_Analysis.ipynb (with all code)

Dataset: hr_data_mnc.csv

Visualizations
1. Number of Employees by Department
![Alt Text](outputs\1_Employees_by_Department.png)

Summary: Shows how employees are distributed across departments. IT and HR dominate, while R&D has the fewest employees.

2. Salary Distribution of Employees
![Alt Text](outputs\2_Salary_Distribution_of_Employees.png)


Summary: Most employees earn between 5–10 LPA. Outliers above 20 LPA may need verification.

Identifies common job roles. Helps detect unrealistic or duplicate job titles that may indicate bad records.

3. Work Mode Distribution
![Alt Text](outputs\3_Work_Mode_Distribution.png)

Summary: Shows workforce distribution across locations. Some locations have very few employees, which can be flagged as anomalies.

4. Employee performance ratings 
![Alt Text](outputs\4_Employee_Performance_Ratings.png)

Summary: Most of the employees have the ratings as 1 while 80 to 85 have the 5 ratings.

5. Average Salary by Department
![Alt Text](outputs\5_Average_salary_by_department.png)

Summary: IT nand Finance stand among the highest salary holders while Marketing,HR,Sales have the almost same salary with R&D as the lowest 

6. Salary Distribution by performance rating
![Alt Text](outputs\6_Salary_Distribution_by_Performance_Rating.png)

Summary: Higher performers generally earn more. However, some low-rated employees with very high salaries may be suspicious.

7. Experience vs Salary (by Department)
![Alt Text](outputs\7_Experience_vs_Salary_(by_Department).png)

Summary: IT employees hold the position of highest earners followed by finance followed by sales , rest have the same level of salary while r&d as lowest 

8. Salary Distribution across Work Modes
![Alt Text](outputs\8_Salary_Distribution_across_Work_Modes.png)

Summary: Onsite employees tend to earn slightly more than remote/hybrid. Sharp salary differences may indicate irregularities.

9. Performance Ratings across Departments
![Alt Text](outputs\9_Performance_Ratings_across_Departments.png)

Summary: Highest ratings are earned by sales department followed by operations department while at least position stand R&D AND HR.

10. Correlation Heatmap (Salary, Experience, Performance
![Alt Text](outputs\10_CORRELATION.png)

Summary: Strong positive correlation between salary and experience. Weak correlation with performance rating suggests pay may not always reflect performance.

Notes

Only the first 500 rows of the dataset were used for faster analysis.

Outliers and anomalies highlighted may indicate possible fraudulent or incorrect data entries.

Plots use consistent color schemes and formatting for presentation quality.

Technical Details

Data Processing: pandas

Visualization: Seaborn + Matplotlib

Output Format: High-resolution PNGs suitable for reports and presentations

About

This project demonstrates how data visualization can reveal important insights from HR datasets, helping companies detect anomalies and make better workforce decisions.