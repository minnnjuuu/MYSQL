import mysql.connector


db = mysql.connector.connect(
    host = 'localhost', #database ip/localhost = 127.0.0.1 = 내 ip
    user = 'root',      #mysql 접속하는 user id -> root권한 접속은 최상위 권한
    password='020411',  #mysql 접속하는 위 사용자의 비밀번호
    database = 'scores' #mysql 에서 만든 하나의 스키마(데이터베이스)
)

#print(db)
#데이터베이스 핸들러 -> 커서
cursor = db.cursor()
cursor.execute('show databases') #데이터 베이스 SQL문 실행
#execute 한 결과를 리스트의 형태로 가져옴

for db_obj in cursor:
    print(db_obj)
try:
    sql = 'insert into students(name, grade, class) values(%s,%s,%s)'
    val = ('강호동', 4, 3) #튜플
    cursor.execute(sql,val)
    db.commit() # commit을 안 해주면 insert가 무효가 됨
except:
    print("입력중에 오류가 발생했습니다.")
cursor.execute('select * from select_all_from_scores') 

liresult = cursor.fetchall() #select한 결과를 전부 가져와라
for item in liresult:
    print(item)
