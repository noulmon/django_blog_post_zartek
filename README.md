# Django BlogPost: Zartek

### Introduction:
_**Django BlogPost**_ is a 'Content Posting'  application 
where the _admin user_ can add **Posts** that includes- 
'**Title**, **Description**, **Images** and **Tags**'.
The _users_ can view the list of all posts.
All _users_ (except _admin user_) can **_like/unlike_** the posts.

The _admin user_ has the privilege to view the list of all users who have liked a particular **post**.

### Follow the steps to _run the application_:

1. Install all the required required packaged(python modules):

    ```pip install -r requirements.txt```

2. Migrate all models to the database(Assuming that you've already setup the Database- PostgreSQL preferred)
 
    ```python manage.py migrate```
    
3. When the migrations are successfully completed, we can run the server:

    ```python manage.py runserver```
    
    If the steps are followed correctly, you're server will be up and running.

 4. To log into admin panel, we have to create a superuser:
 
    ```python manage.py createsuperuser```
    
    User can log into the **Admin Panel** using the following url(assuming that you are on local server):
    
        http://127.0.0.1:8000/admin/
    
    On logging into the admin panel, admin users can:
    ```1. Add users```
    ```2. Add posts```
    
    Don't forget to add **_AUTH TOKENS_** for each users you create, in the **TOKENS** section.

## API Documentation:
   - API Documentation are in: ``\docs\api_docs\blog_post_api_doc.json``
   - Browsable Documentation: `https://documenter.getpostman.com/view/6826654/Szf55ACK` 

### API Endpoints:
(**_`Note: Please add the 'user token' as the 'Authorization Header' for all APIs`_**)
1. ```/post/all/``` list of all posts based on the user likes.

2. ```/post/like/<int:pk>/``` like/unlike a post.

3. ```post/liked_users/<int:pk>/``` list of all users who liked a post(restricted to admin users).
