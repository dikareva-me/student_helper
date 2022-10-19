# Mini lab 3
A repository for a web-app "Student helper" for Java course and API course.

## How this app works.

### Backend
Task model has following fields:
1. Title
2. Description
3. Subject
4. Is it complete?
5. User to which this task belongs
6. Email
7. When it was created
8. When it was updated
9. Deadline date

Tasks can be searched by title and subject and be ordered by completness, date of creation/updating/deadline. When posting a new task, a title and a deadline must be present. Other fields are optional, but if the email is present it must be valid.

### Frontend
On the frontend the list of tasks and a form for posting new task are shown. The rules of a new task are the same as those in the backend. Posting new task from frontend works now. The details of tasks are not present on the frontend yet. From the frontend you can change the status of a task and it will change in the database. 


## HTTPS requests made through Postman are listed below:
1. Posting a task. It must have a title and a valid (date type) deadline, other fields are optional. If an email is present it must be valid.
2. Getting all tasks present.
3. Getting task by name. Returns a task with required title from user.
4. Getting all uncomplete tasks and ordering it by ascending date of deadline.

https://www.getpostman.com/collections/487b8b1afb7de9d16a4d JSON link
https://www.postman.com/payload-pilot-68641284/workspace/my-workspace/collection/23839017-0a119f7c-1726-49b0-b3fc-f3661e1e0b01?ctx=documentation
link to a workspace

## How to install project
1. Create a virtual environment by typing  
python -m venv .venv  
in the terminal in project's folder.  
2. Activate virtual env by typing   
.\.venv\scripts\Activate.ps1  
3. Install django and django REST  
pip install django  
pip install djangorestframework  
pip install django-filter   
pip install django-cors-headers  
4. Run the server:  
cd helper  
python manage.py runserver  
5. Install nodejs if it's not present.  
6. Install vue cli  
npm install -g @vue/cli  
7. Create a vue project  
cd frontend  
vue create .  
Select Manually selected features and besides selected two select Router.  
Select 2.x version  
Yes   
ESLint + Prettier  
Lint on save  
In package.json  
8. Install additional packages  
npm i axios  
vue add vuetify  
9. Copy all code from https://github.com/dikareva-me/student_helper/blob/main/frontend/src/components/HelloWorld.vue and https://github.com/dikareva-me/student_helper/blob/main/frontend/src/App.vue and paste into your created HelloWorld.vue and App.vue respectfully (I don't know how else to create a vue project for an already existing vue app and couldnt find another solution) (You can also try to copy with replacing but I'm not sure how well it will work)
10. Run server (while running django server)  
npm run serve  
11.* If you have an error:   
9:13 error Component name “home“ should always be multi-word vue/multi-word-component-names  
The solution is here: https://programmerah.com/913-error-component-name-home-should-always-be-multi-word-vue-multi-word-component-names-49448/

