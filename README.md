# Smart Campus Resource Scheduler API

A REST API for managing and optimizing campus resource allocation using a heuristic-based scheduling approach. The API is designed to help educational institutions automate the scheduling of resources such as classrooms, lecturers, laboratories, courses, and time slots while reducing scheduling conflicts and improving resource utilization.

## Project Overview

Scheduling within universities and other higher institutions can become difficult as the number of courses, students, lecturers, and facilities increases. Manual scheduling methods often lead to overlapping classes, inefficient use of resources, and unnecessary administrative work.

The Smart Campus Resource Scheduler API was developed to address these issues by providing a centralized backend service that can manage resources and generate scheduling solutions automatically.

The system uses heuristic techniques to evaluate available resources and produce practical schedules that satisfy defined constraints.

---

## Features

- User authentication and authorization
- Resource management
- Classroom management
- Lecturer management
- Course management
- Department management
- Timetable generation
- Conflict detection
- Heuristic-based scheduling
- Schedule recommendations
- RESTful API endpoints

---

## How the Scheduling Process Works

The scheduling workflow follows a heuristic approach:

1. Resources are added to the system:
   - Classrooms
   - Lecturers
   - Courses
   - Departments
   - Laboratories
   - Available time slots

2. Constraints are considered during scheduling:

   - Lecturer availability
   - Resource availability
   - Classroom capacity
   - Department requirements
   - Time restrictions

3. The heuristic algorithm evaluates possible allocations.

4. The system selects suitable scheduling options with minimal conflicts.

5. A timetable is generated and stored.

---

## Technologies Used

### Backend

- Python
- Django
- Django REST Framework

### Database

- PostgreSQL

### Tools

- Git
- GitHub
- Railway
- Postman
