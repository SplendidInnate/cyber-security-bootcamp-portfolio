
#!/bin/bash

# Changes permissions of all objects in a folder to -rw-r--r-- (644)

echo "Enter the folder path:"
read folder

if [-d "$folder" ]; then
	chmod 644 "$folder"/*
	echo "Permissions changed to -rw-r--r-- for all objects in '$folder' "
else
	echo "Error: '$folder' is not a valid directory."
fi
