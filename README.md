# Student_helper
 A repository for a web-app "Student helper".
 It is a todo app made with Django REST framework and Vue.
 
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

Tasks can be searched by title and subject and be ordered by completness, date of creation/updating/deadline. When posting a new task, a title and a deadline must be present. Other fields are optional, but if the email is present it must be valid. There is authentication using Knox. There is an endpoint for changing password, email, username.

### Frontend
On the frontend the list of tasks and a form for posting new task are shown. The rules of a new task are the same as those in the backend. You can also visit a task's page and delete/edit task from there. There is a user profile page where you can see profile information such as email and username. 

