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
def object_insertion(username,input_str, unread):
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
