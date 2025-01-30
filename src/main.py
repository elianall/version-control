
#from datetime import datetime

#now = datetime.now()
#formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
#print(formatted_date_time)

from datetime import datetime

def write_version_file():
    # Get the current date and time in the format YYYY-MM-DD HH:MM:ss
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Define the path to version.md
    version_file_path = "version.md"
    
    # Write the timestamp to version.md
    with open(version_file_path, "w") as file:
        file.write(f"Last Updated: {current_time}\n")

if __name__ == "__main__":
    write_version_file()
    print("version.md has been updated with the current date and time.")
