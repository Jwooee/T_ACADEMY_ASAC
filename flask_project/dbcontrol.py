from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_reset_session=True,
                                    pool_size=3, host="localhost", port=3306,
                                    database="flaskdb", user="root", password="1234")



def selectbase(company):
    con = pool.get_connection()
    c = con.cursor()
    c.execute(f"select pname, cat, shape, desc_med  from medinfo where cname='{company}'")
    data = c.fetchall()
    con.close()
    return data

def selectmed(company, pname):
    con = pool.get_connection()
    c = con.cursor()
    c.execute(f"select pname, cat, shape, desc_med from medinfo where cname='{company}' and pname like '%{pname}%';")
    data = c.fetchall()
    con.close()
    return data

def selectbase1(company):
    con = pool.get_connection()
    c = con.cursor()
    c.execute(f"select pname, cat, shape, desc_med from medinfo where cname='{company}' and cat='의약품';")
    data = c.fetchall()
    con.close()
    return data

def selectmed1(company, pname):
    con = pool.get_connection()
    c = con.cursor()
    c.execute(f"select pname, cat, shape, desc_med from medinfo where cname='{company}' and pname like '%{pname}%' and cat='의약품';")
    data = c.fetchall()
    con.close()
    return data

def selectbase2(company):
    con = pool.get_connection()
    c = con.cursor()
    c.execute(f"select pname, cat, shape, desc_med from medinfo where cname='{company}' and cat='의약외품';")
    data = c.fetchall()
    con.close()
    return data

def selectmed2(company, pname):
    con = pool.get_connection()
    c = con.cursor()
    c.execute(f"select pname, cat, shape, desc_med from medinfo where cname='{company}' and pname like '%{pname}%' and cat='의약외품';")
    data = c.fetchall()
    con.close()
    return data

def selectbase3(company):
    con = pool.get_connection()
    c = con.cursor()
    c.execute(f"select pname, cat, shape, desc_med from medinfo where cname='{company}' and cat='한약(생약)제제등';")
    data = c.fetchall()
    con.close()
    return data


def selectmed3(company, pname):
    con = pool.get_connection()
    c = con.cursor()
    c.execute(f"select pname, cat, shape, desc_med from medinfo where cname='{company}' and pname like '%{pname}%' and cat='한약(생약)제제등';")
    data = c.fetchall()
    con.close()
    return data

def insertmed(pname, cname, cat, desc_med, shape):
    con = pool.get_connection()
    c = con.cursor()
    c.execute(f"insert into medinfo values('{pname}', '{cname}', '{cat}', '{desc_med}','{shape}');")
    con.commit()
    con.close()
    return "추가가 완료되었습니다!"