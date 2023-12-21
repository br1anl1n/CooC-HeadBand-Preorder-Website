design document
 
This is a pretty standard full-stack website with front and backend.
 
The website have 6 HTML files:
- layout.html
- preorder.html
- support.html
- home.html
- thankyou.html
- product.html
 
Every file is an extension from layout.html's "main" tag.
 
We chose this design because the layout contains the navigation bar that allows users to navigate through the different pages on the website. We use href tags and route functions in the created app.py file to direct users to different parts of the website.
 
For most of the html designs, we used some form of css templates from either web3 school or bootstrap, which we specified in the readme document. We chose to do this because it will result in a more organized and professional-looking design instead of writing our own CSS forms. Of course, we used a few customized CSS designs in our style sheet as well, since we can't find a good substitute from license free sites.
 
The back-end of the design is mostly focused on the pre-order form. We chose to create 2 sqlite tables within the database (cooc.db). The first one is "users" where we record the potential customers and their information. The second one is the "preorders" table where we record the transactions of the customers. The two forms are linked with a primary key of "user_id" which tells us who preordered how many products.
 
The reason why we have two tables is because it allows us to keep track of the user’s information separately and thus allows us to have a unique list of customers instead of having to separate them out later on. In addition, a lot of the delivery services require a unique order_id which we included in our "preorder" table. This allows us to tell the delivery services their delivery details (quantity, time, etc) without leaking the personal information of the user.
 
In the "preorder" function in app.py, we inserted the user information into the database with db.execute commands. Additionally, we used javascript to display the completed form every time the user submits/pre-order’s the product which leads them to the thankyou.html file, simply thanking the user for their order.  
 
 
 
 
 
 
 

