import psycopg2

class small_example:

    def __init__(self):
        self.connection = psycopg2.connect(host="localhost", port=5432, dbname="small_example", user="jkhow")

    def menu_print(self):
            return input("==================================\n"
                         "| Please select an option:       |\n"
                         "| 0  Exit                        |\n"
                         "| 1  List Available Equipment    |\n"
                         "| 2  Equipment Check Out/In      |\n" #make sure equipment is checked in; make sure equipment is checked out and by that person; ask user to enter check_in condition and change in equip_inv
                         "| 3  Register for TAP Trip       |\n" #make sure to check that student isn't leading the trip and student/trip exists and trip hasn't already completed
                         "| 4  Generate Trip Records       |\n" #name, start/end dates, who's leading, who's signed up
                         "| 5  Generate TAP Leader Records |\n" #TAP leader name, number of trips led\n (list:) date of trip, name of trip
                         "==================================\n"
                         "Input: ")

    # prints menu and returns the input, not yet validated

    # takes input from menu_selection method, validates input, and calls corresponding method
    # returns
    def menu_handling(self, ins_input):
        isValid = False
        cur_input = ins_input
        while isValid == False:
            if cur_input == '0':
                print("Goodbye!")
                self.connection.close()
                quit()
            elif (cur_input == '1'):
                print("Generating all available equipment for rent...")
                self.listAvailableEquip() #TODO: create method to check machine inventory
                isValid = True
            elif (cur_input == '2'):
                print("Welcome to Equipment Check Out/Check In!")
                self.equipCheckInOut() #TODO: create method to check machine inventory
                isValid = True
            elif (cur_input == '3'):
                print("Welcome to TAP Trip Registration!")
                self.registerStudent()
                isValid = True
            elif (cur_input == '4'):
                print("Generating Trip Records....")
                self.TAP_tripList #TODO: finish implementing this method
                isValid = True
            elif (cur_input == '5'):
                print("Generating TAP Leader Records...")
                # self.generateLeaderLog()
                isValid = True
            else:
                cur_input = input("Please enter valid input (number 0 to 5): ")
        return

    # Generates all equipment currently available for rent
    def listAvailableEquip(self):
        cur = self.connection.cursor()
        # noinspection SqlResolve
        query = "SELECT equip_name, current_condition FROM equip_inv WHERE equip_ID NOT IN (SELECT item_ID FROM rentals WHERE check_in_dt is NULL);"
        try:
            cur.execute(query)
            print("Equipment Name | Current Condition\n")
            for line in cur:
                print("{} | {}".format(line[0], line[1]))
            print("If you are interested in checking out equipment refer to option 2.\n")
        except psycopg2.ProgrammingError as p:
            print("Error, please try again")
            print(p)

    # Generates checks out all equipment
    def isValidItem(self, item_ID):
            cur = self.connection_cursor()
           
            q = "SELECT equip_name, current_condition FROM equip_inv WHERE equip_ID = %d;"
            try:
                cur.execute(q, item_ID)
            except psycopg2.ProgrammingError as p:
                print("Error, please try again")
                print(p)
                if cur.fetchone() is not None:
                    return True
                else:
                    return False

    def equipCheckInOut(self):


        cur = self.connection.cursor()
        print("Are you interested in checking equipment in or out?\n")
        var = input("Please enter in or out.\n")
        while True:
            if var == "q":
                return
            elif var == "in" or "out":
                break
            else:
                var = input("I'm sorry, I did not understand. Please enter in or out (you may enter q to exit).\n")
        if var == "out":
            print("The following equipment is eligible to be checked out\n")
            self.listAvailableEquip()
            IDPair = input(
                "What would you like? Please enter item ID and your ID separated by whitespace: item_ID your_ID\n")
            # Check if item_ID is valid
            if not self.isValidItem(IDPair[0]):
                print("Invalid item, try again.\n")
                return
            # noinspection SqlResolve
            query = "INSERT INTO rentals (item_ID, renter_ID, check_out_dt, check_in_dt) VALUES (%d, %d, (SELECT NOW()), (SELECT NOW() + INTERVAL '1 week'));"
        try:
            cur.execute(query, IDPair)
        except psycopg2.ProgrammingError as p:
            print("Error, please try again")
            print(p)
            return "Done"
        else:
            item_ID = input("What equipment are you checking in today? Please enter the equipment's item_ID.\n")
            if not self.isValidItem(item_ID):
                print("Invalid item, try again.\n")
                return
            query = "if (SELECT due_dt FROM rentals WHERE item_ID=%s AND check_in_dt IS NULL) - SELECT NOW() > 000 days 00:00:00 then UPDATE rentals SET (check_in_dt = (SELECT NOW()), notes = 'Turned in late!') WHERE item_ID=%s AND check_in_dt IS NULL else UPDATE rentals SET check_in_dt = (SELECT NOW()) WHERE item_ID=%s AND check_in_dt IS NULL"
        try:
            cur.execute(query, item_ID)
        except psycopg2.ProgrammingError as p:
            print("Error, please try again")
            print(p)
            return "Done"

    # Registration system for students to attend TAP trips
    def registerStudent(self):
        cur = self.connection.cursor()
        IDPair = input(
            "Please input your ID \n")
        trip = input("input ID of the trip you wish to register ")
     
        query = "INSERT INTO registers (registrant_ID, trip_ID) VALUES (%d, %d)"
        try:
            cur.execute(query, IDPair, trip)
        except psycopg2.ProgrammingError as p:
            print("Error, please try again")
            print(p)
        return "Done"


    # Generates list of TAP trips and each trip's specific details
    def TAP_tripList(self):
        cur = self.connection.cursor()
        query = "SELECT * FROM trips"
        print("trip ID | Title | start | end | destination | description |capacity")
        try:
            cur.execute()
            for line in cur:
                print("{} | {} | {} | {} | {} | {} |{}".format(line[0], line[1], line[2], line[3], line[4], line[5],
                                                               line[6]))
        except psycopg2.ProgrammingError as p:
             print("Error, please try again")
             print(p)
        return "Done"

    #generates details for a specific trip, people on trip, leader, and so forth
    def TAP_tripDetails(self, trip_ID):
    # Generates list of TAP leaders, their trip count, and other details
    # self.generateLeaderLog()
        pass

s = small_example()

s_in = s.menu_print()
s.menu_handling(s_in)
while s_in != 'q'.lower:  # if input is '0' then it'll be handled
    s_in = s.menu_print()
    s.menu_handling(s_in)
    print("\nmenu selection is " + s_in + "\n")