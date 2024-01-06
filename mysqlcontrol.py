import mysql.connector
import time
from discordkeysmain import *


mydb = mysql.connector.connect(
  host=host,
  user= user,
  password=password,
  database=database
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE IF NOT EXISTS storage(username VARCHAR[255],left VARCHAR[5], right VARCHAR[5],total_time INT,title VARCHAR[255],description TEXT,Post_Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
#mycursor.execute("USE userdata")
#mycursor.execute("DROP TABLE users")
#mycursor.execute("CREATE TABLE IF NOT EXISTS users(username VARCHAR(255), left_time VARCHAR(5), right_time VARCHAR(5), total_time VARCHAR(5),Title VARCHAR(255), Description TEXT, Push_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
#mycursor.execute("INSERT INTO users(username, left_time, right_time, total_time, Title, Description) VALUES('john', '12:05','13:05','01:00','work', 'fuck my life bitchs');")
#mycursor.execute("SELECT * FROM users WHERE username='john' AND month(Push_time)=1 AND year(Push_time)=2024 AND day(Push_time)=1;")
#mycursor.execute("SELECT username, total_time, Title FROM users;")
def queryout(outputlist=None):
    if outputlist==None:
        outputlist = []
    for x in mycursor:
        outputlist.append(x)
    return outputlist

def callinguserdata(username, input_str):
    tokens = input_str.split(" ")
    queryout = f"SELECT * FROM users WHERE username='{username}'"
    opts = ["year","month","day"]
    tmp = ""
    if len(tokens)== 4 and tokens[0] == ("month" or "year") and tokens[2]== ("month" or "day"):
        tmp_block = f" AND {tokens[0]}(Push_time)={tokens[1]}"
        tmp+=tmp_block
        tmp_block = f" AND {tokens[2]}(Push_time)={tokens[3]}"
        tmp+=tmp_block
        queryout+=tmp
        return
    elif len(tokens)==3:
        for x in range(len(tokens)):
            tmp_block = f" AND {opts[x]}(Push_time)={tokens[x]}"
            queryout+=tmp_block
            tmp+=tmp_block
            return
    elif len(tokens)==2:
        tmp_block = f" AND {tokens[0]}(Push_time)={tokens[1]}"
        queryout+=tmp_block
        return
    else:
        return
def userdatainsertion(username:str, left_time:str, right_time:str, total_time:int,insertionobj:str, title=None, description=None,Push_time=None):
    if Push_time==None:
        time_object = time.localtime()
        Push_time = time.strftime("%Y-%m-%d ", time_object)+insertionobj
    build = "INSERT INTO users(username, left_time, right_time, total_time, Title, Description, Push_time)"
    builts =  f" VALUES('{username}','{left_time}','{right_time}',{total_time},'{title}','{description}','{Push_time}')"
    mycursor.execute(build+builts+";")
def buildtable(input_str):
    tokens = input_str.split(" ")
    if tokens[0]=="all":
        mycursor.execute(queryout+" GROUP BY username;")
        return
    queryout = "SELECT username, Title, SUM(total_time) FROM users"
    opts = ["year","month","day"]
    if len(tokens)<4:
        queryout+=" WHERE"
        for x in range(len(tokens)):
            if x>0:
                queryout+=" AND"
            tmp_block = f" {opts[x]}(Push_time)={tokens[x]}"
            queryout+=tmp_block
    else:
        return
    
    mycursor.execute(queryout+" GROUP BY username;")
    return    
def pop_insertion(username,input_str, unread):
    tokens = input_str.split(" ")
    queryout = f"SELECT * FROM users WHERE username='{username}'"
    opts = ["year","month","day"]
    if len(tokens)==3:
        for x in range(len(tokens)):
            tmp_block = f" AND {opts[x]}(Push_time)={tokens[x]}"
            queryout+=tmp_block
    else:
        return
    mycursor.execute(queryout+";")
    #query out for forloop on a 2d list ->tuple
    # single pass insertion sort kind of deal
    """if unread==True:
      pass
      #write to node flag
    else:
      mycursor.execute(f"DELETE FROM users WHERE username='{username}"+tmp+";")
    mycursor.execute(queryout+";")"""
    return
def mysql_to_csv():
    pass
word = "2020-01-01 23:59:58"
big_word = "2020-01-01 24:00:00"
def timestampcalout(word:str):
    tokens = word[10::].split(":")
    sum = (int(tokens[0])*3600)+(int(tokens[1])*60)+int(tokens[2])
    return sum
def timestampcalin(word:int):
    if word<60: #360 3600:
        return f"00:00:{seconds}"
    elif word<3600:
        minutes = word//60
        seconds = (word%3600)%60
        return f"00:{minutes}:{seconds}"
    else:
        hours = word//3600
        minutes = (word%3600)//60
        seconds = (word%3600)%60
        return f"{hours}:{minutes}:{seconds}"
def centerinsertion(left:str, right:str):
    left_most = timestampcalout(left)
    total_distance = timestampcalout(right)-timestampcalout(left)
    print(total_distance//2)
    return timestampcalin(left_most+(total_distance//2))

#mycursor.execute("CREATE TABLE usersnames(users VARCHAR(5),fuck INT)")
#ycursor.execute(f"INSERT INTO fuck(users, fuck)VALUES('john', {weight}); ")
#mydb.commit()
#print(mycursor.execute("SELECT * FROM fuck WHERE users='john';"))
#mycursor.execute("CREATE TABLE people(fuk)")#, left1, right1);") #,Total_Time,Title,Description,Upload_Time);")
#print(mydb) 
#mycursor.execute("SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE' AND table_schema='userdata';")
if __name__ == "__main__":
   #print(callinguserdata("john","2024,1,1"))
    print(centerinsertion(word,big_word))
    #print(timestampcalout(word))
    #word = timestampcalout(word)
    #print(timestampcalin(word))
    pass
#for x in mycursor:
#    print(x)
#    print(type(x))
#mydb.commit()
#    for n in mycursor:
#        print(n)