# Python OS Library Sample 🚀

A simple Python example showing how to use the built-in `os` library.  
Learn to interact with your operating system in just a few lines of code!

## What You Can Do

- Check your current working directory 🗂️  
- Create and list folders/files 📁  
- Rename or delete files/folders ✏️❌  
- Access environment variables 🌐  
- Identify files vs folders 🔍  

## Quick Example

```python
import os

print("Current Directory:", os.getcwd())

folder_name = "example_folder"
os.makedirs(folder_name, exist_ok=True)
print(f"Folder '{folder_name}' ready!")

print("Contents:", os.listdir(os.getcwd()))

print(f"'{folder_name}' is a directory" if os.path.isdir(folder_name) else "It's a file")