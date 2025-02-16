import os
import getpass
import sys
import platform

# Get current username and directory
MyUserName = getpass.getuser()
Here = os.getcwd()

# Ask for environment directory name
dirname = input("Directory name of environment: ")

env = os.path.join(Here, dirname)

# Get Python version
default_version = f"{sys.version_info.major}.{sys.version_info.minor}"

in_version = input(f"Enter desired Python version or press Enter to use system default ({default_version}): ")

if in_version == "":
	version = default_version
elif "3." in in_version:
	version = in_version
else:
	version = default_version

# Create the directory
os.makedirs(env, exist_ok=True)


# Provide activation instructions
if platform.system() == "Windows":
	os.system(f"python -m venv {env}")
	activate_cmd = os.path.join(env, "Scripts", "activate.bat")
else:
	os.system(f"python{version} -m venv {env}")
	activate_cmd = f"source {os.path.join(env, 'bin', 'activate')}"

print("Run the command below to start the new virtual environment:")
print(activate_cmd)
