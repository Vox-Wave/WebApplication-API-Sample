# WebApplication

Welcome to the WebApplication repository! This repository serves as the backend for our Django application VoxWave. Follow the instructions below to set up and run the backend server locally.

## Clone the Repository

To get started, clone this repository to your local machine using the following command:

```bash
git clone [https://github.com/your-username/WebApplication.git](https://github.com/Vox-Wave/WebApplication.git)
```

Replace `your-username` with your GitHub username if you are using HTTPS, or use the appropriate URL if you are using SSH.

## Create and Activate Virtual Environment

Once you have cloned the repository, navigate to the project directory:

```bash
cd WebApplication
```

Next, create a virtual environment named `venv`:

```bash
python -m venv venv
```

Activate the virtual environment:

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS and Linux:**

```bash
source venv/bin/activate
```

## Install Required Libraries

With your virtual environment activated, install the required libraries from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
Once you have installed the libraries, navigate to the project directory:

```bash
cd VoxWave
```
## Perform Migrations

If necessary, perform database migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run the Development Server

Finally, start the development server to run the backend:

```bash
python manage.py runserver
```

The server should now be running locally at `http://localhost:8000/`.

You can access the admin panel by navigating to `http://localhost:8000/admin/` and login with the appropriate credentials if your project includes Django's admin functionality.

You are now ready to work on the WebApplication backend for VoxWave. Happy coding!
