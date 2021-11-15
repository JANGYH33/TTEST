# sqlite 사용


import sqlite3

def dbProcess(dbName):
    #print(dbName)
    
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        
        
        cursor.execute("drop table if exists jikwons")
        # 정수 integer 실수:real
        cursor.execute("create table jikwons(id integer primary key, name text)")
        
        # insert
        cursor.execute("insert into jikwons values(1, '홍길동')")
        
        
        #tdata = (2, '고길동') #tuple
        tdata = 2, '고길동' #tuple
        cursor.execute("insert into jikwons values(?,?)", tdata)
        
        ldata = [3, '공기밥'] #list      < set type은 불가능 순서가 없음)
        cursor.execute("insert into jikwons values(?,?)", ldata)
        
        dicdata = {'id':4, 'name':'고래밥'} #dict
        cursor.execute("insert into jikwons values(:id,:name)", dicdata)
        
        dicdata2 = {'obun':5, 'irum':'김밥'} #dict
        cursor.execute("insert into jikwons values(:obun,:irum)", dicdata2)
        
        conn.commit()
        
        # select
        print('출력 1')
        cursor.execute("select * from jikwons")
        for r in cursor:
            print(str(r[0]) + ' ' + r[1])
    
        print('출력 2----')
        #cursor.execute("select * from jikwons where id <= 2")
        #inputid = 2
        #cursor.execute("select * from jikwons where id <= %d"%inputid)
        inputname = '홍길동'
        cursor.execute("select * from jikwons where name = '%s'"%inputname)
        
        for r in cursor.fetchall():
            print(str(r[0]) + ' ' + r[1])
        
        print('출력 3 - SQL함수 ---------')
        
        cursor.execute("select count(*) from jikwons")
        # print("건수 : "+ str(cursor.fetchone())) # (5,)
        print("건수 : "+ str(cursor.fetchone()[0]))
        
    
    except Exception as e:
        print('err : ', e)
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()
    
    

if __name__ == '__main__':
    dbProcess('test.db')



    
    
    
    
    