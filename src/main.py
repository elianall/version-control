from datetime import datetime

now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(date_time)

docs_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'docs')
version_file_path = os.path.join(docs_folder, 'version.md')

with open(version_file_path, 'w') as file:
    file.write(f'# Version Control\n\nCurrent Date and Time: {date_time}')

print(f"Version written to {version_file_path}")

