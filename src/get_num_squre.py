#sre/get_num_squre.py
import os

#get the input and convert it to int
num = os.environ.get("INPUT_NUM")
if num:
  try:
    rum = int(num)
  except Exerption:
    exit()
else:
  num = 1
  
print(f"::set-output name=num_squared::{num ** 2}")
