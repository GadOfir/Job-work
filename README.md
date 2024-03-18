
"# Job-work" 

**git clone https://github.com/GadOfir/Job-work**

**pip install unittest requests selenium**

**edit test params  **

exmaple:

notepad shape.py

or

nano shape.py

**Edit params[] for test , per test doc**

def shape():
    params = [
        ('CLAW', 4, 'false', 'false', 'symmetrical', 9, 20, -1, 'Wireless false'),
        ('CLAW', 4, 'false', 'false', 'symmetrical', 9, 20, -1, 'Wireless false'),
        ('CLAW', 4, 'true', 'false', 'asymmetrical', 9, 20, -1, 'Wireless true'),
        ('CLAW', 4, 'true', 'false', 'both', 9, 20, -1, 'Wireless true'),
        # Add more test cases here as needed
    ]
.....rest of the code 


run with 

**python "test name"**


VM
pip install virtualenv

# Navigate to Your Project Directory
cd your_project_directory

# Create the Virtual Environment
python -m venv venv
# Or, for older Python versions:
# virtualenv venv

# Activate the Virtual Environment
# Windows
venv\Scripts\activate
# MacOS and Linux
