//Jasmine plans to generate this document using Java; kept the old document in case we pivot back
import java.util.Scanner;
import java.io.*;
import java.util.Random;
import java.text.DecimalFormat;
import java.time.LocalDateTime;

public class tableGen {
  private static int maxStudents = 4000, maxName = 4199, maxTrips = 1000, maxLeader = 1000, maxLeads = 5000, 
    maxRegisters = 40000, maxEquip = 1000, maxRentals = 40000, maxTripLoc = 50;
  // private static int numEquipNames = 29; //this needs to be changed if the file "equip_inv.txt" changes # entries
  private static int minStudentID = 930000000;
  private static int maxStudentID = 931999999;
  private static int curEquipID = 0;
  private static Random rnd = new Random();
  private static String[] tripLocationArray = new String[maxTripLoc];
  private static String[] tripActivityArray = {"Biking", "Hiking", "Backpacking", "Bird Watching", "Canoeing", "Camping", "Kayaking", "Paddleboarding", "Yoga Retreat", "Caving", "Climbing", "Surfing", "Skydiving"};
  private static String[] tripDescriptionArray = {"A trip you will never want to forget!", "Make friends that will last a lifetime!", "YOLO", "This beautiful trip is just what you need to escape your busy student schedule", "Join us for an outdoor adventure you will never forget!", "Details TBD.");
  private static int[] tripCapacityArray = {8,10,10,10,12,12,15,15,15,20,25}; //want 10 and 15 to be the most commonly-picked
  private static String[] rentalNoteArray = {"Double-check condition", "Returned item late in the past", "Suggestion", "Note A", "Note B", "Note C", "Note D", "Note E"};
  private static int[] nextTripID = new int[1000]; // starts at 0
  private static String[] studentNameArray = new String[maxName];  //first 20 values are TAP leaders
  private static String[] equipNameArray = new String[maxEquip];
  // private static String[] rentalsArray = new String[maxRentals];
  // private static Boolean[] registersArray = new Boolean[maxRegisters];

  //primary keys
  //trips
  private static int[] tripsTripID = new int[maxTrips];
  //students
  private static int[] studentsStudentID = new int[maxStudents];
  // private static String studentsName = new String[maxStudents]; //not a primary key but want unique names
  //equip_inv
  private static int[] equip_invEquipID = new int[maxEquip];
  //rentals
  private static int[] rentalsItemID = new int[maxRentals];
  private static int[] rentalsRenterID = new int[maxRentals];
  private static int[] rentalsCheckOutDT = new int[maxRentals];
  // registers
  private static int[] registersRegistrantID = new int[maxRegisters];
  private static int[] registersTripID = new int[maxRegisters];
  //leads
  private static int[] leadsLeadID = new int[maxLeads];
  private static int[] leadsTripID = new int[maxLeads];

  //----------------------The following methods are taken from https://www.db-book.com/db7/university-lab-dir/sample_tables-dir/largeRelations/tableGen.java
  private static String squote(int val) {
    return ("'"+val+"'");
    }
    private static String squote(String text) {
    return ("'"+text+"'");
    }
    private static Scanner openFile(String fileName) {
      Scanner in = null;
      try {
        in = new Scanner(new FileInputStream (fileName));
      }
      catch(FileNotFoundException e) {
        System.out.println ("Could not open the file");
        System.exit (0);
      }
      return in;
    }
    private static PrintWriter outputFile(String fileName) {
      PrintWriter out = null;
      try {
        out = new PrintWriter (new FileOutputStream (fileName));
      }
      catch (FileNotFoundException e) {
        System.out.println ("Could not open the file");
        System.exit (0);
      }
      return out;
    }
    private static void fillArrays() {
      int i;
      // fill studentNamesArray
      Scanner in = openFile("first_names");
      i = 0;
      while (in.hasNext() && i < maxName) {
        studentNameArray[i++] = in.nextLine();
      }
      in.close();
      //add last names to studentNamesArray
      Scanner in = openFile("last_names");
      i = 0;
      while (in.hasNext() && i < maxName) {
        i++;
        studentNameArray[i] = studentNameArray[i] + " " + in.nextLine();
      }
      if (i < maxName) maxName = i;
      in.close(); 
      // fill tripLocationArray
      in = openFile("trip_locations");
      i = 0;
      while (in.hasNext() && i < maxDept) {
        tripLocationArray[i++] = in.nextLine(); 
      }
      if (i < maxTripLoc) maxTripLoc = i;
      in.close();
      // fill equipNameArray
      in = openFile("equipment_names");
      i = 0;
      while (in.hasNext() && i < maxEquip) {
        equipNameArray[i++] = in.nextLine();
      }
      if (i < maxEquip) maxEquip = i;
      in.close();
    }
    //----------------------------------------------------End of copying code------------------------------------------

    private static int getCapacity() {
      //capacity SMALLINT
      int capin = rnd.nextInt(tripCapacityArray.length) // shuffling the list by index
      int capacity = tripCapacityArray[capin];
      return capacity;
    }
    private static int getTAPStatus() {
      // is_TAP_leader boolean
      return rnd.nextBoolean() ? 0 : 1;
    }
    private static int getStudentID() { //make sure to check not yet added
      // student_ID INTEGER [930000000,931999999]
      return rnd.nextInt((maxStudentID - minStudentID) + 1) + minStudentID;
    }
    private static String getName() {
      // name char(20)
      return nameArray[rnd.nextInt(maxName)];
    }
    private static int getTripID(D) {
      // trip_ID INTEGER
      // we'll have courses numbered 10000 - 30000
    return 100001 + rnd.nextInt(29999);
    }
    private static int getNextEquipID() { //may not need this method nor curEquipID
      // trip_ID INTEGER
      // we'll have courses numbered 10000 - 30000
      curEquipID++;
    return curEquipID++;
    }
    private static String getEquipName() {
      // name char(20)
      return equipNameArray[rnd.nextInt(maxEquip)];
    }

    private static LocalDateTime getTimeDate() {
      // start_date or end_date or due_dt or check_in_dt or check_out_dt, DATETIME
      // these are fixed with bounds 20-08-21 9:00 AM to 21-05-10 10:00 PM
      //'2020-11-12 13:00:00'
      //https://stackoverflow.com/questions/34051291/generate-a-random-localdate-with-java-time might need to fix
      LocalDateTime start = LocalDate.of(2020, Month.AUGUST, 21, 9, 0, 0); //date, hrs, min, sec
      LocalDateTime end = LocalDate.of(2021, Month.MAY, 10, 22, 0, 0);
      LocalDateTime random = RandomDates.between(start, end);
      assertThat(random).isBetween(start, end);
      return random;
    }

    private static String formatTimeDate(LocalDateTime td) {
      DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
      String formattedDateTime = td.format(myFormatObj);
      return formattedDateTime;
    }

    public static void main(String[] args) { 
      int trips = 200;
      int TAP_leader = 30; //for accuracy
      int equipment = 100;
      int rentals = 200;
      int leads = 100;
      int student = 2000;
      int registers = 20000;
      int i = 0, j = 0, new_id = 0, x = 0, y = 0, cap = 0, is_leader = 0;
      LocalDateTime start, end, due;
      boolean tryValue = true;
      String s = ""; //bool, dec, string
      fillArrays();
      //FILL TRIPS: trip activity array, trip description array, trip location array
      String act;
      String des;
      String loc;
      String title;
      String new_name;
      // fill classroom
      PrintWriter out = outputFile("KeepCalmAndQueryOn_generate.sql");
      //----------------------CLEAR OUT DB--------------------------------------
      out.println("delete from trips;");
      out.println("delete from students;");
      out.println("delete from equip_inv;");
      out.println("delete from rentals;");
      out.println("delete from registers;");
      out.println("delete from leads;");

      //----------------------FILL TRIPS--------------------------------------
      // PrintWriter out = outputFile("trips.txt");
      for (int i = 0; i < trips; trips++){
        // trip_ID
        tryValue = true;
        while (tryValue) {
          new_id = getTripID();
          tryValue = false;
          for (j = 0; j < i; j++) {
            if(new_id == tripsTripID[j]) tryValue = true;
          }
        }
        // title
        act = tripActivityArray[rnd.nextInt(tripActivityArray.length)]; //pick a random activity type
        loc = tripLocationArray[rnd.nextInt(tripLocationArray.length)]; //pick a random location
        title = act + " at " + loc;
        // start_date and end_date
        tryValue = true;
        while (tryValue) {
          start = getTimeDate();
          end = start.plusDays(1 + rnd.nextInt(2)); //add 1 to 2 days
          tryValue = false;
          for (j = 0; j < i; j++) {
            if(start.compareTo(end) > 0){
              System.out.println("Date 1 comes after Date 2");  
              tryValue = true;
            }
          }
        }
        // description
        des = tripDescriptionArray[rnd.nextInt(tripDescriptionArray.length)] //pick a random description
        // capacity
        cap = getCapacity();
        //I believe squote will add a singular quote around each, so DATETIME should be in the right format
        //string statement
        s = new_id.toString() + ", " + squote(title) + ", " + squote(formatTimeDate(start)) + ", " + squote(formatTimeDate(end)) + ", " + squote(loc) + ", " + squote(des) + ", " + cap.toString();
        out.println ("insert into trips values(" + s +");");
      }
      // out.close();  
      //----------------------FILL STUDENTS--------------------------------------
      // out = outputFile("students.txt");
      for (int i = 0; i < student; student++){
        // student_ID
        tryValue = true;
        while (tryValue) {
          new_id = getStudentID();
          tryValue = false;
          for (j = 0; j < i; j++) {
            if(new_id == studentsStudentID) tryValue = true;
          }
        }
        studentsStudentID[i] = new_id;
        // name
        tryValue = true;
        while (tryValue) {
          new_name = getName();
          tryValue = false;
          // for (j = 0; j < i; j++) {
          //   if(name == studentsName[j]) tryValue = true;
          // }
        } 
        // studentsName[i] = new_name; //if we want to make names unique
        //getting random 20 student TAP leaders for is_TAP_leader
        if (i < 20) {
          is_leader = 1;
        }
        else is_leader = 0;
        // string statement
        s = new_id.toString() + ", " + squote(name) + ", " + squote(is_leader);
        out.println ("insert into students values(" + s +");");
      }
      // out.close();  
      //----------------------FILL EQUIP_INV--------------------------------------
      // out = outputFile("equip_inv.txt");
      for (int i = 0; i < equipment; equipment++){
        // equip_ID
        tryValue = true;
        while (tryValue) {
          new_id = getNextEquipID();
          tryValue = false;
        }
        equip_invEquipID[i] = new_id;
        // equip_name
        tryValue = true;
        while (tryValue) {
          new_name = getEquipName();
          tryValue = false;
        }
        // condition [0,3]
        int condit = rnd.nextInt(4) //random val [0,3]
        //string statement
        s = new_id.toString() + ", " + squote(new_name) + ", " + condit.toString();
        out.println("insert into equip_inv values(" + s + ");");
      }
      // out.close();  
      //----------------------FILL RENTALS--------------------------------------
      // out = outputFile("rentals.txt");
      //CAREFUL: want to ensure an item isn't rented twice in one checkout period
      //note: not caring too much about it for simplicity in coding
      for (int i = 0; i < rentals; rentals++){
      // item_id
        int eq_id = equip_invEquipID[i % maxEquip]; //cycles through equipment to avoid double-booking
      // renter_id
        int ren_id = studentsStudentID[10*i]; //count by 10s, will stop at 1,990
      //check_out_dt
        tryValue = true;
        while(tryValue){
          start = getTimeDate();
          // due_dt
          due = start.plusDays(7);
          // check_in_dt
          end = start.plusdays(1 + rnd.nextInt(9)) //some people will turn in late
          tryValue = true;
          for (j = 0; j < i; j++) {
            if(start.compareTo(end) > 0 || start.compareTo(due)){
              System.out.println("Start date comes after due date or end date");  
              tryValue = true;
            }
          }
        }
        //notes
        String note = rentalNoteArray[rnd.nextInt(rentalNoteArray.length)]
        //string statment
        s = eq_id.toString() + ", " + ren_id.toString(), ", " + squote(formatTimeDate(start), + ", " + squote(formatTimeDate(due)) + ", " + squote(formatTimeDate(end)) + ", " + note));
        out.println ("insert into students values(" + s +");");
      }
      // out.close();  
      //----------------------FILL REGISTERS--------------------------------------
      // out = outputFile("registers.txt");
      //should prevent students from signing up for the same trip twice
      //TODO: should not allow leaders to sign up for their own trip
      for (int i = 0; i < registers; registers++){ //20,000 w/ 2,000 students so ~10/student
        //registrant_ID
        registersRegistrantID[i] = studentNameArray[rnd.nextInt(maxStudents)]; //random student
        //trip_ID
        registersTripID[i] = tripsTripID[i % maxTrips]; //walk through trip options
        s = registersRegistrantID[i].toString() + ", " + registersTripID[i].toString();
        out.println ("insert into registers values(" + s + ");");
      }
      // out.close();  
      //----------------------FILL LEADS--------------------------------------
      // out = outputFile("leads.txt");
      //two trips led per leader
      //TODO: should not allow a leader to register for the same trip twice
      //methodology: iterate through the 30 leaders backwards, two leaders per trip added, then go back through leaders again in same cycle until all trips have 2 leads
      //did not account for overlapping dates with trips
      for (int i = 0; i < leads; leads++){
        // lead_ID first leader
        leadsLeadID[i] = studentNameArray[TAP_leader - (i % TAP_leader)];
        // lead_ID second leader
        leadsLeadID[i+1] = studentNameArray[TAP_leader - (i % TAP_leader)];
        // trip_ID
        leadsTripID[i] = tripsTripID[i % trips]; //walk through trip options
        s = leadsLeadID[i].toString() + ", " + leadsTripID[i].toString();
        out.println("insert into leads values(" + s + ");");
        s = leadsLeadID[i+1].toString() + ", " + leadsTripID[i].toString();
        out.println("insert into leads values(" + s + ");");
      }
      // out.close();  
}