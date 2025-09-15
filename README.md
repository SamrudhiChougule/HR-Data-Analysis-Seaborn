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

Visualizations:.
1. Number of Employees by Department
   <img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/b50ee2f3-4fea-4489-b23c-a1e309088ff3" />



Summary: Shows how employees are distributed across departments. IT and HR dominate, while R&D has the fewest employees.

2. Salary Distribution of Employees
   <img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/b08248e5-195c-4d7b-a5e6-97e571840967" />




Summary: Most employees earn between 5–10 LPA. Outliers above 20 LPA may need verification.

Identifies common job roles. Helps detect unrealistic or duplicate job titles that may indicate bad records.

3. Work Mode Distribution
   <img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/cd70aa05-fa1b-4bfe-b04d-fe82a7c7a870" />



Summary: Shows workforce distribution across locations. Some locations have very few employees, which can be flagged as anomalies.

4. Employee performance ratings
   <img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/a4875a16-1d52-44d3-a331-ac1a71272497" />



Summary: Most of the employees have the ratings as 1 while 80 to 85 have the 5 ratings.

5. Average Salary by Department
   <img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/67a20712-4252-4b51-b376-2fcb02a4c637" />



Summary: IT nand Finance stand among the highest salary holders while Marketing,HR,Sales have the almost same salary with R&D as the lowest 

6. Salary Distribution by performance rating
   <img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/42a65dad-83d4-4ce3-9196-312efdae0e14" />



Summary: Higher performers generally earn more. However, some low-rated employees with very high salaries may be suspicious.

7. Experience vs Salary (by Department)
   <img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/e27297de-bf2d-40e1-9ad0-b4e1ff6cb840" />



Summary: IT employees hold the position of highest earners followed by finance followed by sales , rest have the same level of salary while r&d as lowest 

8. Salary Distribution across Work Modes
   <img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/f80ee794-f9c9-4106-bf53-c0a70eea6b6d" />



Summary: Onsite employees tend to earn slightly more than remote/hybrid. Sharp salary differences may indicate irregularities.

9. Performance Ratings across Departments
    <img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/ba7bec3b-a2d8-4f38-8016-9947ef91df11" />



Summary: Highest ratings are earned by sales department followed by operations department while at least position stand R&D AND HR.

10. Correlation Heatmap (Salary, Experience, Performance)
    <img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/e53e37ce-3653-4b01-b4aa-cf1a3d8ac425" />



Summary: Strong positive correlation between salary and experience. Weak correlation with performance rating suggests pay may not always reflect performance.

Notes:

Only the first 500 rows of the dataset were used for faster analysis.

Outliers and anomalies highlighted may indicate possible fraudulent or incorrect data entries.

Plots use consistent color schemes and formatting for presentation quality.

Technical Details:

Data Processing: pandas

Visualization: Seaborn + Matplotlib

Output Format: High-resolution PNGs suitable for reports and presentations

About:

This project demonstrates how data visualization can reveal important insights from HR datasets, helping companies detect anomalies and make better workforce decisions.


