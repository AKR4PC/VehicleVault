# Automobile Management System

A comprehensive management system for car dealerships built with Python and MySQL, featuring inventory management for BMW and Mercedes vehicles, customer records, and employee data management.

## Project Overview

This system allows car dealerships to:
- Manage BMW and Mercedes vehicle inventory
- Track customer information and purchases
- Manage employee records and sales performance
- Perform CRUD operations (Create, Read, Update, Delete) on all records

## Tech Stack

- Python 3.x
- MySQL
- mysql-connector-python

## Project Structure

```
automobile-management/
│
├── backend/
│   ├── main.py
│   ├── bmw.py
│   ├── mercedes.py
│   ├── customers.py
│   ├── employees.py
│   └── README.md
│
├── database/
│   ├── schema.sql
│   └── README.md
│
└── README.md
```

## Features

- **Multi-table Database Management**: Handles four main tables (BMW, Mercedes, Customers, Employees)
- **Complete CRUD Operations**: For all tables with error handling
- **User-friendly Interface**: Menu-driven interface for easy navigation
- **Data Validation**: Input validation and error handling
- **Modular Design**: Separate modules for different functionalities

## Setup Instructions

1. Install Python 3.x and MySQL
2. Install required Python packages:
   ```bash
   pip install mysql-connector-python
   ```
3. Create MySQL database and tables using scripts in database/schema.sql
4. Update database connection parameters in Python files:
   ```python
   user='your_username'
   passwd='your_password'
   host='localhost'
   database='automobile_management'
   ```

## Usage

1. Run the main program:
   ```bash
   python main.py
   ```
2. Select the table you want to work with:
   - BMW Inventory
   - Mercedes Inventory
   - Customer Records
   - Employee Management

3. Choose operations from the menu:
   - Add Record
   - Display Records
   - Search Record
   - Delete Record
   - Update Record

## Database Schema

The system consists of four main tables:

1. **BMW**
   - Vehicle details including model, body type, fuel type, price, acceleration, top speed

2. **Mercedes**
   - Vehicle details including model, body type, fuel type, class, price, output, acceleration, top speed

3. **Customers**
   - Customer information including name, address, purchased car, contact details

4. **Employees**
   - Employee records including name, post, salary, years of service, sales performance

## Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
