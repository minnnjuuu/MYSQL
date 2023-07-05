import mysql.connector
# python app <---- mysql.connector ----> MYSQL Database
# 기본적으로 python compiler 포함되어 있지 않다.
# pip : python 외부 library installer
# mysql.connector 외부 api를 pip로 설치

from flask import Flask,render_template,request,session
from flask import redirect as rd
# python에는 기본 web server engine(core s/w) 포함
# django, flask : 매우 많이 사용되는 python WAS api, Framework
# WAS : Web Application Server
# Web Server : Apache, IIS, NGINX...
# request : 클라이언트의 요청을 처리

from flask_mysqldb import MySQL, MySQLdb
# mysql.connector 를 flasl 에서 사용하기 편하도록 만들어진
#flask전용 mysql.connector의 Wrapper(랩퍼)

from my_constants import *

#__name__ :현재 컴파일될 모듈명
# flask 객체를 생성
app = Flask(__name__) #flask를 사용한다고 선언

#라우팅 경로를 지정
#홈페이지가 호출되었을때 실행하는 프로세스

#'127.0.0.1/login'  라우팅경로
@app.route('/')

def index():
    if 'Email_id' in session and 'ID_' in session:
        #로그인 처리가 되었다면
        #todo 데이터베이스에서 가져온다
        todos = getTodos()
        return render_template('index.html',login=True, Nick_Name=session.get('Nick_Name'),todos=todos)
    
    return render_template('index.html',login=False) #template폴더 및에 index.html 호출

def getTodos():
    sql = 'select * from todos where user_id = %s'
    val = (session.get('ID_'),)
    
    cursor = mysql.connection.cursor()
    cursor.execute(sql,val)
    result = cursor.fetchall()
    cursor.close()
    return result


@app.route('/signupform')
def showSignupform():
    return render_template('signup.html')

# '127.0.0.1/login' : 라우트 경로
@app.route('/login',methods = ['POST']) #로그인 처리하는 대상
def login():
    if request.method != 'POST': 
        return " 잘못된 경로로 호출되었습니다" 
    email_id = request.form.get('InputEmail')   #index.html의 form 태그안에 있는 input태그의 이름(name)  
    passwd=request.form.get('InputPassword')    #index.html의 form 태그안에 있는 input태그의 이름(name)
        
    cursor = mysql.connection.cursor()
    sql='select * from users where email = %s and password = %s'
    val= (email_id, passwd)
        
    cursor.execute(sql,val)
    result = cursor.fetchall() #select 한 결과를(튜플, 리스트 형태로) 가져온다
    cursor.close()
        
    if len(result)>1 or len(result)==0:
        return '로그인이되지 않았습니다.'
      
    #debug용    
    #for item in result:
    #   print(item)
        
        
    #정상적으로 값이 나왔으면 session 정보에 값을 저장한다 ===> HTTP 통신의 로그인 처리
    session['Email_id'] = email_id
    session['Nick_Name'] = result[0][3] #첫 번째 레코드의 nick_name 필드 나옴
    session['ID_'] = result[0][0] #id필드
        
    return rd('/')


#/signup 라우트에 POST방식으로 request 했을때 실행되는 프로세스(sign up())
@app.route('/signup',methods = ['POST'])
def signup():
    if request.method != 'POST':
        return '잘못된 접근입니다!'
    # signup.html 에서 폼(form)필드에 입력한 각각의 값들을 가져와서 변수에 저장
    email_id = request.form.get('InputEmail')
    passwd = request.form.get('InputPassword')
    passwdconf = request.form.get('InputPasswordConfirm')
    nick_name = request.form.get('InputNickname')
    
    #비밀번호를 서로 맞지않게 입력했다면 오류를 출력하고 종료
    if passwd != passwdconf :
        return '비밀번호 입력을 확인하세요'
    
    sql = 'insert into users(email,password,nick_name) values(%s, %s, %s)'
    val = (email_id, passwd, nick_name) #튜플의 형태로 값을 만듬
    
    cursor = mysql.connection.cursor()
    cursor.execute(sql,val) #SQL문을 실행시킨다
    mysql.connection.commit() #select문 외에 명령어들을 실행시켰을때 DB에 적용
    cursor.close() #사용한 핸들러는 반드시 닫아준다
    
    #홈페이지로 리다이렉트 시킴
    return rd('/')

@app.route('/insert_todo' , methods = ['POST'])
def insertTodo():
    #todo를 입력하는 처리
    if 'Email_id' in session and 'ID_' in session:
        todo = request.form.get("InputTodo") #index.html의 form에서 받은 할일
        sql = 'insert into todos(todo_name,user_id) values(%s,%s)'
        val = (todo, session.get('ID_')) #user_id는 로그인 시에 session에 저장해둔 걸 가져옴
        
        cursor = mysql.connection.cursor()
        cursor.execute(sql,val)
        mysql.connection.commit()
        cursor.close()
        
    return rd('/')

#로그아웃 처리
@app.route('/logout')
def logout():
    # session 저장한 값 (키 : 밸류)들을 전부 삭제
    session.pop('Email_id')
    session.pop('Nick_Name')
    session.pop('ID_')
    return rd('/')

@app.route('/update_done',methods = ['POST'])
def updateDone():
    if request.method!='POST':
        return "잘못된 경로로 호출하였습니다."
    done = request.json['done']
    user_id = request.json['user_id']
    todo_id = request.json['todo_id']
    
    #sql = 'update 테이블명 set 컬럼명 = 값 where 조건'
    sql = 'update todos set done = %s where id = %s and user_id = %s'
    val = (done, todo_id, user_id)
    cursor = mysql.connection.cursor()
    cursor.execute(sql, val)
    mysql.connection.commit()
    cursor.close()
    
    return rd('/')
    

#Entry Point
if __name__ == '__main__': #이 모듈을 실행하는 Entry Point
    app.secret_key = SECRET_KEY #웹 통신에 있어서 보안을 위해 키를 생성
    app.config['MYSQL_HOST']=HOST_IP #MYSQL 의 IP ADDRESS
    app.config['MYSQL_USER']= DB_USER #USER ID
    app.config['MYSQL_PASSWORD']=DB_PASSWORD #USER PASSWORD
    app.config['MYSQL_DB']= DB_SCHEMA #DATABASE SCHEMA
    mysql = MySQL(app)
    app.run(port = 8080,debug = True)   #WAS시작 (web application server)



