"""
 키보드로 직원번호와 이름을 각각 입력 받아 해당 직원이 있으면 로그인이 되었다 가정하고
 직원번호 직원명 부서명 부서전화 직급 성별을 출력하고
 해당 직원이 없으면 로그인 실패라는 에러 메세지 출력

select jikwon_no, jikwon_name, buser_name from jikwon 
inner join buser on jikwon.buser_num = buser.buser_no
where jikwon_no <=5;
"""



import MySQLdb

config = {

    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True

}


def test():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
    
        jikwon_no = input('직원번호 : ')
        jikwon_name = input('직원이름 : ')
        
        sql = """
        
        select jikwon_no,jikwon_name, buser_name , buser_tel ,  jikwon_jik,  jikwon_gen 
        from jikwon inner join buser on jikwon.buser_num = buser.buser_no
        where jikwon_no = {} and jikwon_name = '{}'
        """.format(jikwon_no, str(jikwon_name))
        #and jikwon_name = {}
        cursor.execute(sql)
        datas = cursor.fetchall()
        
        if len(datas) > 0:
            print('로그인이 됬네')
            print(datas)
            
        else:
            print('아무도 없지')
    
    
    
    except Exception as e:
        print('오류는 : ' , e) 
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close() 
    
if __name__ == '__main__':
    test()