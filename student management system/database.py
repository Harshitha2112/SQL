import sqlite3


def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE c_table(cid INTEGER PRIMARY KEY  ,name text,duration text,charges text,description text)")
    con.commit()

    cur.execute("CREATE TABLE  Student(roll INTEGER PRIMARY KEY  ,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,address text)")
    con.commit()

    cur.execute("CREATE TABLE result(rid INTEGER PRIMARY KEY  ,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()

    con.close()
create_db()