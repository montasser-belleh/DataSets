                                                        ** USER MANUAL **

This is a simple conception for data storage and data manipulation .
A database will be replaced by a folder , that contains .csv files to replace any relation in the database .
Csv files are easy to manipulate with pandas as they can be turned to data frames (tables , matixes , lists , strings ..) : we talk about datasets .

Requirements:

         python3
         pandas module (pip install pandas)

Execute the storage.sh file :

         bash storage.sh
         a help menu will appear , follow it
         any .csv file created by the Query Interpreter will be now saved under system/data/database_name .
    
The execution will open a command prompt : the Query interpreter , type ? for help when using it .

         DECLARE ENTITY_NAME AS FIELD1, [[FIELD2], FIELD3]  // declare ENTITY_NAME as FIELD1, [[FIELD2], FIELD3]
         ADD (FIELD1, [[FIELD2], FIELD3]) TO ENTITY_NAME    // add (FIELD1, [[FIELD2], FIELD3]) to ENTITY_NAME
         DELETE PRIMARY_KEY_VALUE FROM ENTITY_NAME          // delete PRIMARY_KEY_VALUE from ENTITY_NAME    
         FIND [PRIMARY_KEY_VALUE | ALL] IN ENTITY_NAME      // find [PRIMARY_KEY_VALUE | all] in ENTITY_NAME 
         UPDATE PRIMARY_KEY_VALUE IN ENTITY_NAME SET FIELDNAME=NEW_VALUE // update PRIMARY_KEY_VALUE in ENTITY_NAME set FIELDNAME=NEW_VALUE 
         
         (note that both upcase and downcase are accepted.)

Note: please use '' instead of "" . e.g: ('ali','baba') , this system doesn support " <thing> " now ..
      


