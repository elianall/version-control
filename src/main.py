from datetime import datetime
import os

now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(date_time)

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
docs_folder = os.path.join(repo_root, 'docs')
version_file_path = os.path.join(docs_folder, 'version.md')

with open(version_file_path, 'w') as file:
    file.write(f'# Version Control\n\nCurrent Date and Time: {date_time}')

print(f"Version written to {version_file_path}")

