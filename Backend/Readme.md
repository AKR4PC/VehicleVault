# Backend Documentation

This folder contains all Python scripts that handle the core functionality of the Automobile Management System.

## Files Overview

### main.py
- Entry point of the application
- Handles main menu and navigation between different modules
- Provides interface to access different tables (BMW, Mercedes, Customers, Employees)

### bmw.py & mercedes.py
- Manage vehicle inventory for respective brands
- Handle CRUD operations for vehicle records
- Features:
  - Add new vehicle entries
  - Display all vehicles
  - Search specific vehicles
  - Update vehicle information
  - Delete vehicle records

### customers.py
- Manages customer database
- Tracks customer information and purchases
- Features:
  - Register new customers
  - View customer details
  - Update customer information
  - Remove customer records
  - Search customer by ID

### employees.py
- Handles employee records and performance tracking
- Manages sales data and employee grades
- Features:
  - Add new employee records
  - View employee details
  - Update employee information
  - Track sales performance
  - Manage employee grades

## Common Functions

Each module contains these standard functions:
- `clrscreen()`: Clears console screen
- `display()`: Shows all records
- `insertdata()`: Adds new records
- `deletedata()`: Removes records
- `search()`: Finds specific records
- `update()`: Modifies existing records
- `menubook()`: Displays operation menu

## Error Handling

All database operations include error handling for:
- Access denied errors
- Database not found
- General MySQL errors
- Invalid input validation

## Database Connection

Each module uses the following connection parameters:
```python
connection.MySQLConnection(
    user='root',
    passwd='your_password',
    host='localhost',
    database='automobile_management'
)
```

Remember to update these credentials according to your MySQL setup.
