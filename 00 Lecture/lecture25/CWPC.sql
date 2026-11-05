-- Step 1 Create DataBase
create database cwpc111;
-- Step 2 select database
use cwpc111;
-- Step 3 create a new table 
create table customers(
	customerID int primary key,
    name varchar(100),
    mobile varchar(100),
    age int,
    creditlimit bigint,
    dob date,
	bank enum("HDFC","SBI","ICICI")
);
-- show tables records
select * from customers;
-- insert record into table 
insert into customers 
(customerid,name,mobile,age,creditlimit,dob,bank)
values(1,"nishant","7894562100",14,45000,"2015-04-23","ICICI"),
(2,"Riya","7894562100",14,45000,"2015-04-23","ICICI"),
(3,"Neha","7894562100",14,45000,"2015-04-23","HDFC"),
(4,"Rohan","7894562100",14,45000,"2015-04-23","ICICI");

insert into customers(customerid,name,mobile,age,dob,bank)
values(10,"nishant","7894562100",14,"2015-04-23","ICICI"); 

-- empty table 
truncate table customers;
select * from customers;
-- delete table
drop table customers;
-- check table 
show tables;

-- find the list of databases 
show databases;
-- create a new database
create database cwpc90;
-- delete database
drop database cwpc90;
-- select database
 
-- create a table 
create table Employee(
	emp_id int,
    name varchar(100),
    city varchar(100),
    dob date,
    salary int,
    age int,
    dept enum("hr","sales","it") 
);

-- show list of tables
show tables;

-- show table record
select * from employee;

-- insert record into table 

insert into employee (emp_id,name,city,dob,salary,age,dept)
value(101,"nishant","mumbai","1990-11-23",45000,32,"sales");



-- date 5 oct 2026


use classicmodels;

show tables;

-- check customers table records 
select * from customers;
select customernumber,customername,country,city,creditlimit 
from customers;
-- update
select * from customers where customernumber = 125;

update customers set creditlimit = 10000
where customernumber = 125; 
-- delete
delete from customers where customernumber = 125; 
-- where
-- and 
select * from customers where country = "USA" and creditlimit > 50000;
-- or
select * from customers where creditlimit > 100000 and creditlimit < 200000;
-- count()
select count(*) from customers 
where creditlimit > 100000 and creditlimit < 200000;

select customername , country , creditlimit from customers 
where country = "USA" and creditlimit < 100000;




-- 8 Oct 2026
create database CWPC_Company;
use CWPC_Company;

create table employees(
	employee_id int primary key,
    name varchar(50),
    department varchar(50),
    salary decimal(10,2),
    city varchar(50),
    joining_date Date,
    manager_id int
);

select * from employees;


-- limit
select * from employees limit 3;

-- order by
select * from employees order by salary desc limit 5;
select * from employees order by salary asc limit 5;

-- offset 2 (First 2 row skip)
select * from employees limit 6 offset 9;
select * from employees where employee_id > 9 and employee_id < 16;

-- is NULL 
select * from employees where manager_id is NULL;

-- is not NULL
select * from employees where manager_id is not NULL;

-- total record not null

select count(*) from employees where manager_id is not NULL;

-- coalesce()
select name , coalesce(manager_id,0) as manager_id from employees;

select count(*) from employees where Department = "IT";

-- distinct
select distinct Department from employees;
-- count() - Department
select count(distinct Department) from employees;

-- group by
select Department , count(Department) as total_employee
from employees group by Department;

select name , salary , salary * 1.10 as new_salary 
from employees where Department = "IT";


-- Date 9 Oct 2026


create database CWPC0909;
use CWPC0909;
create table customers(
	customer_id int primary key,
    name varchar(100),
    city varchar(100),
    email varchar(100)
);
insert into customers(customer_id,name,city,email) 
values(101,"Joy","Mumbai","joy@cwpc.in"),
(102,"Nishant","Mumbai","nishant@cwpc.in"),
(103,"Neha","Surat","neha@cwpc.in"),
(104,"Rohan","Surat","rohan@cwpc.in"),
(105,"Riya","Delhi","riya@cwpc.in"),
(109,"Tiya","bhuj","tiya@cwpc.in"),
(110,"Kiya","pune","kiya@cwpc.in");
select * from customers;

create table orders(
	order_id int primary key,
    customer_id int,
    orderdate date,
    total_amount decimal(10,2)
);
insert into orders(order_id,customer_id,orderdate,total_amount) 
values(10,100,"2026-05-23",5600.23),
(11,101,"2026-05-23",5600.03),
(12,102,"2026-10-22",5900.73),
(13,103,"2026-07-13",5800.13),
(14,104,"2026-06-03",5500.33),
(15,105,"2026-07-33",4600.83),
(16,106,"2026-08-23",2600.73),
(17,107,"2026-09-13",5500.63),
(18,108,"2026-04-02",4500.63);

select * from orders;
select * from customers;

-- left join 


 select customers.customer_id ,customers.name , customers.city , 
 orders.total_amount , orders.order_id 
 from customers left join orders on 
 customers.customer_id = orders.customer_id;
 
 -- right join
 
select customers.customer_id ,customers.name , customers.city , 
orders.total_amount , orders.order_id 
from customers right join orders on 
customers.customer_id = orders.customer_id;
 


-- Date 12 oct 2026

-- like 
use classicmodels;
show tables;

select * from customers;

-- like 
select * from customers where customername like "t%";
select * from customers where customername like "toy%";
select * from customers where customername like "%toy%";
select * from customers where customername like "%t";

-- String upper()
select customername , upper(customername) as name from customers;
-- lower()
select customername , lower(customername) as name from customers;
-- length of string 
select customername , length(customername) as name_length from customers;
--  substring()
select customername , substring(customername,1,5) as short_name from customers;
-- concat()
select contactlastname , contactfirstname , 
concat(contactfirstname,' ',contactlastname) as full_name from customers;
-- replace()
select customername , Country , 
replace(country,"USA","Mumbai") as update_city from customers;

-- + , - , * /
select customername , country, creditlimit, 
creditlimit / 3.2 as update_limit from customers;

-- round()
select customername , country,  creditlimit, creditlimit / 3.2 as old_limit,
round(creditlimit / 3.2) as update_limit from customers;


select customername , creditlimit , round(creditlimit * 1.049 , 2) as update_cl
from customers;


select ceil(123.25) as round_up,
floor(123.75) as round_down;

use CWPC_company;
select * from employees;
-- current_date()
select current_date() as today;
-- current_datetime now()
select now() as current_datetime;
select timestamp() as current_datetime;

-- Date 13 Oct 2026
use CWPC_company;
select * from employees;

select name,joining_date,
year(joining_date) as year,
month(joining_date) as month,
day(joining_date) as day
from employees;

-- add days to a date 
select name, joining_date , date_add(joining_date,interval 10 Day) as after_10
from employees;
-- add month 
select name, joining_date , date_add(joining_date,interval 10 month) as after_10
from employees;

select name, joining_date , date_sub(joining_date,interval 2 month) as after_10
from employees;

select name, joining_date , date_sub(joining_date,interval 2 year) as after_10
from employees;

select name, joining_date ,round(datediff(current_date(),joining_date)/365,1) as diff_day 
from employees;

-- views

create view exp_emp as 
select name, joining_date ,round(datediff(current_date(),joining_date)/365,1) as diff_day 
from employees;

-- call views 
select * from exp_emp; 

-- windows function 
-- rank()
select * from employees;
select name ,salary, department from employees order by salary desc;

 







