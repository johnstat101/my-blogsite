# [BlogSite Preview Website](https://myblogs-webapp.herokuapp.com/)

## By John Kimani

## Description

My-blogsite is an online Python-Flask application that allows users to create, edit and delete blogs. Users who are sign-in can comment on other Blogs. The application also allows users to subscribe to email alerts when a new blog has been posted by other users

User Story:

* A user would like to view the blog posts on the site
* A user would like to comment on blog posts
* A user would like to view the most recent posts
* A user would like to get an email alert when a new post is made by joining a subscription
* A user would like to see random quotes on the site
* A writer would like to sign in to the blog and create a blog from the application
* A writer would like to delete comments, update or delete blogs

### Prerequisites

You need the following to start working on the project on your local computer:

* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python version 3.9
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Getting Started

* Clone this repository to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual amchine.
* Create start.sh file and in it write the following lines:
```
 export MAIL_USERNAME='<Your-Mail UserName>'
 export MAIL_PASSWORD='<Your-Mail Password>'
 python3.9 manage.py server
```
* Run ```chmod +x start.sh``` follwoed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.
* Alternatively the application can be accessed by visiting https://myblogs-webapp.herokuapp.com/

## Technologies Used

* Python v3.9
* Boostrap
* Flask

## License

MIT License

Copyright (c) 2022 John Kimani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. Copyright (c) 2018 Peter Polle

