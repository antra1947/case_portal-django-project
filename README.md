# CasePortal - Django Case Management Portal



## Live at:  
case-portal-django-project.onrender.com/


## Project Overview
CasePortal is a Django-based web application designed to streamline the management of various types of cases. It provides features like digital scheduling of hearings, document management, and notifications, improving efficiency and transparency in case management.

Traditional case management relies on manual processes which lead to delays, inefficiencies, and scattered information. This project automates these processes in a simple, user-friendly portal.

## Features
- User authentication (login/logout)
- Add, view, and manage cases
- Schedule hearings for cases
- Upload and manage case-related documents
- Dashboard with total, ongoing, and closed cases
- Notifications for new hearings
- Secure access: Only authenticated users can manage their own cases


## Technologies Used
- Backend: Python, Django  
- Frontend: HTML, CSS, Bootstrap  
- Database: SQLite (default Django DB)  
- Version Control: Git & GitHub  

## Installation

1. Clone the repository:
```bash
git clone https://github.com/antra1947/case_portal-django-project.git
cd case_portal-django-project
````

2. Create a virtual environment:

```bash
python -m venv env
```

3. Activate the environment:

* Windows:

```bash
env\Scripts\activate
```

* Mac/Linux:

```bash
source env/bin/activate
```

4. Install required packages:

```bash
pip install -r requirements.txt
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Create a superuser (optional for admin access):

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Open your browser and go to:

```
http://127.0.0.1:8000/
or
http://127.0.0.1:8001/
```

## Usage

1. Log in with your credentials.
2. Add a new case via Add Case.
3. View all cases in Cases.
4. Click on a case to see details, add hearings, or upload documents.
5. Notifications will show scheduled hearings in the portal.

## Project Structure

```
case_portal/
├─ core/                 
│  ├─ templates/core/    
│  ├─ forms.py
│  ├─ models.py
│  ├─ views.py
│  └─ urls.py
├─ case_portal/          
├─ manage.py
├─ db.sqlite3            
├─ requirements.txt
└─ media/                
```

## Notes

* Media files (documents) are stored locally in media/.
* Notifications are displayed inside the portal, not as browser pop-ups.

## Author

Antra Gupta
GitHub: [antra1947](https://github.com/antra1947)

## License

This project is free to use for learning and academic purposes.

```
```
