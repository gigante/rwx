[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e80ea997c71045538b3c14321b280c30)](https://app.codacy.com/app/gigante/rwx?utm_source=github.com&utm_medium=referral&utm_content=gigante/rwx&utm_campaign=Badge_Grade_Dashboard)
# rwx [![Build Status](https://travis-ci.org/gigante/rwx.svg?branch=master)](https://travis-ci.org/gigante/rwx) [![Maintainability](https://api.codeclimate.com/v1/badges/acb669fd65fa45e7ec02/maintainability)](https://codeclimate.com/github/gigante/rwx/maintainability)

**rwx** is a tool to convert between two formats of Linux File Permission. It can be used via API or CLI.

<p align="center">
  <img src="https://raw.githubusercontent.com/gigante/rwx/master/img/example.jpg" alt="Api example" width="800" height="300">
</p>

## How to install

**Requirements**

[pipenv](https://docs.pipenv.org/)

```sh
$ pip install --user pipenv
```

**Install**

Clone this repo

```sh
$ git clone https://github.com/gigante/rwx
$ cd rwx
```

Install packages

```sh
$ make install
```

## How to use

Access the `venv`

```sh
$ pipenv shell
```

**Via api**

In one terminal, run server

```sh
$ make run
```

In other, request endpoint (curl or [httpie](https://httpie.org/))

```sh
$ http localhost:8000/chmod/700

    HTTP/1.1 200 OK
    Connection: close
    Content-Length: 47
    Content-Type: application/json
    Date: Sat, 12 Jan 2019 23:53:31 GMT
    Server: gunicorn/19.9.0

    {
        "numeric_mode": "700",
        "text_mode": "rwx------"
    }
```

**Via cli**

Example

```sh
$ python cli.py 700

    numeric_mode: 700
    text_mode: rwx------
```

## Tests

```sh
$ make test
```
