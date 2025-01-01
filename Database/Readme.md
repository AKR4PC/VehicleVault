# Database Documentation

This folder contains the MySQL database schema and setup instructions for the Automobile Management System.

## Schema Overview

The database consists of four main tables:

### 1. BMW Table
```sql
CREATE TABLE BMW (
    SRno int primary key,
    Model varchar(30),
    Bodytype varchar(20),
    Fueltype varchar(10),
    Price bigint(10),
    Acceleration float(2,1),
    topspeed int(3)
);
```

### 2. Mercedes Table
```sql
CREATE TABLE mercedes (
    SRno int primary key,
    model varchar(30),
    body_type varchar(20),
    fuel_type varchar(15),
    class varchar(15),
    price bigint(10),
    output varchar(100),
    acceleration float(5,2),
    top_speed int(3)
);
```

### 3. Customers Table
```sql
CREATE TABLE customers (
    SRno int primary key,
    name varchar(20),
    address varchar(20),
    car varchar(30),
    phone_number varchar(15),
    age smallint(2),
    car_company varchar(20)
);
```

### 4. Employees Table
```sql
CREATE TABLE employees (
    empno int primary key,
    name varchar(30),
    post varchar(20),
    salary bigint(10),
    years_of_service tinyint(2),
    employe_code varchar(10),
    sales_in_month int(4),
    grade varchar(1)
);
```

## Setup Instructions

1. Create the database:
```sql
CREATE DATABASE automobile_management;
USE automobile_management;
```

2. Create all tables using the provided schema in schema.sql

3. Grant necessary permissions:
```sql
GRANT ALL PRIVILEGES ON automobile_management.* TO 'your_username'@'localhost';
FLUSH PRIVILEGES;
```

## Data Types Used

- **int**: For IDs and numeric values
- **varchar**: For text data with varying length
- **bigint**: For large numeric values (prices, salaries)
- **float**: For decimal numbers (acceleration)
- **tinyint**: For small numeric ranges
- **smallint**: For medium-range numeric values

## Constraints

- Primary keys on SRno/empno fields
- Appropriate field lengths for varchar fields
- Numeric constraints for relevant fields

## Sample Data

Sample data is provided in schema.sql for initial testing and demonstration purposes.
