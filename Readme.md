Selenium Automation: Multi-Window Handling and File Download
This project demonstrates advanced web automation using Python Selenium. The tasks involve handling multiple windows, frames, and file downloads from two websites: CoWIN and Ministry of Labour & Employment.

Prerequisites
Python: Install the latest version from here.
Google Chrome Browser: Download Chrome.
Install Required Libraries:
bash
Copy code
pip install selenium webdriver-manager requests
Tasks and Solutions
Task 1: CoWIN Website
Steps Automated:
Click on the "Create", "FAQ", and "Partners" links to open new windows.
Retrieve and display the Window/Frame IDs in the console.
Close the new windows and return to the home page.
Code Explanation:
Window Handling:

driver.window_handles retrieves the list of window IDs.
driver.switch_to.window() switches between windows.
Console Output:

Prints all active window IDs and confirms switching back to the main window.
Window Management:

Closes specific windows using driver.close().
Task 2: Labour Ministry Website
Steps Automated:
Documents:

Navigate to the "Documents" menu.
Download the "Monthly Progress Report."
Media:

Navigate to "Media > Photo Gallery".
Download the first 10 images and save them to a folder created dynamically using Python.
Code Explanation:
Navigation:

Use Selenium's find_element and Actions for menu and sub-menu interactions.
File Download:

Image URLs are fetched using Selenium's get_attribute('src').
Files are downloaded using Python's requests library.
Dynamic Folder Creation:

Use Python's os module to create a directory named photo_gallery.
How to Run the Script
Clone or download the repository.
Update the script paths if necessary.
Execute the script:
bash
Copy code
python script_name.py
Example Outputs
CoWIN Task:
Console Output:

less
Copy code
Main Window ID: CDwindow-ABC12345
Opened Window IDs: ['CDwindow-XYZ12345', 'CDwindow-PQR67890']
Labour Ministry Task:
Monthly Progress Report is saved in the project directory.
A folder named photo_gallery contains the first 10 images from the Photo Gallery.
Folder Structure
Copy code
project/
├── code
    |__fqa.py
    |__labour.py
    |__media.py
├── photo_gallery/
│   ├── photo_1.jpg
│   ├── photo_2.jpg
│   ├── ...
References
Selenium Documentation
Python os Module
Requests Library
Author
This project is created for learning Selenium automation and handling multiple tasks on live websites. Feel free to contribute and enhance the functionality!