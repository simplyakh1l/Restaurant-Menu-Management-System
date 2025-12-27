# Restaurant Menu Management System

A simple Python + MySQL based project to manage restaurant food items.

## Features
- Create database and table
- Add food records
- Delete food records
- Display all records
- Search and update options (extendable)

## Tech Stack
- Python 3.8
- MySQL 8.0
- mysql-connector-python

## Database Schema
| Field | Type | Constraint |
|-----|-----|-----|
| fid | INT | Primary Key |
| fname | VARCHAR | Not Null |
| price | INT | Not Null |
| rating | DECIMAL | > 0 |
| dor | DATE | — |

## How to Run
1. Install MySQL and Python
2. Install connector:
   ```bash
   pip install mysql-connector-python
