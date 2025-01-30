
import sys√
from datetime import datetime

now = datetime.now()
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date_time)

with open('version.md', 'w') as file:
    file.write(f"Version created on: {formatted_date_time}\n")

print ("Current date and time written to version.md:" , formatted_date_time)
