import sys
import os


# Student name: NOOR HAYATHI JAMAL MOHAMMED 
# Student ID: S3955306
# Level: HD


class Course:
    def __init__(self, course_id, course_type, course_name, credit_points, offered_semesters):
        self.course_id = course_id
        self.course_type = course_type
        self.course_name = course_name
        self.credit_points = credit_points
        self.offered_semesters = offered_semesters

    def get_course_id(self):
        return self.course_id

    def get_course_type(self):
        return self.course_type

    def get_course_name(self):
        return self.course_name

    def get_credit_points(self):
        return self.credit_points

    def get_offered_semesters(self):
        return self.offered_semesters

    def get_offered_semesters(self):
        return self.offered_semesters

    def compute(self):
        """
    Computes the average score, number of finished courses, and number of ongoing courses for a specific course.

    Reads the result file and processes the lines to calculate the average score for the specified course.
    Keeps track of the number of finished and ongoing courses associated with the course ID.
    Returns a list containing the average score, number of finished courses, and number of ongoing courses.

    """
        with open(result_file, 'r') as file:
            lines = file.readlines()
            compute_result = []
            average = 0.0
            counter = 0.0
            nfinish = 0
            nongoing = 0
            for line in lines:
                student_id, course_id, score = line.strip().split(',')
                course_id = course_id[1:]
                score = score[1:]

                if course_id == self.course_id:
                    if score:
                        average += float(score)
                        counter += 1
                        nfinish += 1
                    else:
                        nongoing += 1

            if counter != 0.0:
                average = float(average / counter)
            compute_result.append(average)
            compute_result.append(nfinish)
            compute_result.append(nongoing)
        return compute_result


class Student:
    def __init__(self, student_id, name, student_type, mode):
        self.student_id = student_id
        self.name = name
        self.type = student_type
        self.mode = mode

    def compute(self):
    
        """
    Computes the GPA(100), GPA(4), number of finished courses, and number of ongoing courses for a specific student.

    Reads the result file and processes the lines to calculate the GPA(100) for the specified student.
    Keeps track of the number of finished and ongoing courses associated with the student ID.
    Converts the GPA(100) to GPA(4) based on the predefined scale.
    Returns a list containing the GPA(100), GPA(4), number of finished courses, and number of ongoing courses.

    """
        gpa100 = 0.0
        nongoing = 0
        nfinish = 0
        compute_result = []
        with open(result_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                student_id, course_id, score = line.strip().split(',')
                course_id = course_id[1:]
                score = score[1:]

                if student_id == self.student_id:
                    if score:
                        gpa100 += float(score)
                        nfinish += 1
                    else:
                        nongoing += 1
            gpa100= gpa100/(nfinish+nongoing) 
            if gpa100 >= 79.5:
                gpa4 = 4
            elif gpa100 >= 69.5:
                gpa4 = 3
            elif gpa100 >= 59.5:
                gpa4 = 2
            elif gpa100 >= 49.5:
                gpa4 = 1
            else:
                gpa4 = 0
            compute_result.append(gpa100)
            compute_result.append(gpa4)
            compute_result.append(nfinish)
            compute_result.append(nongoing)
        return compute_result


class Results:
    def __init__(self):
        self.courses = []
        self.students = []
        self.results = {}

    def read_courses(self, course_file_name):
        """
    Reads and processes the course information from a file.

    Opens the specified course file and reads its lines.
    Extracts the course details from each line and creates a Course object.
    Validates the course ID to ensure it starts with one of the specified prefixes.
    Adds the Course object to the list of courses in the Results instance.

    """
        with open(course_file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                course_info = line.strip().split(', ')
                course_id = course_info[0]
                prefixes = ["COSC", "ISYS", "MATH"]
                if course_id.startswith(tuple(prefixes)) == False:
                    print("Wrong course ID")
                    sys.exit(1)
                course_type = course_info[1]
                course_name = course_info[2]
                credit_points = int(course_info[3])
                offered_semesters = course_info[4:] if len(
                    course_info) > 4 else ['All']

                course = Course(course_id, course_type,
                                course_name, credit_points, offered_semesters)
                self.courses.append(course)

    def read_students(self, student_file_name):
        """
    Reads and processes the student information from a file.

    Opens the specified student file and reads its lines.
    Extracts the student details from each line and creates a Student object.
    Validates the student ID to ensure it starts with "S".
    Sets the mode to "FT" if not specified.
    Adds the Student object to the list of students in the Results instance.

    """
        with open(student_file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                student_info = line.strip().split(', ')
                student_id = student_info[0]
                if student_id[0] != "S":
                    print("Student ID doesn't start with S")
                    sys.exit(1)
                name = student_info[1]
                type = student_info[2]
                if len(student_info) == 4:
                    mode = student_info[3]
                    mode = mode
                else:
                    mode = "FT"
                student = Student(student_id, name, type, mode)
                self.students.append(student)

    def read_results(self, result_file_name):
        """
    Reads and processes the result information from a file.

    Opens the specified result file and reads its lines.
    Extracts the student ID, course ID, and score from each line.
    Validates the score to ensure it is a valid floating-point number.
    Stores the result in the Results instance with a key of (student ID, course ID).

    """
        with open(result_file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                student_id, course_id, score = line.strip().split(',')
                try:
                    if score:
                        float(score)
                except ValueError:
                    print("score invalid")
                    sys.exit(1)
                key = (student_id, course_id[1:])
                self.results[key] = score[1:]

    def display_results(self):
        total_scores = 0
        pass_scores = 0

        # Print header row
        header = "Student ID\t"
        for course in self.courses:
            header += "{:^8}\t".format(course.course_id)

        print("RESULTS")
        print("-" * (len(header) + 1))
        print(header)
        print("-" * (len(header) + 1))

        for student in self.students:
            row = "{:^8}\t".format(student.student_id)

            for course in self.courses:
                key = (student.student_id, course.course_id)
                if key in self.results:
                    score = self.results[key]
                    if score == "":
                        # Enrolled but no score yet
                        row += "{:^8}\t".format("--")

                    else:
                        row += "{:^8}\t".format(score)
                        total_scores += 1
                        if float(score) >= 49.5:
                            pass_scores += 1
                else:
                    row += "{:^8}\t".format("")  # Not enrolled

            print(row)

        print("-" * (len(header) + 1))
        print()

        pass_rate = (pass_scores / total_scores) * \
            100 if total_scores > 0 else 0
        print(f"Number of Students: {len(self.students)}")
        print(f"Number of Courses: {len(self.courses)}")
        print(f"Pass Rate: {pass_rate:.2f}%")

    def save_reports_courses(self, report_file_name):
        """
            Save course reports to a file.

            This function generates tables containing course information and writes them to the specified report file.
            It computes statistics for each course, such as the average score, number of students who finished the course,
            and number of students who are currently taking the course. It also identifies the most difficult core course
            and the most difficult elective course based on the average scores.

            Parameters:
                report_file_name (str): The name of the file to save the course reports.

    """
        with open(report_file_name, 'w') as file:
            # Generate core courses table
            core_courses_table = "COURSE INFORMATION\n"
            core_courses_table += "{:<10}{:<20}{:<8}{:<12}{:<8}{:<8}{:<8}{:<8}\n".format(
                "Course ID", "Course Name", "Type", "Credit", "Semester", "Average", "Nfinish", "Nongoing"
            )
            core_courses_table += "-" * 80 + "\n"

            # Generate elective courses table
            elective_courses_table = "Elective Courses\n\n"
            elective_courses_table += "{:<10}{:<20}{:<8}{:<12}{:<8}{:<8}{:<8}{:<8}\n".format(
                "Course ID", "Course Name", "Type", "Credit", "Semester", "Average", "Nfinish", "Nongoing"
            )
            elective_courses_table += "-" * 80 + "\n"

            diff_c_score = 100
            diff_c_name = ""
            diff_e_score = 100
            diff_e_name = ""

            for course in self.courses:
                compute_result = course.compute()
                avg_score = compute_result[0]
                num_finish = compute_result[1]
                num_ongoing = compute_result[2]

                course_info = "{:<10}{:<20}{:<8}{:<12}{:<8}{:<8.2f}{:<8}{:<8}\n".format(
                    course.course_id,
                    course.course_name,
                    course.course_type,
                    course.credit_points,
                    ", ".join(course.get_offered_semesters()),
                    avg_score,
                    num_finish,
                    num_ongoing
                )

                if course.get_course_type() == "C":
                    core_courses_table += course_info
                    if avg_score < diff_c_score:
                        diff_c_name = course.get_course_id()
                        diff_c_score = avg_score
                else:
                    elective_courses_table += course_info
                    if avg_score < diff_e_score:
                        diff_e_name = course.get_course_id()
                        diff_e_score = avg_score

            file.write(core_courses_table + "\n")
            file.write(elective_courses_table + "\n")

            file.write("COURSE SUMMARY\n")
            file.write(f"The most difficult core course is "+diff_c_name +
                       " with an average score of " + str(diff_c_score) + "\n")
            file.write(f"The most difficult elective course is " +
                       diff_e_name+" with an average score of " + str(diff_e_score))

            print(core_courses_table)
            print(elective_courses_table)
            print("COURSE SUMMARY\n")
            print(f"The most difficult core course is "+diff_c_name +
                  " with an average score of " + str(diff_c_score))
            print(f"The most difficult elective course is "+diff_e_name +
                  " with an average score of " + str(diff_e_score))

    def save_reports_students(self, report_file_name):
        """
    Save student reports to a file.

    This function generates tables containing student information and writes them to the specified report file.
    It computes statistics for each student, such as their GPAs, number of finished courses, and number of ongoing courses.
    The function identifies the best Postgraduate (PG) student and the best Undergraduate (UG) student based on their GPAs.

    Parameters:
        report_file_name (str): The name of the file to save the student reports.

    """
        with open(report_file_name, 'a') as file:
            pg_student_table = "STUDENT INFORMATION\n"
            pg_student_table += "{:<10}{:<20}{:<8}{:<12}{:<8}{:<8}{:<8}{:<8}\n".format(
                "Student ID", "Name", "Type", "Mode", "GPA(100)", "GPA(4)", "Nfinish", "Nongoing"
            )
            pg_student_table += "-" * 80 + "\n"

            ug_student_table = "{:<10}{:<20}{:<8}{:<12}{:<8}{:<8}{:<8}{:<8}\n".format(
                "Student ID", "Name", "Type", "Mode", "GPA(100)", "GPA(4)", "Nfinish", "Nongoing"
            )
            ug_student_table += "-" * 80 + "\n"

            best_pg_name = ""
            best_pg_gpa = 0
            best_ug_name = ""
            best_ug_gpa = 0

            for student in self.students:
                compute_result = student.compute()
                name = student.name
                if student.mode == "FT":
                    
                    if int(compute_result[2])+int(compute_result[3])<4:
                        name += "(!)"
                else:
                    if int(compute_result[2])+int(compute_result[3])<2:
                        name += "(!)"


                student_info = "{:<10}{:<20}{:<8}{:<12}{:<8.2f}{:<8.2f}{:<8}{:<8}\n".format(
                    student.student_id,
                    name,
                    student.type,
                    student.mode,
                    compute_result[0],
                    compute_result[1],
                    compute_result[2],
                    compute_result[3]
                )
                if student.type == "PG":
                    if compute_result[1]> best_pg_gpa:
                        best_pg_gpa= compute_result[1]
                        best_pg_name= student.student_id
                    pg_student_table += student_info  
                else:
                    if compute_result[1]> best_ug_gpa:
                        best_ug_gpa= compute_result[1]
                        best_ug_name= student.student_id
                    ug_student_table += student_info 

            file.write("\n\n" + pg_student_table+ "\n")
            file.write(ug_student_table+ "\n")
            file.write("STUDENT SUMMARY" + "\n")
            file.write("The best PG student is "+ best_pg_name+" with a GPA score of "+str(best_pg_gpa)+ "\n")
            file.write("The best UG student is "+ best_ug_name+" with a GPA score of "+str(best_ug_gpa))
            
            print(pg_student_table)
            print(ug_student_table)
            print("STUDENT SUMMARY")
            print("The best PG student is "+ best_pg_name+" with a GPA score of "+str(best_pg_gpa))
            print("The best UG student is "+ best_ug_name+" with a GPA score of "+str(best_ug_gpa))


result_file = ""

if __name__ == '__main__':
    """
    Entry point of the program.

    This code block checks the command-line arguments, reads input files, performs necessary checks, and saves reports.
    It ensures that the correct number of command-line arguments are provided.
    The result file is checked for emptiness, and if empty, an error message is displayed.
    The program handles the FileNotFoundError exception if any of the input files cannot be found.

    """
    if len(sys.argv) != 4:
        print("Usage: python my_school.py <result file> <course file> <student file>")
        sys.exit(1)

    result_file = sys.argv[1]
    course_file = sys.argv[2]
    student_file = sys.argv[3]

    try:
        results = Results()
        results.read_courses(course_file)
        results.read_students(student_file)
        results.read_results(result_file)
        # Results file check
        if os.path.getsize(result_file) == 0:
            print("Error: The result file is empty.")
            sys.exit(1)
        results.display_results()
        results.save_reports_courses("reports.txt")
        results.save_reports_students("reports.txt")
    except FileNotFoundError as e:
        filename = e.filename
        print(f"File not found: {filename}")
        sys.exit(1)
