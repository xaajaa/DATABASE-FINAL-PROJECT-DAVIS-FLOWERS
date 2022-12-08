import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('PawesomePets.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor
query = """
    CREATE TABLE Clinic (
    ClinicNo            varchar (8),
    clinic_name         varchar(255)    NOT NULL,
    address             varchar(255)    NOT NULL,
    clinic_phone        varchar(20)     NOT NULL    CHECK (clinic_phone NOT LIKE '%[^0-9]%'),
    PRIMARY KEY (clinicNo)
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)
query = """
    CREATE TABLE Staff (
    staffNo         varchar(8),
    staff_name      varchar(255)    NOT NULL,
    staff_address   varchar(255),
    staff_phone     varchar(20)     CHECK (staff_phone not like '%[^0-9]%'),
    DOB             date            NOT NULL,
    salary          int             NOT NULL,
    position        varchar(255),
    clinicNo        varchar(8),
    PRIMARY KEY (staffNo),
    FOREIGN KEY (clinicNo) REFERENCES Clinic ON DELETE SET NULL
);
    """

# Execute query, the result is stored in cursor
cursor.execute(query)
query = """
    PRAGMA foreign_keys = OFF;
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Clinic2(
    clinicNo            varchar (8),
    clinic_name         varchar(255)    NOT NULL,
    address             varchar(255)    NOT NULL,
    clinic_phone        varchar(20)     NOT NULL    CHECK (clinic_phone NOT LIKE '%[^0-9]%'),
    managerNo           varchar (8),
    PRIMARY KEY (clinicNo)
);
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    DROP TABLE Clinic
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    ALTER TABLE Clinic2 RENAME TO Clinic
    """
# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    PRAGMA foreign_keys = ON;
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Owner ( 
    ownerNo         varchar(8), 
    owner_name      varchar(255)    NOT NULL, 
    owner_address   varchar(255), 
    owner_phone     varchar(20)     NOT NULL    CHECK (owner_phone not like '%[^0-9]%'), 
    PRIMARY KEY (ownerNo)
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Pet ( 
    petNo       varchar(8), 
    pet_name    varchar(255), 
    pet_DOB     date, 
    species     varchar(255), 
    breed       varchar(255),
    color       varchar(255),
    ownerNo     varchar(8),
    clinicNo    varchar(8),
    PRIMARY KEY (petNo),
    FOREIGN KEY (ownerNo) references Owner      ON DELETE SET NULL,
    FOREIGN KEY (clinicNo) references Clinic    ON DELETE SET NULL
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Examination (
    examNo              varchar(8),
    chief_complaint     varchar(255),
    description         varchar(255),
    exam_date           date            NOT NULL,
    actions_taken       varchar(255),
    staffNo             varchar(8)      NOT NULL,
    petNo               varchar(8)      NOT NULL,
    PRIMARY KEY (examNo),
    FOREIGN KEY (staffNo) references Staff,
    FOREIGN KEY (petNo) references Pet
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# Insert row into table
#insert into CLINC
query = """
    INSERT INTO Clinic
    VALUES('CL551155', 'Atsbury Vale Pawesome', '555 Relevance Street, Miami, Florida', 5055055505, null);
    """
cursor.execute(query)

query = """
    INSERT INTO Clinic
    VALUES('CL551156', 'Trainsbury Vale Pawesome', '444 Irrelevant Street, Miami, Florida', 6066066606, null);
    """
cursor.execute(query)

query = """
    INSERT INTO Clinic
    VALUES('CL111111', 'Range Rider Pawesome', '123 MadeUp Street, Hollywood, Florida', 1231239876, null);
    """
cursor.execute(query)

query = """
    INSERT INTO Clinic
    VALUES('CL999999', 'Open Window Pawesome', '6091 Shutter Rd, Vilewood, Ohio', 111111111111, null);
    """
cursor.execute(query)

query = """
    INSERT INTO Clinic
    VALUES('CL222222', 'Best Value Pawesome', '1999 BestValue Street, Money, New York', 9999999999, null);
    """
cursor.execute(query)

# INSERT INTO STAFF

query = """
    INSERT INTO Staff
    VALUES ('ST000000', 'Mr. Pawesome', '1111 Pawesome Road, Pawesome Town, Florida', '9989989998', date('1960-01-01'), 1000000, 'CEO', 'CL111111');
    """
cursor.execute(query)

query = """
    INSERT INTO Staff
    VALUES ('ST444555', 'Richard Price', '222 Steal Road, Rome, New York', '4561237890', date('1999-05-12'), 100000, 'Manager', 'CL222222');
    """
cursor.execute(query)

query = """
    INSERT INTO Staff
    VALUES ('ST999999', 'Vet Erinarian', '554 Pet Lover St, Pawesome Town, Florida', '9989989998', DATE('1989-04-22'), 800000, 'Veterinarian', 'CL551155');
    """
cursor.execute(query)

query = """
    INSERT INTO Staff
    VALUES ('ST555555', 'John Doe', '111 Road Road, Town Town, State State', '1010100011', DATE('2001-11-28'), 50000, 'Front Desk', 'CL222222');
    """
cursor.execute(query)

query = """
    INSERT INTO Staff
    VALUES ('ST111111', 'Something Cool', '2005 Old Town Road, Lil Nas Town, Oregon', '1234561234', DATE('2005-04-01'), 80000, 'Veterinarian', 'CL999999');
    """
cursor.execute(query)

query = """
    INSERT INTO Staff
    VALUES ('ST666666', 'Drew Freeze', '1002 Johnt Rd, Jackson, Florda', '4443330091', DATE('1992-11-01'), 90000, 'Veterinarian', 'CL551156');
    """
cursor.execute(query)

#ADD MANAGER
query = """
    UPDATE CLINIC
    SET managerNo = 'ST000000'
    WHERE clinicNo = 'CL111111';
    """
cursor.execute(query)

query = """
    UPDATE CLINIC
    SET managerNo = 'ST444555'
    WHERE clinicNo = 'CL222222';
    """
cursor.execute(query)

query = """
    UPDATE CLINIC
SET managerNo = 'ST999999'
WHERE clinicNo = 'CL551155';
    """
cursor.execute(query)

query = """
    UPDATE CLINIC
    SET managerNo = 'ST111111'
    WHERE clinicNo = 'CL999999';
    """
cursor.execute(query)

#ADD OWNERS

query = """
    INSERT INTO Owner
Values ('OW111111', 'Worst Friend', '124 Friend St, Friendtown, Texas', '8877655309');
    """
cursor.execute(query)

query = """
    INSERT INTO Owner
Values ('OW555555', 'Best Friend', '123 Friend St, Friendtown, Texas', '9999990000');
    """
cursor.execute(query)

query = """
    INSERT INTO Owner
Values ('OW333333', 'Alfred Batman', '2239 Color Blvd, Portland, Florida', '1020020004');
    """
cursor.execute(query)

query = """
    INSERT INTO Owner
Values ('OW222222', 'John Cena', '4432 Anchor Rd, Allen, Florida', '9827737465');
    """
cursor.execute(query)

query = """
    INSERT INTO Owner
Values ('OW444444', 'Amon Gus', ' 1 Overgrowth Rd, Vilewood, Ohio', '4324324433');
    """
cursor.execute(query)

#ADD PETS

query = """
   INSERT INTO Pet
Values ('PT000000', 'Bubbles Cena', DATE('2020-09-09'), 'Dog', 'Terrier', 'Natural Blonde', 'OW222222', 'CL999999');
    """
cursor.execute(query)

query = """
    INSERT INTO Pet
Values ('PT111111', 'Catman', DATE('2020-07-19'), 'Cat', 'Short-Hair', 'Tuxedo', 'OW333333', 'CL111111');
    """
cursor.execute(query)

query = """
    INSERT INTO Pet
Values ('PT222222', 'Milo', DATE ('2020-06-15'), 'Cat', 'Short-Hair', 'Tuxedo', 'OW444444', 'CL999999');
    """
cursor.execute(query)

query = """
    INSERT INTO Pet
Values ('PT333333', 'Jessie Friend', DATE ('2017-09-20'), 'Dog', 'Husky', 'White/Black', 'OW111111', 'CL551155');
    """
cursor.execute(query)

query = """
    INSERT INTO Pet
Values ('PT444444', 'Crazy Frog', DATE ('2022-11-20'), 'Frog', 'Frog', 'Green', 'OW555555', 'CL222222');
    """
cursor.execute(query)

#ADD EXAMINATION


query = """
   INSERT INTO Examination
Values('EX000000', 'Dog was having trouble using the restroom', 'Terrier is stopped up!', DATE ('2022-11-28'), 'Unclogged the Dog', 'ST111111', 'PT000000');
    """
cursor.execute(query)

query = """
    INSERT INTO Examination
Values('EX111111', 'Cat was meowing too loud', 'Small kitten has vocal chords that are three times too large', DATE ('2022-07-30'), 'Gave the cat growth hormones so he will grow to the size of his vocal chords', 'ST000000', 'PT111111');
    """
cursor.execute(query)

query = """
    INSERT INTO Examination
Values('EX222222', 'Dog is still having trouble using the restroom', 'Terrier is still stopped up!', DATE ('2022-12-02'), 'Unclogged the dog again', 'ST111111', 'PT000000');
    """
cursor.execute(query)

query = """
    INSERT INTO Examination
    Values('EX333333', 'Frog laid its eggs, but has not been eating since', 'Small green frog is underweight and needs to be given nutrients', DATE ('2022-01-28'), 'Fed the Frog', 'ST444555', 'PT444444');
    """
cursor.execute(query)

query = """
    INSERT INTO Examination
Values('EX444444', 'Dog has been fainting on walks', 'Large Male Husky has irregular heartbeat', DATE ('2022-07-18'), 'Gave the owner medication to give the dog once a day', 'ST999999', 'PT333333'); 
   """
cursor.execute(query)


# Select data
query = """
    SELECT *
    FROM Clinic
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

print("\n\n")

query = """
    SELECT *
    FROM Staff
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print("\n\n")

query = """
    SELECT *
    FROM Owner
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print("\n\n")

query = """
    SELECT *
    FROM Pet
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

print("\n\n")

query = """
    SELECT *
    FROM Examination;
    """
cursor.execute(query)


# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print("\n\n")

#START OF QUERIES
# Select data

#List all staff and the clinic they work at with salary greater than 100000$
query = """
    SELECT staff_name, staffNo, salary, clinic_name
    FROM Staff s, Clinic c
    WHERE salary > 100000 AND s.clinicNo = c.clinicNo
    Group BY clinic_name, staff_name, staffNo, salary;
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

print("\n\n")

#List All clinics that do not have a manager

query = """
    SELECT *
    FROM Clinic
    WHERE managerNo IS NULL;
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print("\n\n")

#List the number of staff at each clinic

query = """
    SELECT COUNT(staffNo) as numStaff, c.clinicNo, clinic_name
    FROM Staff s, Clinic c
    Where s.clinicNo = c.clinicNo
    GROUP BY c.clinicNo, clinic_name;
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print("\n\n")

#List the managers and their respective location

query = """
    SELECT s.*, clinic_name
    FROM Staff s, Clinic c
    WHERE c.managerNo = s.staffNo;
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

print("\n\n")

#List All Exams done by Staff member "Something Cool"
query = """
    SELECT e.*
FROM Examination e, Staff s
WHERE e.staffNo = s.staffNo and staff_name IS "Something Cool"
    """
cursor.execute(query)


# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)


# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
