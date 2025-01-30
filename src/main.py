From datetime import datetime

# Get the current date and time in the format YYYY-MM-DD HH:MM:ss
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md
with open('version.md', 'w') as file:
    file.write(f"Version created on: {current_time}\n")
