#db1.py
import sqlite3

#파일에 저장
con = sqlite3.connect("c:\\work\\test.db")

#일단은 메모리에 저장
#con = sqlite3.connect(":memory:")
#구문 실행은 커서객체에서
cur = con.cursor()

#테이블 구조 생성( ANSI SQL 92, 99에서 표준)
cur.execute("CREATE TABLE IF NOT EXISTS PhoneBook " + 
            "(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, PhoneNum TEXT);")
#1건 입력
cur.execute("INSERT INTO PhoneBook (name, phoneNum) VALUES ('홍길동', '010-111');")
#cur.execute("INSERT INTO PhoneBook (name, phoneNum) VALUES ('배철수', '010-222');")
#cur.execute("INSERT INTO PhoneBook (name, phoneNum) VALUES ('김여희', '010-333');")

#입력 파라미터 처리
name = "전우치"
phoneNumber = "010-222"
cur.execute("INSERT INTO PhoneBook (name, phoneNum) VALUES (?, ?);", (name, phoneNumber))

#다중의 레코드 입력
datalist = (("박문수", "010-123"), ("김길동","010-456"))
cur.executemany("INSERT INTO PhoneBook (name, phoneNum) VALUES (?, ?);", datalist)

#결과 확인
cur.execute("SELECT * FROM PhoneBook;")

#for row in cur:
#    print(row)

print("---------fetchone()--------\n")
print(cur.fetchone())
print("---------fetchmany()--------\n")
print(cur.fetchmany(2))
print("---------fetchall()--------\n")
cur.execute("SELECT * FROM PhoneBook;")
print(cur.fetchall())


#연결닫기
con.close()

