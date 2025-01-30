Ã
from datetime import datetime

now = datetime.now()
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date_time)

with open("version.md", "w") as f:
    f.write(formatted_date_time)
