
# Python Project - Upload files and images and save it to database.

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
[![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
[![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
[![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)

## 🌟 Project Overview

This project is a **production-grade web application backend** built with **FastAPI**. It demonstrates essential, real-world concepts for creating modern APIs, including:

* **File Handling:** Securely uploading and managing images and videos.
* **Database Integration:** Connecting to and managing data in a persistent store (using `aiosqlite`).
* **User Authentication:** Implementing robust user login and authorization using JWT tokens via `fastapi-users[sqlalchemy]`.
* **External Service Integration:** Utilizing **ImageKit** for powerful image and video API capabilities, including an AI-Powered Digital Asset Management (DAM) system.

This repository serves as the code base for a comprehensive tutorial on building a full-featured FastAPI application.

> **Note:** This project is designed for developers with basic Python and API knowledge who want to move beyond simple tutorials to build production-ready applications.


# Table of Contents

This is a table of contents for your project. It helps the reader navigate through the README quickly.
- [Project Title](#project-title)
- [Quick Start Demo](#quick-start-demo)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contribute](#contribute)
- [License](#license)


# Installation
[(Back to top)](#table-of-contents)

> **Note**: For longer README files, I usually add a "Back to top" buttton as shown above. It makes it easy to navigate.

When start new python project :

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh

```
Then restart the terminal, and check uv version

```shell
uv —version
```
init vu

```shell
uv init
```
install dependencies need it in the project:

```shell
uv add fastapi 
uv add python-dotenv
uv add fastapi-users[sqlalchemy]
uv add imagekitio
uv add uvicorn[standard]
uv add aiosqlite

```
Package,Purpose
fastapi,"High-performance, modern Python web framework."
uvicorn[standard],ASGI web server to run the FastAPI application.
aiosqlite,Asynchronous SQLite driver for database interaction.
fastapi-users[sqlalchemy],"Handles robust user registration, login, and JWT-based authentication."
imagekitio,"Integrates ImageKit for image/video upload, management, and optimization."
python-dotenv,Loads configuration from the .env file.

uv add fastapi            to add fastapi dependence.<br>
uv add python-dotenv<br>
uv add fastapi-users[sqlalchemy] 		to handle authentication and authorization in project.<br>
uv add imagekitio                                   to handle images and videos. <br>
uv add uvicorn[standard]                uvicorn is a web server in python that allows us to serve out fast api application.<br>
uv add aiosqlite    to interact with database.<br>

To start running the python:
```shell
uv run ./main.py
```
[http://localhost:8000/docs]            to display all available roots  <br>
[http://localhost:8000/redoc]           same but newer <br>

Environment Variables
Create a file named .env in the project root to store your secrets and configuration. You will need keys for ImageKit and a secret for your JWTs.

# Example .env file content
# ImageKit Credentials (Get these from your ImageKit dashboard)
IMAGEKIT_PUBLIC_KEY="your_public_key"
IMAGEKIT_PRIVATE_KEY="your_private_key"
IMAGEKIT_URL_ENDPOINT="your_url_endpoint"

# Secret Key for Authentication (Generate a long, random string)
SECRET_KEY="a_very_secret_and_long_jwt_secret"

# Database path (for aiosqlite, will be created if it doesn't exist)
DATABASE_URL="sqlite+aiosqlite:///./sql_app.db"
# Usage
[(Back to top)](#table-of-contents)

Next, you have to explain how to use your project. You can create subsections under here to explain more clearly.


# Development
[(Back to top)](#table-of-contents)

You have people who want to use your project and then you have people who want contribute to your project.

This is where you provide instructions for the latter.

Add instructions on how to set up a development environment, clone, and build the project.

You can use the code snippets here as well:

```shell
command to clone your project
command to build your project
command to run your project in development mode
```


# Contribute
[(Back to top)](#table-of-contents)

You can use this section to highlight how people can contribute to your project.

You can add information on how they can open issues or how they can sponsor the project.


# License
[(Back to top)](#table-of-contents)

You can also mention what license the project uses. I usually add it like this:

[MIT license](./LICENSE)


