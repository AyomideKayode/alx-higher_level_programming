# Project: 0x10. Python - Network #0

## Resources

### Read or watch:

- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

## Learning Objectives

### General

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Tasks

0. [cURL body size](./0-body_size.sh) :

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

- The size must be displayed in bytes
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```sh
root@8beaefef1df8:/alx-higher_level_programming/0x10-python-network_0# ls
0-body_size.sh  README.md
root@8beaefef1df8:/alx-higher_level_programming/0x10-python-network_0# ./0-body_size.sh 0.0.0.0:5000
Content-Length: 10
root@8beaefef1df8:/alx-higher_level_programming/0x10-python-network_0#
```

1. [cURL to the end](./1-body.sh) :

Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response

- Display only body of a `200` status code response
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

| Task                    | File                                                 |
| ----------------------- | ---------------------------------------------------- |
|                    |
|                              |
| 2. cURL Method          | [2-delete.sh](./2-delete.sh)                         |
| 3. cURL only methods    | [3-methods.sh](./3-methods.sh)                       |
| 4. cURL headers         | [4-header.sh](./4-header.sh)                         |
| 5. cURL POST parameters | [5-post_params.sh](./5-post_params.sh)               |
| 6. Find a peak          | [6-peak.py](./6-peak.py), [6-peak.txt](./6-peak.txt) |
