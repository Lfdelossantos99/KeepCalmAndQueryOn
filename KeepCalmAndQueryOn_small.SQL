/*
Populating DB for small-scale testing
*/

--db-book.com (sample data for files)


delete from rentals;
delete from registers;
delete from leads;
delete from equip_inv;
delete from trips;
delete from students;
--TRIPS: ID,title,start date/time,end date/time,location,description,capacity
insert into trips values (10000, 'Pathways Surfing Adventure', '2020-08-21 09:00:00', '2020-08-28 18:30:00', 'James River', 'Grab a buddy for a day of paddling along the beautiful James River',10);
insert into trips values (11110, 'Canoe Camping at Great Dismal Swamp', '2020-09-18 11:30:00', '2020-09-20 17:30:00', 'Great Dismal Swamp', '', 12);
insert into trips values (11111, 'York River Day Hike', '2020-10-08 06:30:00', '2021-10-08 21:00:00', 'York River', 'Restorative hike and picnic along the banks of the beautiful York River.', 15);
insert into trips values (11234, 'Weekend Backpacking in Shenandoah', '2020-10-15 08:30:00', '2020-10-17 21:30:00', 'Shenandoah', 'Put your backpacking skills to the test on the AT!', 10);
insert into trips values (11340, 'Cape Hatteras Camping Adventure', '2020-10-26 07:00:00', '2020-10-28 14:00:00', 'Cape Hatteras', '', 8);
insert into trips values (13444, 'Fall Day Hike in Richmond', '2020-11-05 08:30:00', '2020-11-07 21:30:00', 'Richmond', '', 12);
insert into trips values (24340, 'York River Day Hike', '2021-02-26 06:30:00', '2021-02-26 21:00:00', 'York River', 'Restorative hike and picnic along the banks of the beautiful York River.', 15);
insert into trips values (21345, 'Backpacking in Harper''s Ferry', '2021-03-10 07:00:00', '2021-03-12 14:00:00', 'Harper''s Ferry', 'This is a 3-day backpacking trip you''ll never forget!', 10);
insert into trips values (30435, 'Canoeing on the Upper James River', '2021-04-01 08:30:00', '2021-04-01 21:30:00', 'James River', 'Grab a buddy for a day of paddling along the beautiful James River', 15);
insert into trips values (32225, 'Caving at Glade Cave', '2021-04-20 010:00:00', '2021-04-22 13:00:00', 'Glade Cave', 'Experience Virginia''s own Glade Cave', 10);
insert into trips values (32244, 'Canoeing on the Upper James River', '2021-05-01 08:30:00', '2021-05-02 21:30:00', 'James River', 'Grab a buddy for a day of paddling along the beautiful James River', 20);
insert into trips values (34599, 'Skydiving in Virginia', '2021-05-11 06:00:00', '2021-05-11 17:00:00', 'Virginia', 'Enjoy the end of the semester with a once-in-a-lifetime experience!', 15);
--STUDENTS: ID,name,bool is_TAP_leader (0 if F)
insert into students values (930000000,'John Doe', '0');
insert into students values (930557448, 'Johanna Deverick', '0');
insert into students values (931453457, 'Jamie Jones', '0');
insert into students values (930454308, 'Alex Cameron', '0');
insert into students values (930303444, 'Omar Johnson', '0');
insert into students values (930040002, 'Michaela Hilton', '0');
insert into students values (931405002, 'Aaron Aarde', '0');
insert into students values (931405223, 'Archibald Andrews', '0');
insert into students values (930092455, 'Athena Moon', '0');
insert into students values (930302108, 'Ferdison Cayetana', '0');
insert into students values (930212212, 'Tamara Williams', '0');
insert into students values (930552109, 'Margaret Spencer', '0');
insert into students values (930222333, 'Tanya Jones', '0');
insert into students values (930567234, 'Amber Mundy', '0');
insert into students values (930987645, 'Beth Carter', '0');
insert into students values (930987655, 'Jacob Filbert', '0');
insert into students values (931187655, 'Peter Sakai', '0');
insert into students values (931345678, 'River Fields', '1');
insert into students values (931039455, 'Pooja Karandikar', '1');
insert into students values (931039456, 'Jon Stewart', '1');
insert into students values (930049448, 'Ferdison Cayetana', '1');
insert into students values (931345670, 'Savannah George', '1');
insert into students values (930987888, 'Alvaro Rivera', '1');
insert into students values (930334549, 'Angela Diaz', '1');
insert into students values (931029455, 'Alyssa Adams', '1');
insert into students values (930245678, 'Jin Lee', '1');
insert into students values (931340008, 'Jose Fernandez', '1');
--EQUIP_INV: ID,name,current_condition
insert into equip_inv values (14508,'Camping Chair', 0);
insert into equip_inv values (22495,'Camping Chair', 1);
insert into equip_inv values (32345,'Camping Chair', 2);
insert into equip_inv values (42111,'Camping Chair', 2);
insert into equip_inv values (50039,'Camping Chair', 3);
insert into equip_inv values (00001,'Camping Stove', 0);
insert into equip_inv values (00021,'Sleeping Bag', 1);
insert into equip_inv values (00022,'Sleeping Bag', 1);
insert into equip_inv values (00232,'Sleeping Pad', 2);
insert into equip_inv values (00023,'Flashlight', 3);
--RENTALS: item_ID,renter_ID,check_out_dt,due_dt,check_in_dt,notes, ~12
insert into rentals values (14508, 930000000, '2021-03-10 13:00:00', '2021-03-17 13:00:00', '2021-03-12 10:00:00'); --default note value: NULL
insert into rentals values (14508, 930000000, '2021-03-21 13:00:00', '2021-03-28 13:00:00', '2021-03-24 13:00:00');
insert into rentals values (14508, 931453457, '2021-04-10 13:00:00', '2021-04-17 13:00:00', '2021-04-12 10:00:00');
insert into rentals values (22495, 930557448, '2020-11-12 13:00:00', '2020-11-19 13:00:00', '2020-11-14 12:00:00');
insert into rentals values (00232, 930557448, '2020-11-12 13:00:00', '2020-11-19 13:00:00', '2020-11-14 12:00:00');
insert into rentals values (00022, 930557448, '2020-11-12 13:00:00', '2020-11-19 13:00:00', '2020-11-14 12:00:00');
insert into rentals values (22495, 930557448, '2021-03-12 13:00:00', '2021-03-19 13:00:00', '2021-03-14 12:00:00');
insert into rentals values (32345, 930222333, '2021-03-12 13:00:00', '2021-03-19 13:00:00', '2021-03-19 11:00:00');
insert into rentals values (22495, 931340008, '2020-09-12 13:00:00', '2020-09-19 13:00:00', '2020-09-14 12:00:00');
insert into rentals values (50039, 931340008, '2020-09-12 13:00:00', '2020-09-19 13:00:00', '2020-09-14 12:00:00');
insert into rentals values (42111, 931340008, '2020-09-12 13:00:00', '2020-09-19 13:00:00', '2020-09-14 12:00:00');
insert into rentals values (00021, 930557448, '2021-05-12 13:00:00', '2021-05-19 13:00:00', '2021-05-14 12:00:00');
insert into rentals values (00021, 930557448, '2021-03-12 13:00:00', '2021-03-19 13:00:00', '2021-03-14 20:00:00');
--REGISTERS: registrant_ID,trip_ID
--checked that leaders listed here aren't leading that trip (ID)
--checked that students aren't signed up twice under the same trip
insert into registers values (930000000,10000);
insert into registers values (930000000,11111);
insert into registers values (930000000,13444);
insert into registers values (930000000,30435);
insert into registers values (930000000,34599);
insert into registers values (931453457,10000);
insert into registers values (930454308,10000);
insert into registers values (930303444,10000);
insert into registers values (930040002,10000);
insert into registers values (931405002,11234);
insert into registers values (931405223,11234);
insert into registers values (930987655,11234);
insert into registers values (930000000,11234);
insert into registers values (931453457,11234);
insert into registers values (930303444,11234);
insert into registers values (930302108,11234);
insert into registers values (930212212,11234);
insert into registers values (930567234,11234);
insert into registers values (930454308,24340);
insert into registers values (930303444,24340);
insert into registers values (930040002,24340);
insert into registers values (931405002,24340);
insert into registers values (930092455,24340);
insert into registers values (930212212,24340);
insert into registers values (930567234,24340);
insert into registers values (930987655,24340);
insert into registers values (931187655,24340);
insert into registers values (931345678,24340);
insert into registers values (931340008,24340);
insert into registers values (930245678,24340);
insert into registers values (931187655,21345);
insert into registers values (930987645,21345);
insert into registers values (930567234,21345);
insert into registers values (930222333,21345);
insert into registers values (930303444,21345);
insert into registers values (930303444,34599);
--LEADS: lead_ID,trip_ID
--checked that students listed here aren't registered for that trip (ID)
--checked that tap leaders aren't leading the same trip twice
insert into leads values (930049448, 10000);
insert into leads values (930049448, 11111);
insert into leads values (930049448, 11234);
insert into leads values (931029455, 10000);
insert into leads values (931029455, 11234);
insert into leads values (931345678, 13444);
insert into leads values (931039455, 11340);
insert into leads values (931039456, 34599);
insert into leads values (931345670, 34599);
insert into leads values (930987888, 30435);
insert into leads values (930334549, 13444);
insert into leads values (930334549, 11111);
insert into leads values (931029455, 32225);
insert into leads values (930245678, 32244);
insert into leads values (931340008, 32225);
insert into leads values (931340008, 30435);
insert into leads values (930987888, 24340);
insert into leads values (931345670, 24340);
insert into leads values (931039456, 21345);
