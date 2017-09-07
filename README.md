# look-up
Custom unix command that returns the contact information found in a yaml file


#### **Table of Contents**
1. Description
2. Setup
3. Usage
4. Limitations

## **Description**
---

This is a custom unix command that returns the contact information about a user based on the specified username.

This is achieved by using a .sh script that calls a Python script that reads the yaml script and prints out the results

### **Setup**
---

1. Clone this repository into your user directory
2. Update parse.py with the direction parse.py is located in
3. Copy whois to /usr/bin/
4. run $chmod +x whois

Now you can run the command whois. See usage for details

## **Usage**
---

$whois <username>

See limitations

## **Limitations**
---

Contact information can only be found if the username exist and the contact information exists as a comment. 
Contact information cannot be displayed if it is not in the yaml file.
The yaml file must be up to date with the yaml file used by the puppet module.

