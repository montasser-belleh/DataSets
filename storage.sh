#!/usr/bin bash
if [ ! -d "DataSets" ]; then
  mkdir ~/DataSets
fi
cd data
if [ ! $1 ]; then
  echo "
      the storage engine needs at least one argument , none is given
      bash storage.sh 0 to exit                    
      bash storage.sh 1 to create a new dataset    
      bash storage.sh 2 to open an existing dataset"
  exit
fi
if [ $1 -eq 0 ]; then
  exit
fi
if [ $1 -eq 1 ]; then
  echo "dataset name :"
  read dataset_name
  mkdir $dataset_name
  cd ~/DataSets/$dataset_name
  echo ">> dataset $dataset_name created under ~/DataSets/$dataset_name , opening up the Query Interpreter .. "
  python ~/QueryInt/Query_Interpreter.py
fi
if [ $1 -eq 2 ]; then
  echo "dataset to open:"
  read dataset_name
  cd ~/DataSets/$dataset_name
  echo ">> dataset $dataset_name opened , opening up the Query Interpreter .. "
  python ~/QueryInt/Query_Interpreter.py
fi
