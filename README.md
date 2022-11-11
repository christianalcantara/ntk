[![Django CI](https://github.com/christianalcantara/ntk/actions/workflows/django.yml/badge.svg)](https://github.com/christianalcantara/ntk/actions/workflows/django.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7c1a68a9935446c5b6e1e346a290f721)](https://www.codacy.com/gh/christianalcantara/ntk/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=christianalcantara/ntk&amp;utm_campaign=Badge_Grade)
[![Updates](https://pyup.io/repos/github/christianalcantara/ntk/shield.svg)](https://pyup.io/repos/github/christianalcantara/ntk/)
[![Python 3](https://pyup.io/repos/github/christianalcantara/ntk/python-3-shield.svg)](https://pyup.io/repos/github/christianalcantara/ntk/)
[![GitHub issues](https://img.shields.io/github/issues/christianalcantara/ntk)](https://github.com/christianalcantara/ntk/issues)
[![GitHub forks](https://img.shields.io/github/forks/christianalcantara/ntk)](https://github.com/christianalcantara/ntk/network)
[![GitHub stars](https://img.shields.io/github/stars/christianalcantara/ntk)](https://github.com/christianalcantara/ntk/stargazers)
[![GitHub license](https://img.shields.io/github/license/christianalcantara/ntk)](https://github.com/christianalcantara/ntk/blob/main/LICENSE)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/christianalcantara/ntk">
    <img src="docs/images/django-logo.png" alt="Logo" height="80">
  </a>
</p>
<h3 align="center">Django Backend</h3>

  <p align="center">
    Usage example of Django Rest Framework.
    <br />
    👽&nbsp;&nbsp;<a href="https://book-backend-rest.herokuapp.com/">View Demo</a>&nbsp;&nbsp;
    🐛&nbsp;&nbsp;<a href="https://github.com/christianalcantara/ntk/issues">Report Bug</a>&nbsp;&nbsp;
    ✳&nbsp;&nbsp;<a href="https://github.com/christianalcantara/ntk/issues">Request Feature</a>
  </p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#deploy-heroku">Deploy Heroku</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#authorization-token">Authorization Token</a></li>
        <li><a href="#get-customers">Get Customers</a></li>
        <li><a href="#get-books">Get Books</a></li>
      </ul>
    </li>
    <li>
       <a href="#roadmap">Roadmap</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://book-backend-rest.herokuapp.com/)

- Modern Python development with Python 3.8+
- Bleeding edge Django 3.0+
- PostgreSQL 11.6+
- Complete [Django Rest Framework](http://www.django-rest-framework.org/) integration
- Always current dependencies and security updates enforced by [pyup.io](https://pyup.io/).
- A slim but robust foundation -- just enough to maximize your productivity, nothing more.

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally. To get a local copy up and
running follow these simple example steps.

### Deploy Heroku

Use Heroku button to deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Installation

- Docker

  ```bash
  $ docker compose up
  ```

- Local

1. Clone the repo

   ```bash
   $ git clone https://github.com/christianalcantara/ntk.git

   # jump do path
   $ cd ntk
   ```

2. Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).
   ```bash
   $ virtualenv venv
   $ source venv/bin/activate
   $ pip install -r requirements.txt
   ```
3. Create dotenv file and define enviroment variables.

   ```bash
   $ touch .env
   $ echo "#Django
     DEBUG=True
     SECRET_KEY=YOUSECRETKEY
     DOMAIN=http://localhost:8000
     ALLOWED_HOSTS=*  > .env
   ```

4. Migrate the database and run

   ```shell
   $ python manage.py migrate

   # Optional: populate database
   $ python manage.py loaddata apps/users/fixtures/users.json apps/book/fixtures/books.json  apps/rent/fixtures/rents.json

   # run
   $ python manage.py runserver
   ```

5. Run tests
   ```shell
   $ pytest
   ```

<!-- USAGE -->

## Usage

Clique [here](https://book-backend-rest.herokuapp.com/) to view complete API endpoints.

### Authorization Token

- curl

```bash
curl -X POST "http://localhost:8000/api-token-auth/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"username\": \"admin@gmail.com\", \"password\": \"adminpassword\"}"```
```
- Response

```json
{
  "token": "71b3e6c42f5305a2ee4a1a2b46631662ab12a83b"
}
```

### Create Person

```bash
curl -X POST "http://localhost:8000/api/person/" -H "accept: application/json" -H "Content-Type: application/json" -H "Authorization: Token 047dd1377ef7695773a682f6d12172c6ec8ec6bc" -d "{ \"name\": \"Person Name\", \"email\": \"person_name@domain.com\"}"
```

<details>
<summary>Response</summary>

```json
{
  "id":2,
  "name":"Person Name",
  "email":"person_name@domain.com",
  "sale_opportunity":true,
  "cars":[],
  "created":"2022-11-11T01:23:58.762307Z",
  "modified":"2022-11-11T01:23:58.762327Z"
}
```

</details>

### Create `Car and link to `Person`

```bash
curl -X POST "http://localhost:8000/api/car/" -H "accept: application/json" -H "Content-Type: application/json" -H "Authorization: Token 047dd1377ef7695773a682f6d12172c6ec8ec6bc" -d "{ \"name\": \"Ferrari\", \"model\": \"convertible\", \"color\": \"yellow\", \"person\": 2}"
```

<details>
<summary>Response</summary>

```json
{
  "id": 1,
  "name": "Ferrari",
  "model": "convertible",
  "color": "yellow",
  "person": 2,
  "created": "2022-11-11T01:28:53.743637Z",
  "modified": "2022-11-11T01:28:53.743661Z"
}
```

</details>

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/christianalcantara/ntk/issues) for a list of proposed features (and
known issues).

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

<a href="mailto:christian.douglas.alcantara@gmail.com">Christian Douglas Alcântara </a>

Project Link: [https://github.com/christianalcantara/ntk](https://github.com/christianalcantara/ntk)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: docs/images/screenshot.png
