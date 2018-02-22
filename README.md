# DataSets
                                               ** User Manual **
# DESCRIPTION:

This is a simple conception for data storage and data manipulation .
A database will be replaced by a folder , that contains .csv files to replace any relation in the database .
Csv files are easy to manipulate with pandas as they can be turned to data frames (tables , matixes , lists , strings ..) We talk about DATASETS .
  
  .___________________________________________________.
  |    DataBase --> Folder                            |
  |    DataBase Relation --> file.csv                 |             
  !___________________________________________________!
       
# REQUIREMENTS:

   .____________________________________________________.
   |    python 3 and above                              |
   |    pandas (python module)                          |
   |    bash                                            |
   !____________________________________________________!

# USAGE :
0) Extract this repository in your home repository .   
1) Execute the storage.sh file :

    bash storage.sh
    a help menu will appear , follow it :
    .___________________________________________________.     
    |  bash storage.sh 0 to exit                        |                   
    |  bash storage.sh 1 to create a new dataset        |
    |  bash storage.sh 2 to open an existing dataset    |
    ! __________________________________________________!    

any .csv file created by the Query Interpreter will be now saved under ~/DataSets/database_name .
    
The execution will open a command prompt : the Query interpreter , type ? for help when using it .

2) Use the Query Interpreter to create your dataset relations , and manipulate them

    .______________________________________________________________________.
    |    DECLARE ENTITY_NAME AS FIELD1, [[FIELD2], FIELD3]                 |
    |     ADD (FIELD1, [[FIELD2], FIELD3]) TO ENTITY_NAME                  |
    |     DELETE PRIMARY_KEY_VALUE FROM ENTITY_NAME                        |
    |     FIND [PRIMARY_KEY_VALUE | ALL] IN ENTITY_NAME                    |
    |     UPDATE PRIMARY_KEY_VALUE IN ENTITY_NAME SET FIELDNAME=NEW_VALUE  |
    |     QUIT to exit                                                     |
    !______________________________________________________________________!    


Notes:
      * upcase and downcase are accepted when using the Query interpreter .
      * please use '' instead of "" . e.g: ('ali','baba') and not ("ali","baba")
        this system doesn support "<thing>" now .
      * ('ali','baba') and (ali,baba) are the same .
      


