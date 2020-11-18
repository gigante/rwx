# rwx

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

[![Build Status](https://travis-ci.org/gigante/rwx.svg?branch=master)](https://travis-ci.org/gigante/rwx) [![Maintainability](https://api.codeclimate.com/v1/badges/acb669fd65fa45e7ec02/maintainability)](https://codeclimate.com/github/gigante/rwx/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/acb669fd65fa45e7ec02/test_coverage)](https://codeclimate.com/github/gigante/rwx/test_coverage) [![Requirements Status](https://requires.io/github/gigante/rwx/requirements.svg?branch=master)](https://requires.io/github/gigante/rwx/requirements/?branch=master)

**rwx** is a tool to convert between two formats of Linux File Permission. It can be used via API or CLI.

## How to use

**Install**

```sh
$ git clone https://github.com/gigante/rwx && cd rwx
$ make install
```

**Local**

In one terminal, run server

```sh
$ make run
```

In another, request endpoint

```sh
$ ./rwx api 700

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

Or... cli

```sh
$ ./rwx cli 700

    numeric_mode: 700
    text_mode: rwx------
```

**Docker**

```sh
$ make deploy
$ ./rwx api 700
$ ./rwx api rwx------
```

## Tests and code coverage

```sh
$ make test
```
