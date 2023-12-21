CooC Headband Inc.
Pre-order website
By Brian Lin and Allen Zhang
Video link: https://youtu.be/tSbeJmkpjo0
 
Project description:
This project is a pre-order website for a student's (my) start-up. The website introduces the product (an EEG headband that measures the effectiveness of meditation) and allows customers to pre-order the product by entering their emails.
 
This website has 2 major functions:
1. A nicely built website with all the information that a customer will need to understand the product, the company, and the underlying logic behind the product. For that, we have 3 different web pages with images and formatted using a combination of HTML, CSS, and  Javascript.
 
2. A pre-order form that allows customers to pre-order by giving us the person's name, email, address, and phone number. Once that happens, we will store this information in a database and likely send the user a confirmation email. We will also store the quantity of the pre-order and the time of ordering.
 
 
How to operate:
1. Unzip file then open directory in VS Code
2. CD workspace to CS50_final_project
3. Make sure Flask is installed
 
To run the website, execute “flask run” in the terminal and click on the provided link

To see or modify the database execute the following :
sqlite3 cooc.db

To see all user data execute the following (Note that information has to be inputted to the pre-order form in order to view the current information on users):
SELECT * FROM users;

To see all pre-orders execute the following:
SELECT * FROM preorders;
 
 

Citation:
We used finance as a reference to structure our website (how the pages should structure, how to route each pages, etc) but the content and formating is very different.
 
We also used bootstrap and web3school for someof our CCS style. In particular, we used some free templates from web3school.com for our styling but with modification and completely different content.
 
Bootstrap spec: https://getbootstrap.com/docs/5.0/getting-started/introduction/
Web3school reference: https://www.w3schools.com/w3css/w3css_references.asp
images from google.com
NOT FOR COMMERCIAL PURPOSES FOR NOW
 
 
 
 
 

