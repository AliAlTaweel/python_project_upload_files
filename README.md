
# Python Project - Upload files and images and save it to database.

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
[![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
[![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
[![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)

The project title is a level 1 heading (`<h1>Project Title</h1>` or `# Project Title`).

If your project has a name, then this is where it would go.

If your project does not have a name, you can use this space to explain the project. For example, code repositories of research papers usually have the paper title here.

You can also add your branding in a cover image. It makes the README unique and gets people's attention quickly.

Wait, I forgot something. You can use this README as a template from [this link](README-template.md).

I usually prefer the dimensions 1280×650. It has worked well for me so far. I can also reuse it as my social preview image for the repo.

Below the title, you will see some badges. These can be used to show the status of the project.

The badges used here were generated with [shields.io](https://shields.io/).

You can add a workflow status badge to indicate the status of your workflows in your README. This can used to answer questions like, `is the build working?` or `are the e2e tests passing?`.

The badges used here are explained below:

<!-- Add badges with link to Shields IO -->

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
: Shows the current release version.

![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
: Shows the last commit time. Good indication of the project activity.

![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
: Dynamic badge that shows the number of open issues in the project.

![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
: Similar dynamic badge, but for pull requests.

![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)
: Shows the open source license the project uses.


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
[http://localhost:8000/docs]            to display all roots available <br>
[http://localhost:8000/redoc]           same but newer <br>


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


