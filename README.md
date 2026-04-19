# Academic Institution DB — Assignment 4A

Group members:
CS23B019
CS23B034
CS23B098
CS23B083
CS22B010

A terminal-based Python application to manage course and enrollment data for Even Semester 2006 in the `academic_insti` MySQL database.

## Prerequisites
- Python 3
- MySQL with the `academic_insti` database loaded
- mysql-connector-python: `pip install mysql-connector-python`

## Running
```bash
python main.py -u root               # prompts for password
python main.py -u root -p mypassword # password inline
python main.py --host 192.168.1.5 -u root -p mypassword  # custom host
```


### Requirements

- Python 3.6+
- mysql-connector-python
- MySQL Server with `academic_insti` database as its name 


```

### Usage

Run the application:


python main.py -u yourusername -p yourpassword

```


```

## Features
1. **Add Course** — Assigns a teacher and classroom to a course for Even 2006, with validations on department, course, and professor.
2. **Enroll Student** — Enrolls a student into one or more courses for Even 2006, verifying prerequisites are passed.
