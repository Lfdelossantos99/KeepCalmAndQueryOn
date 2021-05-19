import psycopg2


class small_example:

    def __init__(self):
        self.connection = psycopg2.connect(host="localhost", port=5432, dbname="small_example", user="jkhow")

    # prints menu and returns the input, not yet validated
    def menu_print(self):  # TODO: make this formatting pretty (double-check teammates haven't yet)
        print("==================================")
        print(
            "| Please select an option:       |\n| 0  Exit                        |\n| 1  Generate Advisor List       |\n| 2  Hire New Instructor         |\n| 3  Generate Transcript         |\n| 4  Generate Course List        |\n| 5  Register Student for Course |")
        print("==================================")
        return input("Input: ")

    # takes input from menu_selection method, validates input, and calls corresponding method
    # returns
    def menu_handling(self, ins_input):
        isValid = False
        cur_input = ins_input
        while isValid == False:
            if (cur_input == '0'):
                print("Goodbye!")
                self.connection.close()
                quit()
            elif (cur_input == '1'):
                print("Generating Advisor List...")
                self.advisorList()
                isValid = True
            elif (cur_input == '2'):
                print("Hiring New Instructor....")
                self.newInstructor()
                isValid = True
            elif (cur_input == '3'):
                self.generateTranscript()
                isValid = True
            elif (cur_input == '4'):
                print("Generating Course List....")
                self.generateCourses()
                isValid = True
            elif (cur_input == '5'):
                print("Registering Student for Course....")
                self.registerStudent()
                isValid = True
            else:
                cur_input = input("Please enter valid input (number 0 to 5): ")
        return

    # Generates advisor list
    def advisorList(self):
        cur = self.connection.cursor()
        try:
            cur.execute(
                "WITH advisors AS (SELECT s_ID, i_ID AS i_ID, name AS a_name FROM advisor NATURAL JOIN (SELECT i_id, name FROM advisor JOIN instructor ON (i_id=ID)) as instructor_s) SELECT DISTINCT ID, name, a_name AS Advisor FROM Student JOIN (advisor NATURAL JOIN advisors) ON (student.ID=s_id)")
            print("S_ID|S_name|A_name")
            # Prints with formatting seen above
            for line in cur:
                print("{}|{}|{}".format(line[0], line[1], line[2]))

        except psycopg2.ProgrammingError as p:
            print("Error, please try again")
            print(p)

        # Add a new Instructor

    def newInstructor(self):
        cur = self.connection.cursor()
        cur1 = self.connection.cursor()
        cur2 = self.connection.cursor()

        ID = input("What is their Employee ID?")
        name = input("What is their name?")
        dept = input("What is their Department?  ")
        salary = input("What is their starting salary? ")
        # Check if the department exists
        try:
            cur.execute("Select dept_name from department where dept_name= %s", (dept,))
        except psycopg2.ProgrammingError as p:
            print(p)
            print("Error finding Department")
        # if it doesn't add it
        if cur.fetchone() is None:
            try:
                cur1.execute("Insert into Department (dept_name) VALUES (%s)", (dept,))
            # Errors for if name is too long or general programming error
            except psycopg2.ProgrammingError as p:
                print(p)
                print("Error adding Department")

            except psycopg2.errors.StringDataRightTruncation as p:
                print(p)
                print("New Department Name too Long")
                return 0
        # Insert instructor into instructor table
        try:
            cur2.execute("Insert into Instructor (ID, name, dept_name, salary) VALUES (%s,%s,%s,%s)",
                         (ID, name, dept, salary))
            print("Inserted")
        # Errors for if ID or name is too long, salary is too low, or ID already exists
        except psycopg2.errors.StringDataRightTruncation as p:
            print(p)
            print("ID or Name too long")

        except psycopg2.errors.CheckViolation as p:
            print(p)
            print("Salary too low")

        except psycopg2.errors.UniqueViolation as p:
            print(p)
            print("ID already exists")
        # Commits changes to DB
        self.connection.commit()

    # Generates a transcript
    def generateTranscript(self):

        def transcript_menu_selection():
            curInput = input("Enter the ID of a student " \
                             "to get transcript of that person: ")
            # keep prompting until user enters something a valid integer
            while len(curInput) == 0 or not curInput.isnumeric():
                if (curInput == 'q'):
                    print("Goodbye!")
                    quit()
                else:
                    curInput = input("Enter valid student ID: ")

            # pad with zeroes until ID will match the ID in the DB if it exists
            while (len(curInput) < 5):  # max length of ID
                curInput = '0' + curInput  # pad with one zero
            return curInput

        # converts letter grade to grade point scale
        def convert_to_gp(grade):
            if (grade == "A"):
                to_return = 4.0
            elif (grade == "A-"):
                to_return = 3.7
            elif (grade == "B+"):
                to_return = 3.3
            elif (grade == "B"):
                to_return = 3.0
            elif (grade == "B-"):
                to_return = 2.7
            elif (grade == "C+"):
                to_return = 2.3
            elif (grade == "C"):
                to_return = 2.0
            elif (grade == "C-"):
                to_return = 1.7
            elif (grade == "D+"):
                to_return = 1.3
            elif (grade == "D"):
                to_return = 1.0
            elif (grade == "D-"):
                to_return = 0.7
            return to_return

        cur = self.connection.cursor()

        cur_sem = ""
        cur_year = ""
        student_id = ""
        name = ""
        dept_name = ""
        gpsum_total = 0.0
        gpsum_sem = 0.0
        num_courses = 0
        num_courses_sem = 0

        trn = transcript_menu_selection()
        query = "SELECT * FROM student natural join takes WHERE ID = %s ORDER BY semester;"  # student name query

        try:
            cur.execute(query, (trn,))

            if (cur.rowcount == 0):
                print("Transcript unavailable: no such student or the student has taken 0 classes")
            else:
                # print("The number of courses this student takes: ", cur.rowcount) #must be 1+
                row = cur.fetchone()  # indexAt of a list? yep mylist[1] for example
                # store first semester and year
                student_id = row[0]
                print("Student ID: " + student_id)
                # store the name
                name = row[1]
                # store the dept
                dept_name = row[2]
                print(name + ", " + dept_name)
                cur_sem = row[6]
                cur_year = row[7]
                # store course_id for query call
                course_id = row[4]
                print("-----------------------")
                print(cur_sem + " " + str(cur_year) + "\n")

                while row is not None:
                    # print(row)
                    # label new semester and year indicated
                    if (cur_sem != row[6] or cur_year != row[7]):
                        # reset semester GPA info
                        gpsum_sem = 0.0
                        num_courses_sem = 0
                        cur_sem = row[6]
                        cur_year = row[7]
                        print("-----------------------")
                        print(cur_sem + " " + str(cur_year) + "\n")
                    # for each entry, while semester and year is the same as the current one stored,
                    # print the course ID, section number, course name, credits, and grade
                    else:
                        # TODO: query "SELECT credits FROM course WHERE course_id = %s", row[#]) and save as cur_cred
                        query = "SELECT credits FROM course WHERE course_id = %s"
                        cur2 = self.connection.cursor()  # need a new cursor for a new query
                        cur2.execute(query, (course_id,))
                        # expected output: one attribute, one tuple, containing the number of corresponding credits for that particular course
                        q2 = cur2.fetchone()  # table result
                        corr_creds = q2[0]
                        corr_creds = str(corr_creds)
                        print("  " + row[4] + "-" + row[5] + "  (" + corr_creds + ")  " + row[8])
                        # add credits to gpsum? to divide at end??
                        points = convert_to_gp(row[8])
                        gpsum_total += points
                        gpsum_sem += points
                        num_courses += 1
                        num_courses_sem += 1

                        row = cur.fetchone()
                    if (row is None or cur_sem != row[6] or cur_year != row[7]):
                        print("->Semester GPA " + str(gpsum_sem / num_courses_sem))

                print("\nCumulative GPA " + str(gpsum_total / num_courses))

        except psycopg2.ProgrammingError as e:
            print("Other Error")
            print(e)

    # Generates list of courses offered that term
    def generateCourses(self):
        cur = self.connection.cursor()
        values = input("Enter the semester and year separated by whitespace: semester year\n").split()
        if len(values) != 2:
            return "Invalid Input"
        query = "WITH courses AS (SELECT * FROM course NATURAL JOIN section	WHERE semester=%s AND year=%s), enrollment AS (SELECT course_id, count(course_id) as enrolled FROM (SELECT course_id FROM takes Where semester=%s and year=%s) as e group by course_id) SELECT course_id, sec_id, title, credits, building, room_number,  enrolled, capacity, time_slot_id  FROM ((courses NATURAL JOIN time_slot) as ts NATURAL JOIN classroom) NATURAL JOIN enrollment ORDER BY course_id ASC"

        time_slots = self.__displayTimeSlots()
        try:
            cur.execute(query, (values[0], values[1], values[0], values[1]))
            # Proper formatting for the list
            for line in cur:
                out = "{}-{} {}({}) {}-{}, {}/{} ".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                                                          line[7])
                out += time_slots[line[8]]
                print(out)
        except psycopg2.ProgrammingError as p:
            print("Error, please try again")
            print(p)

    # Helper function to get the timeslots displayed with proper formatting
    def __displayTimeSlots(self):
        cur = self.connection.cursor()
        cur2 = self.connection.cursor()
        cur3 = self.connection.cursor()
        query = "SELECT day FROM time_slot Where time_slot_id=%s ORDER BY CASE WHEN day = 'M' THEN 1 WHEN day = 'T' THEN 2 WHEN day = 'W' THEN 3 WHEN day = 'R' THEN 4 WHEN day = 'F' THEN 5 ELSE 6 END ASC"
        timeSlotKeys = []
        timeSlotValues = []
        try:
            cur.execute("SELECT DISTINCT(time_slot_id) as t_s_id FROM time_slot order by time_slot_id asc")

            for line in cur:
                timeSlotKeys.append(line[0])

            for day in timeSlotKeys:

                time = ""

                cur2.execute(query, (day,))

                for line in cur2:
                    time += line[0]

                cur3.execute(
                    "SELECT distinct(start_hr) as s_hr, start_min, end_hr, end_min From time_slot WHERE time_slot_id = %s",
                    (day,))
                x = cur3.fetchone()
                time += " {}:{}-{}:{}".format(x[0], format(x[1], "02"), x[2], x[3])
                timeSlotValues.append(time)
            return {timeSlotKeys[i]: timeSlotValues[i] for i in range(len(timeSlotKeys))}
        except  psycopg2.ProgrammingError as p:
            print("Error, please try again")
            print(p)

    # Registers students if they pass a few checks
    def registerStudent(self):

        cursor = self.connection.cursor()
        cur1 = self.connection.cursor()
        cur2 = self.connection.cursor()
        cur3 = self.connection.cursor()
        cur4 = self.connection.cursor()
        cur5 = self.connection.cursor()
        cur6 = self.connection.cursor()
        semester = input("What is the semester for the class you are trying to register for? ")
        year = input("What year is the class you are trying to register for? ")
        stud = input("What is your student ID? ")
        course = input("What is the course ID for the class? ")
        section = input("What section is the class? ")
        prereq_query = "select prereq_id from prereq where course_id = %s"

        query = "select course_id from takes where semester= %s and year= %s and ID=%s"
        p_query = "select distinct t.course_id from takes as t, prereq as p where t.course_id = p.prereq_id and t.id=%s and p.prereq_id = %s"
        cap_query = "select distinct s.course_id from classroom as c natural join section as s, takes where s.course_id = %s and s.year = %s and s.sec_id = %s and s.semester = %s and c.capacity > (select count(id) from takes where course_id = %s and year = %s and sec_id = %s and semester = %s)"
        # Find if course exists if not print error message
        try:
            cur5.execute(
                "select course_id from section where course_id = %s and semester = %s and year = %s and sec_id= %s",
                (course, semester, year, section))
        except psycopg2.ProgrammingError as p:
            print(p)
            print("Cannot get course info")
        if cur5.fetchone() is None:
            print("Course does not exist in this term")
            return 0
        # Find prereq info for a class
        try:
            cur1.execute(prereq_query, (course,))

        except psycopg2.ProgrammingError as p:
            print(p)
            print("Cannot get prereq info")
        prereq = cur1.fetchone()
        # if it has a prereq check if student has taken it
        if prereq is not None:
            try:
                cur2.execute(p_query, (stud, prereq))
            except psycopg2.ProgrammingError as p:
                print(p)
                print('Cannot find their prereq status')
            x = cur2.fetchone()

        # if there are no prereqs or he has taken them.
        if prereq is None or x is not None:
            try:
                cur = self.connection.cursor()
                # Check to make sure there is no class they are taking in the same term
                cur.execute(query, (semester, year, stud))
            except psycopg2.ProgrammingError as p:
                print(p)
                print("Error finding courses")
            # If there is a class at same semester and year for that student check timeslot
            if (cur.fetchone() is not None):
                # Finds timeslot of class they are taking at same time
                cur3.execute(
                    "Select s.Time_slot_id From section as s, takes as t Where t.ID = %s and s.course_id = t.course_id and s.year = t.year and s.sec_id = t.sec_id and s.semester = t.semester and t.semester= %s and t.year= %s",
                    (stud, semester, year))
                # finds timeslot of class they want to take
                cur4.execute(
                    "select time_slot_id from section where course_id = %s and sec_id = %s and year = %s and semester = %s",
                    (course, section, year, semester))

                z = cur4.fetchone()[0]
                # Loops through all classes they are taking that term and compares timeslots to the one they want to join. If there is a conflict it raises an error
                for x in cur3:

                    if (x[0] == z):
                        print("Error: conflicting timeslots")
                        return 0

            try:
                cur6.execute(cap_query, (course, year, section, semester, course, year, section, semester))
            except psycopg2.ProgrammingError as p:
                print(p)
                print("Error finding capacity")
            if cur6.fetchone() is None:
                print("Class is full")
                return 0
            # If the main query passes then insert the values into takes table
            try:
                cursor.execute("INSERT INTO Takes (ID, course_id, sec_id, semester, year) VALUES(%s, %s, %s, %s, %s)",
                               (stud, course, section, semester, year))
                print("Inserted")
            except psycopg2.ProgrammingError as p:
                print(p)
                print("Cannot insert")
        # Else he hasn't met the requirements
        else:
            print("Has not met prereq requirements")

        self.connection.commit()


s = small_example()

s_in = s.menu_print()
s.menu_handling(s_in)
while s_in != 'q'.lower:  # if input is '0' then it'll be handled
    s_in = s.menu_print()
    s.menu_handling(s_in)
    print("\nmenu selection is " + s_in + "\n")
