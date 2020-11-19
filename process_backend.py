import subprocess
import re 

subprocess.call("php connect.PHP")

def getValues(dataArray, filename, typew, location):
    arr = dataArray
    i =0
    while(dataArray[].length != 0)
        for x in dataArray
            j =dataArray[i][x]
            if(idCheck(j)== true)
                cursor.execute("INSERT INTO PHYSICAL_ATTRIBUTES VALUES (%s, %s, %s, %s)", (filename, typew, location, 1))
            elif(emailCheck(j) == true)
                cursor.execute("INSERT INTO PHYSICAL_ATTRIBUTES VALUES (%s, %s, %s, %s)", (filename, typew, location, 3))

def idCheck(value):
    if(int(value) == 13):
        return True
    else:
        return False

def emailCheck(value):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
    if(re.search(regex,email))
        return True
    else 
        return False

        
