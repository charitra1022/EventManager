# EventManager

A simple Django based event management application

The features of this web application are as follows:
1. User login/signup
2. Admin can approve a user as organizer on request
3. When approved, the organizer can create events
4. Other users, say Attendees, can register for events

## How to run this application

1. Clone the github repo, (or download the zip and extract).
2. Make sure the latest version of Python is installed onto your system.
3. Open terminal in the project directory.
4. Run `pip install -r requirements.txt` to install packages.
5. Run `python manage.py runserver` to run the deployment server.
6. Open `http://127.0.0.1:8000/` into a web browser. (Port can be different if `8000` is busy.)

## How to access the ADMIN panel

1. Follow the steps above.
2. Open `http://127.0.0.1:8000/admin` into a web browser. (Port can be different if `8000` is busy.)
3. Enter `admin` as username and `admin` as password to login.
