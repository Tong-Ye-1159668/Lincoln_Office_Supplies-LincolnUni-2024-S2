# Lincoln Office Supplies Order System

#### Submitted on 09 August 2024

This repository contains a Python application developed as part of the COMP 642: Advanced Programming course during Semester 2 of my Master of Applied Computing studies at Lincoln University. The project showcases Object-Oriented Programming (OOP) concepts and implements a comprehensive system for managing customers, orders, and payments for Lincoln Office Supplies.

## Interface
Order Placement Window

![image](https://github.com/user-attachments/assets/e18ef9eb-76db-4ba4-a45d-899e64c02323)

List All Orders Window

![image](https://github.com/user-attachments/assets/59c81620-c110-49ed-a5fd-4abb38a7e02c)

## Features
- **Customer Management**:
  - Display customer information.
  - Maintain a list of all customers.
- **Order Management**:
  - Create and process orders for existing customers.
  - Add products and quantities as order items.
  - View all orders for a specific customer or the entire company.
- **Payment Management**:
  - Record and update payments for customers.
  - View all payments made by a specific customer or the entire company.
- **User Interface**:
  - Built using Tkinter for a graphical and interactive user experience.
  - Provides useful feedback and prevents input errors.

## Technical Details
- **Programming Approach**:
  - Model-View-Controller (MVC) design pattern.
  - Automatic ID assignment for customers and orders.
  - Current date tracking for orders and payments.
- **Technologies Used**: Python (OOP with Tkinter).
- **Custom Logo**: Designed a unique logo to enhance the branding of the application.

## Purpose
This project emphasizes my ability to:
- Apply advanced Object-Oriented Programming principles.
- Build intuitive user interfaces using Tkinter.
- Design and implement maintainable and scalable software systems.

The inclusion of a custom-designed logo adds a professional touch, reflecting my attention to detail and creativity in software development.

---------------------

## Set Up the Environment

Prerequisites:
- Python 3.x
- pip (Python package installer)

Installation Steps:
1. Clone the repository:
   git clone https://github.com/Tong-Ye-1159668/Lincoln_Office_Supplies-LincolnUni-2024-S2.git
   cd Lincoln_Office_Supplies-LincolnUni-2024-S2

2. Create and activate a virtual environment:
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python -m venv .venv
   source .venv/bin/activate

3. requirements.
Core dependencies
Note: tkinter and datetime are part of Python standard library
No additional packages are required for basic functionality

File Permissions:
- Ensure read permissions for customer.txt and product.txt
- Write access needed for payment processing
- Read permissions required for image files

## Running the Application:
1. Activate virtual environment
2. Run: python driver.py
