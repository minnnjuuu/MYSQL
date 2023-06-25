import mysql.connector
from flask import Flask,render_template,request,session
from flask_mysqldb import MySQL, MySQLdb
from my_constants import *

app = Flask(__name__) #flask를 사용한다고 선언

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods = ['POST']) #로그인 처리하는 대상
def login():
    if request.method == 'POST':  
        email_id = request.form['InputEmail']    
        passwd=request.form['InputPassword']
        
        cursor = mysql.connection.cursor()
        sql='select * from users email %s and password %s'
        val= (email_id, passwd)
        
        cursor.execute(sql,val)
        result = cursor.fetchall()
        cursor.close()
        
        if len(result)>1:
            return '회원정보에 중복된 값이 있습니다. 관리자에게 문의하세요'
        
        for item in result:
            print(item)
        
        
        #정상적으로 값이 나왔으면 session 정보에 값을 저장한다 ===> HTTP 통신의 로그인 처리
        session['Email_id'] = email_id
        session['Nick_Name'] = result[0][3] #첫 번째 레코드의 nick_name 필드 나옴
        session['ID_'] = result[0][0] #id필드
        
    return 'ok'

@app.route('/signup',methods = ['POST'])
def signup():
    if request.method != 'POST':
        return '잘못된 접근입니다!'
    email_id = request.form.get('InputEmail')
    passwd = request.form.get('InputPassword')
    passwdconf = request.form.get('InputPasswordConfirm')
    nick_name = request.form.get('InputNickName')
    
    if passwd != passwdconf :
        return '비밀번호 입력을 확인하세요'
    
    sql = 'insert into users(email,password,nick_name) values(%s, %s, %s)'
    val = (email_id, passwd, nick_name)
    
    cursor = mysql.connection.cursor()
    cursor.execute(sql,val)

    mysql.connection.commit()
    cursor.close()
    
    return 'ok'

@app.route('/signupform')
def showSignupform():
    return render_template('signup.html')








if __name__ == '__main__': #이 모듈을 실행하는 Entry Point
    app.secret_key = SECRET_KEY #웹 통신에 있어서 보안을 위해 키를 생성
    app.config['MYSQL_HOST']=HOST_IP #MYSQL 의 IP ADDRESS
    app.config['MYSQL_USER']= DB_USER #USER ID
    app.config['MYSQL_PASSWORD']=DB_PASSWORD #USER PASSWORD
    app.config['MYSQL_DB']= DB_SCHEMA #DATABASE SCHEMA
    mysql = MySQL(app)
    app.run(port = 8080,debug = True)   #WAS시작 (web application server)