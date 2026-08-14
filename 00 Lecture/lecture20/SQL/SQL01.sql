-- show database list  # kud-yuyo-ijj
show databases;
-- create a database
create database cwpc;
-- drop database
-- drop database cwpc;
-- select database
use cwpc;
-- show tables list into db
show tables;

create table employee(
	Employee_id int auto_increment primary key,
    name varchar(50),
    date_of_birth date,
    gender enum("male","female"),
    email varchar(100) unique key,
    phone varchar(100) unique key,
    salary  decimal(10,2),
    age int    
);
-- show table records 
select * from employee;
-- insert into table 

insert into employee (Employee_id,name,date_of_birth,gender,email,phone,salary,age)
values(101,"Nisha","1990-12-05","female","nisha@cwpc.in","987654312",45000,88);

insert into employee (name,date_of_birth,gender,email,phone,salary,age)
values("Nishant","1990-12-05","male","nishant@cwpc.in","9876543102",45000,88),
("Joy","1996-12-05","male","joy@cwpc.in","9876543106",48000,76),
("Bhavin","1997-12-05","male","bhavin@cwpc.in","9876593106",49000,48),
("Toy","1990-10-05","female","toy@cwpc.in","9876543505",45060,78),
("Shubham","1960-12-05","male","subh@cwpc.in","9876545102",42000,68);

-- empty table 
truncate table employee;

-- switch database 
use classicmodels;
show tables;
select * from customers;
-- total record 
select count(*) from customers;
-- and / or / where
select customername , city , country , state , creditlimit from customers
where country = "USA";

select customername , city , country , state , creditlimit from customers
where country = "USA" and creditLimit > 100000;

select customername , creditlimit , creditlimit + 50000 as update_creditlimit
from customers where country = "USA" and creditlimit < 100000;

select customername , sum(creditlimit) , creditlimit + 50000 as update_creditlimit
from customers where country = "USA" and creditlimit < 100000;

-- group by

select country , count(country) as total_country from customers group by country
having count(country) > 5; 





-- select distinct country from customers; 


-- join 

create database cwpc01;
use cwpc01;

create table customers(
	customerID int primary key,
    name varchar(100),
    email varchar(100),
    city varchar(100)
);
create table orders(
	orderID int primary key,
    customerID int,
    orderDate date,
    totalamount decimal(10,2)
);
insert into orders values(101,1,"2026-05-10",2500.56),
(102,2,"2026-05-10",2500.56),
(103,3,"2026-10-11",3500.56),
(104,4,"2026-12-12",6500.56),
(105,5,"2026-04-13",8500.56),
(106,12,"2026-07-15",9500.56),
(107,11,"2026-06-17",7500.56);

insert into customers values(1,"joy","joy@gmail.com","mumbai"),
(2,"Mohit","mohit@gmail.com","mumbai"),
(3,"neha","neha@gmail.com","pune"),
(5,"umika","umika@gmail.com","pune"),
(8,"sweta","sweta@gmail.com","surat"),
(9,"bhumika","bhumika@gmail.com","bhuj"),
(10,"bhavin","bhavin@gmail.com","jaipur");

select * from orders;
select * from customers;
-- inner join
select customers.name , customers.city , orders.orderdate , orders.totalamount
from customers inner join orders on customers.customerid = orders.customerid;
-- other way
select c.name , c.city , o.orderdate , o.totalamount
from customers as c inner join orders as o on c.customerid = o.customerid;

-- left join 
select customers.name , customers.city , orders.orderdate , orders.totalamount
from customers left join orders on customers.customerid = orders.customerid;

-- right join 
select customers.name , customers.city , orders.orderdate , orders.totalamount
from customers right join orders on customers.customerid = orders.customerid;

-- full join 

select customers.name , customers.city , orders.orderdate , orders.totalamount
from customers left join orders on customers.customerid = orders.customerid
union
select customers.name , customers.city , orders.orderdate , orders.totalamount
from customers right join orders on customers.customerid = orders.customerid;

-- create views 
create view  customer_data as 
select customers.name , customers.city , orders.orderdate , orders.totalamount
from customers left join orders on customers.customerid = orders.customerid
union
select customers.name , customers.city , orders.orderdate , orders.totalamount
from customers right join orders on customers.customerid = orders.customerid;  

-- call the view 

select * from customer_data;


-- 14 Aug 2026
use cwpc_db;

select count(*) from employees;
select * from employees;

select department , count(department) from employees group by department;

select department , avg(salary) from employees group by department;

-- windows function 
select emp_name , department , salary, 
avg(salary) over( partition by department) as agv_sal_dept
from employees;

select emp_name , count(emp_name) from employees group by emp_name;


# row_number()

select emp_name,department , salary , 
row_number() over( order by salary desc) as row_num
from employees;

# rank()
select emp_name , salary , 
rank() over( order by salary desc) as salary_rank
from employees;

# dense_rank()

select emp_name , salary , 
dense_rank() over( order by salary desc) as salary_rank
from employees;


-- ranking within each department

select emp_name, department , salary , 
rank() over( partition by department order by salary desc) as dept_rank from employees;

-- find the highest-paid employee in each department
with rank_employee as (
select emp_name, department , salary , 
rank() over( partition by department order by salary desc) as dept_rank from employees
)
select * from rank_employee where dept_rank = 1;

-- total salary every department
-- sum()
-- avg()
-- count()
-- min()
-- max()
select emp_name, department , salary , 
sum(salary) over( partition by department) as dept_salary_total from employees;

-- department salary percentage
select emp_name, department , salary , 
sum(salary) over( partition by department) as dept_salary_total, 
round(
salary * 100.0 / sum(salary) over( partition by department),2) as salary_per
from employees;

-- lag()
select hire_date, salary , 
lag(salary) over(order by hire_date) as salary_01
from employees;

select * from employees;

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE,
    salesperson VARCHAR(50),
    amount INT
);

INSERT INTO sales
(sale_id, sale_date, salesperson, amount)
VALUES
(1, '2026-01-01', 'Rahul', 1000),
(2, '2026-01-03', 'Amit', 1500),
(3, '2026-01-05', 'Priya', 2000),
(4, '2026-01-07', 'Rahul', 1200),
(5, '2026-01-10', 'Amit', 1800);

SELECT
    sale_date,
    amount,
    SUM(amount) OVER (
        ORDER BY sale_date
    ) AS running_total
FROM sales;

SELECT
    sale_date,
    amount,
    LAG(amount) OVER (
        ORDER BY sale_date
    ) AS previous_amount,

    amount - LAG(amount) OVER (
        ORDER BY sale_date
    ) AS difference

FROM sales;


 
