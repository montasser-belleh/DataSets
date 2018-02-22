# DataSets
                                               ** User Manual **
# DESCRIPTION:

This is a simple conception for data storage and data manipulation .
A database will be replaced by a folder , that contains .csv files to replace any relation in the database .
Csv files are easy to manipulate with pandas (python module) as they can be turned to data frames (tables , matixes , lists , strings ..) We talk about DATASETS .
    
    * DataBase --> Folder
    * DataBase Relation --> file.csv         
       
# REQUIREMENTS:

    * python 3 and above
    * pandas (python3 module)
    * bash
    
install requirements :

    $ sudo apt-get install python3
    $ sudo apt-get install python3-pandas

# USAGE :
0) Extract this repository in your home repository & open a terminal in it .
1) Execute the storage.sh file :

       $ bash storage.sh
    
    a help menu will appear , follow it :
         
       $ bash storage.sh 0 to exit                  
       $ bash storage.sh 1 to create a new dataset
       $ bash storage.sh 2 to open an existing dataset
       

any .csv file created by the Query Interpreter will be now saved under ~/DataSets/database_name .
    
The execution will open a command prompt : the Query interpreter , type 

       Query Interpreter >>?
        
 for help when using it .


2) Use the Query Interpreter to create your dataset relations , and manipulate them

    
       Query Interpreter >>  DECLARE ENTITY_NAME AS FIELD1, [[FIELD2], FIELD3]                 
       Query Interpreter >>  Query Interpreter >> ADD (FIELD1, [[FIELD2], FIELD3]) TO ENTITY_NAME                  
       Query Interpreter >>  DELETE PRIMARY_KEY_VALUE FROM ENTITY_NAME                        
       Query Interpreter >>  FIND [PRIMARY_KEY_VALUE | ALL] IN ENTITY_NAME                   
       Query Interpreter >>  UPDATE PRIMARY_KEY_VALUE IN ENTITY_NAME SET FIELDNAME=NEW_VALUE 
       Query Interpreter >>  QUIT to exit                 
       


Notes:

   * upcase and downcase are accepted when using the Query interpreter .
   * please use '<thing>' instead of "<thing>" . e.g: ('ali','baba') and not ("ali","baba")
        this system doesn't support "<thing>" yet .
   * ('ali','baba') and (ali,baba) are the same .
