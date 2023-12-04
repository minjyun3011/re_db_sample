import os

print(os.environ.get("PWD"))
print(os.environ.get("SECRET"))

from dotenv import load_dotenv
load_dotenv()

print(os.environ.get("SECRET")) 
