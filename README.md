# Python-Project
Title: Final Coding Challenge - School Management System
Overview

For the final coding challenge of the COSC2531 - Programming Fundamentals course, I developed a Python-based school management system using object-oriented programming (OOP) principles. The system is designed to manage student, course, and result data for a school, providing functionality to read and process data from files and display meaningful reports.
Problem Overview

The goal of this assignment was to implement a Python program with at least three classes: Results, Course, and Student. The program should be capable of reading data from text files (student, course, and result files), processing this data, and displaying a formatted table with the results. The program needed to support various levels of complexity, starting from basic functionality to more advanced features such as handling course types, student types, and error handling.
What Was Done

    PASS Level:

        Developed the Results, Course, and Student classes using the object-oriented paradigm.

        Implemented functionality to read student, course, and result data from separate text files.

        Created methods to display student scores in a well-formatted table, calculate pass rates, and display relevant information about students and courses.

        Handled file input and error scenarios, such as missing or incorrect file arguments.

    CREDIT Level:

        Enhanced the Course class to include more detailed information, such as course names, credit points, and offered semesters.

        Implemented methods to compute statistics about courses, such as the number of students who finished or are ongoing in the course, and the average score.

        Extended the result file format to support the new course details and displayed additional course information.

    DI Level:

        Introduced two types of students: Undergraduate and Postgraduate students.

        Added functionality to track and display student enrollment status and GPA (both on a scale of 100 and 4) based on their results.

        Implemented methods to ensure students meet the minimum enrollment requirements, displaying warnings when requirements are not met.

    HD Level:

        Implemented exception handling for scenarios such as missing files, empty result files, invalid scores, and incorrect student/course IDs.

        Enhanced the program to calculate and display weighted GPAs (WGPA) for students, considering course credit points.

        Added features to sort and accumulate reports in a text file, including timestamps for each report.

Technologies Used

    Python: The main programming language used to implement the school management system.

    Object-Oriented Programming (OOP): All program functionality was encapsulated within classes and methods.

    File Handling: Used Python's built-in file handling capabilities to read data from and write reports to text files.

Key Features

    Student Information: Displays details about students, including their enrollment status, GPA, and whether they meet enrollment requirements.

    Course Information: Shows course details, such as course type (Core/Elective), offered semesters, and statistics about student performance.

    Results Display: Generates a table showing students' results for each course, calculating the pass rate and providing insights about student performance.

Challenges

    Designing the classes and methods to handle multiple levels of functionality.

    Implementing error handling and validation of the data files to ensure robust behavior.

    Handling the complexity of weighted GPA calculations and ensuring all requirements were met for each level of the assignment.

Conclusion

This project demonstrates a comprehensive application of object-oriented programming principles, file handling, and error management to build a school management system that handles real-world data. The solution evolves through multiple levels, from basic functionality to advanced features such as weighted GPA calculations and reporting.
