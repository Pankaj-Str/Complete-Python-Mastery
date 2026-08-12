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


