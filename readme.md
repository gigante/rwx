# rwx

**rwx** is a tool to convert between two formats of Linux File Permission. It can be used via API or CLI.

<p align="center">
  <img src="./img/example.png" alt="Api example" width="800" height="300">
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