# Project: 0x11. Python - Network #1

## Resources

### Read or watch:-

- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
- [Requests package](https://pypi.org/project/requests/)

## Learning Objectives

### General

- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` #requestsiswaysimplerthanurllib
- How to make HTTP `GET` request
- How to make HTTP `POST`/`PUT`/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Tasks

0. [What's my status? #0](./0-hbtn_status.py) :

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- You must use the package `urllib`
- You are not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before `-`)
- You must use a `with` statement

```sh
ayomide@Kazzywiz:~/alx-higher_level_programming/0x11-python-network_1$ ./0-hbtn_status.py | cat -e
Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
ayomide@Kazzywiz:~/alx-higher_level_programming/0x11-python-network_1$ 
```

| Task                        | File                                   |
| --------------------------- | -------------------------------------- |
|  |
| 1. Response header value #0 | [1-hbtn_header.py](./1-hbtn_header.py) |
| 2. POST an email #0         | [2-post_email.py](./2-post_email.py)   |
| 3. Error code #0            | [3-error_code.py](./3-error_code.py)   |
| 4. What's my status? #1     | [4-hbtn_status.py](./4-hbtn_status.py) |
| 5. Response header value #1 | [5-hbtn_header.py](./5-hbtn_header.py) |
| 6. POST an email #1         | [6-post_email.py](./6-post_email.py)   |
| 7. Error code #1            | [7-error_code.py](./7-error_code.py)   |
| 8. Search API               | [8-json_api.py](./8-json_api.py)       |
| 9. My GitHub!               | [10-my_github.py](./10-my_github.py)   |
