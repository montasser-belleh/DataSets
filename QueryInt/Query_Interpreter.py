#NOTE : USE PYTHON3
import pandas as pd

def extract_primary_key(string):
    key=''
    for i in range(len(string)):
        if string[i] not in("(","'",")"):
            key+=string[i]
    return(key.split(sep=",")[0])


def find(name,file_csv):
    data=pd.read_csv(file_csv,sep=',',header=0)
    data_table=data.as_matrix()
    i=0
    for i in range(data_table.shape[0]):
        if data_table[i][0]==name:
            return(i)
    else:
        i+=1
    return(-1)

def size(string):
    return(len(string.split(sep=",")))

def header_size(file_csv):
    data=pd.read_csv(file_csv,header=0)
    return(data.as_matrix().shape[1])

def extract_data(string):
    key=''
    for i in range(len(string)):
        if string[i] not in("(","'",")","\n"):
            key+=string[i]
    return(key)

def extract_fieldname(string):
    return(string.split(sep="=")[1])

def extract_field_to_modify(string):
    return(string.split(sep="=")[0])

def extract_index(string,field):
    L=string.split(sep=",")
    for i in range(len(L)):
        if L[i]==field:
            return(i)
    
def extract_modification(string):
    return(string.split(sep="=")[1])
    
    
    
    

while 1:
    request=input("Query Interpreter>> ")
    request_words=request.split()
    
    if request_words[0]=="?":
        print("._________________________________________________________________.")
        print("| Howdy ! help will be given to those who need it                 |")
        print("| Usage :                                                         |")
        print("|                                                                 |")
        print("| DECLARE ENTITY_NAME AS FIELD1, [[FIELD2], FIELD3]               |")
        print("| ADD (FIELD1, [[FIELD2], FIELD3]) TO ENTITY_NAME                 |")
        print("| DELETE PRIMARY_KEY_VALUE FROM ENTITY_NAME                       |")
        print("| FIND [PRIMARY_KEY_VALUE | ALL] IN ENTITY_NAME                   |")
        print("| UPDATE PRIMARY_KEY_VALUE IN ENTITY_NAME SET FIELDNAME=NEW_VALUE |")
        print("| QUIT to exit                                                    |")
        print("!_________________________________________________________________!")
        
    elif request_words[0]=="QUIT" or request_words[0]=="quit":
        break
    elif request_words[0]=="DECLARE" or request_words[0]=="declare":
        if request_words[2]=="AS" or request_words[2]=="as":
            if len(request_words)>=3:
                file_name=request_words[1]+".csv"
                f=open(file_name,"a")
                f.write(request_words[3]+'\n')
                f.close()
                print("Query Interpreter>> OK")
            else:
                print("Query Interpreter>> ERROR: at least one field should be specified")

    elif request_words[0]=="ADD" or request_words[0]=="add":
        if request_words[2]=="TO" or request_words[2]=="to":
            file_name=request_words[3]+".csv"
            to_add=extract_data(request_words[1])
            if size(to_add)!=header_size(file_name):
                print("Query Interpreter>> ERROR input size doesn't match the number of columns")
            else:
                primary_key=extract_primary_key(request_words[1])
                if find(primary_key,file_name)==-1:
                    f=open(file_name,"a")
                    f.write(to_add+'\n')
                    f.close()
                    print("Query Interpreter>> OK")
                else:
                    print("Query Interpreter>> ERROR: this record already exists")
                    
    elif request_words[0]=="DELETE" or request_words[0]=="delete":
        if request_words[2]=="FROM" or request_words[2]=="from":
            file_name=request_words[3]+".csv"
            target=extract_data(request_words[1])
            if find(target,file_name)!=-1:
                f=open(file_name,"r")
                file_lines=f.readlines()
                f.close()
                found=find(target,file_name)+1
                f=open(file_name,"w")
                for i in range(len(file_lines)):
                    if i!=found:
                        f.write(file_lines[i])
                f.close()
                print("Query Interpreter>> OK")
            else:
                print("Query Interpreter>> ERROR: this record doesn't exist")
                
    elif request_words[0]=="UPDATE" or request_words[0]=="update":
        if request_words[2]=="IN" or request_words[2]=="in":
            if request_words[4]!="SET" or request_words[4]!="set":
                file_name=request_words[3]+".csv"
                found=find(request_words[1],file_name)
                if found!=-1:
                    #TODO modify the needed line within the proposed normes
                    f=open(file_name,"r")
                    file_lines=f.readlines()
                    f.close()
                    index=extract_index(extract_data(file_lines[0]),extract_field_to_modify(request_words[5]))
                    print(index)
                    print(file_lines[found].split(sep=",")[index])
                    file_lines[found].split(sep=",")[index]=extract_modification(request_words[5])
                    print(file_lines[found].split(sep=",")[index])
                    f=open(file_name,"w")
                    for i in range(len(file_lines)):
                        f.write(file_lines[i])
                    f.close()
                    print("Query Interpreter>> OK")
                else:
                    print("Query Interpreter>> ERROR: this record doesn't exist")
                    
    elif request_words[0]=="FIND" or request_words[0]=="find":
        if request_words[2]=="IN" or request_words[2]=="in":
            file_name=request_words[3]+".csv"
            target=extract_data(request_words[1])
            if find(target,file_name)!=-1:
                    f=open(file_name,"r")
                    file_lines=f.readlines()
                    f.close()
                    found=find(target,file_name)+1
                    print("the record was found")
                    print(file_lines[found])
            elif request_words[1]=="ALL" or request_words[1]=="all":
                    f=open(file_name,"r")
                    file_lines=f.readlines()
                    f.close()
                    for i in range(1,len(file_lines)):
                        print(file_lines[i])
            else:
                    print("Query Interpreter>> ERROR: this record doesn't exist")

                    
    else:
        print("Query Interpreter>> ERROR: wrong command")
                

        
        
