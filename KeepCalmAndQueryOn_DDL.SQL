-- This database simulates a student recreation system that records information of students who may 
-- (a) rent out equipment, 
-- (b) lead TAP trips
-- (c) register to participate in TAP trips

-- ASSUMPTIONS
--Equipment for rent includes all rentable items
--Not all items will be rented out
--(0,all) students may participate in renting equipment from the rec
--Trips and classes can be added without instructors/leaders, so that they may be decided upon at a later date/time (generalization)
--leads won't try to sign up for their own courses
--trips can have 0+ leads but only three would mark themselves as leads on their end
--capacities do not have to match the same kind of trip (i.e. two trips to York River State Park don't automatically have the same capacity due to its name/same experience)

-- CREATE DATABASE KeepCalmAndQueryOn;
--Corresponds to room_reservations, name changed for simplicity
--will contain multiple instances if a certain room has multiple reservation slots
-- CREATE TABLE reservable_rooms
-- (
--     res_ID        SMALLINT,
--     start_time    TIME,
--     end_time      TIME,
--     name_num VARCHAR(20) NOT NULL, --ROOM NUMBER/NAME because "location" is a SQL type and can't be a variable name
--     PRIMARY KEY (res_ID)
-- );
-- CREATE TABLE gym_timeslots
-- (
--     time_slot_ID      SMALLINT,
--     start_time        TIME,
--     end_time          TIME,
--     PRIMARY KEY (time_slot_ID)
-- );
--IDEA:  'classification' could be included in ID with a code (aka if it starts with a '1', it's a GF class)
-- CREATE TABLE classes
-- (
--     class_ID          SMALLINT,  --Classification aka type of class (Fitwell Class, Fitwell Series, Mindfulness, etc.) coded here too
--     class_name        VARCHAR(50),
--     class_description VARCHAR(200),
--     PRIMARY KEY (class_ID),
-- );

--new to separate and clarify
-- CREATE TABLE class_sections
-- (
--     class_ID          SMALLINT,  --Classification aka type of class (Fitwell Class, Fitwell Series, Mindfulness, etc.) coded here too
--     instructor_name   VARCHAR(50),
--     dow               VARCHAR(1), --M,T,W,R,F
--     start_time        TIME,
--     end_time          TIME,
--     room_name_num     VARCHAR(20), --name and number because "location" is a SQL type and can't be a variable name
--     PRIMARY KEY (class_ID, start_time, room_name_num), --two classes can't start at the same time at the same place
--     FOREIGN KEY (instructor_name) REFERENCES staff_members ON DELETE SET NULL
-- );

-- DROP TABLE IF EXISTS
--     trips,
--     students,
--     equip_inv,
--     rentals,
--     registers,
--     leads,
-- CASCADE;

--records all trips that have taken place, are taking place, and are planned for the future
CREATE TABLE trips
    (trip_ID         INTEGER,
    title            VARCHAR(100),
    trip_start       TIMESTAMP, 
    trip_end         TIMESTAMP, 
    destination      VARCHAR(50),
    trip_description VARCHAR(200), 
    capacity         SMALLINT,
    PRIMARY KEY (trip_ID),
    CHECK (trip_start < trip_end)
    );

--lists all students, some of which who are qualified to lead
CREATE TABLE students
    (student_ID      INTEGER,
    student_name    VARCHAR(50) NOT NULL,
    is_TAP_leader   BOOLEAN, --students who are not qualified should not be in "leading"; 0 false, true otherwise
    PRIMARY KEY (student_ID)
    );

--lists all equipment of any rental status
CREATE TABLE equip_inv
    (equip_ID            INTEGER,
    equip_name          VARCHAR(20),
    current_condition   SMALLINT, -- 0 = "New/Like New", 1 = "Good", 2 = "Poor/Dirty", 3 = "Needs Repair/Retire -- Action needed (out of use)"
    PRIMARY KEY (equip_ID)
    --FOREIGN KEY (current_condition) REFERENCES rentals, --check_in_condition, but if it isn't in the relation that's also okay
    );

--records all rentals that have taken and are currently taking place
CREATE TABLE rentals
    (item_ID             INTEGER,
    renter_ID           INTEGER,
    check_out_dt        TIMESTAMP, --changed from timestamp, I feel like for consistency this would be easier --Jasmine
    -- check_out_condition  SMALLINT NOT NULL, 
    due_dt              TIMESTAMP NOT NULL, --this should be 7 days after check_out_dt, but doesn't have to be, which is why we keep (staff member enters manually)
    check_in_dt         TIMESTAMP, --same here
    -- check_in_condition  SMALLINT, --want this to change "current_condition" in equip_inv on check-in, will do in menu?
    notes               VARCHAR(100), --can't have default empty string
    PRIMARY KEY (item_ID,renter_ID,check_out_dt),
    FOREIGN KEY (item_ID) REFERENCES equip_inv
        ON DELETE CASCADE,
    FOREIGN KEY (renter_ID) REFERENCES students
        ON DELETE CASCADE,
    --FOREIGN KEY (check_in_condition) REFERENCES equip_inv,
    CHECK (check_out_dt < due_dt),
    CHECK (check_out_dt < check_in_dt),
    );
--records all previous and current registrations for TAP trips
CREATE TABLE registers
    (registrant_ID   INTEGER, --TAP leaders and non-TAP leaders alike may register for trips
    trip_ID         INTEGER,
    PRIMARY KEY (registrant_ID,trip_ID),
    FOREIGN KEY (registrant_ID) REFERENCES students
        ON DELETE CASCADE,
    FOREIGN KEY (trip_ID) REFERENCES trips
        ON DELETE CASCADE,
    );

--records all TAP leaaders who currently/have been registered to lead trips, recorded per trip
--thus, a TAP leader can be in multiple tuples associated with different  s
CREATE TABLE leads
    (
    lead_ID   INTEGER, --CHECK students.is_TAP_leader == 0, --check that tuple in students relation is qualified,
    trip_ID   INTEGER,
    PRIMARY KEY (lead_ID,trip_ID),
    FOREIGN KEY (lead_ID) REFERENCES students
        ON DELETE CASCADE,
    FOREIGN KEY (trip_ID) REFERENCES trips
        ON DELETE CASCADE,
    );
 
