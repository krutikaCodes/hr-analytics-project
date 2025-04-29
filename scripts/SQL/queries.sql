use hr_analytics;
#overall attrition rate
select ROUND(100*SUM( CASE WHEN Attrition ='Yes' THEN 1 ELSE 0 END )/COUNT(*),2) AS attrition_rate_percent
FROM employees;
#average monthly income by department
SELECT Department, ROUND(avg(MonthlyIncome),2) AS average_monthlyincome 
FROM EMPLOYEES
GROUP BY Department;
#job satisfaction by job role
select JobRole, ROUND(avg(JobSatisfaction),2) as avg_jobsatisfaction
from employees
group by JobRole
order by avg_jobsatisfaction desc;
#years at company by department
select Department,Round(avg(YearsAtCompany),2) as avg_years
from employees
group by department
order by avg_years desc;