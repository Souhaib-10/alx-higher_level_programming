# 0x10. Python -Network #0

##  Project Summary

This project covers fundamental networking concepts using **Python** and **Bash**, focusing on HTTP, `curl`, request methods, headers, and response analysis. It includes scripting with curl, understanding HTTP status codes, cookies, and crafting efficient Bash scripts.

---

##  Learning Objectives

By the end of this project, you should be able to explain:

- What a URL is and how to read one
- The structure of HTTP URLs and request methods
- What HTTP headers, bodies, and status codes are
- How cookies work in HTTP
- How to use `curl` in different ways (GET, POST, DELETE)
- What happens when you type a URL in your browser
- How to extract information from HTTP responses

---

## Project Structure

├── 0-body_size.sh # Bash script to get size of HTTP response body
├── 1-body.sh # GET request, displays body for 200 status only
├── 2-delete.sh # Sends a DELETE request
├── 3-methods.sh # Lists allowed HTTP methods
├── 4-header.sh # Sends custom header in GET request
├── 5-post_params.sh # Sends POST request with email and subject
├── 6-peak.py # Python function to find a peak
├── 6-peak.txt # Time complexity of the peak-finding algorithm
└── README.md # This file

---

##  Requirements

- All scripts tested on Ubuntu 20.04 LTS
- Bash scripts must have exactly 3 lines and be executable
- Python scripts use Python 3.8.5 and `pycodestyle` for style checks
- No external libraries allowed
- Files must end with a newline
- Python code must be well-documented (module, class, function)

---

##  Commands Used

- `curl -s` – silent mode
- `curl -X METHOD` – custom HTTP method
- `curl -H` – custom headers
- `curl -d` – send POST data
- `wc -c` – count bytes
- `chmod +x` – make files executable

---

##  Sample Usage

```bash
$ ./0-body_size.sh 0.0.0.0:5000
10

$ ./1-body.sh 0.0.0.0:5000/route_1
Route 2

$ ./2-delete.sh 0.0.0.0:5000/route_3
I'm a DELETE request

$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT

$ ./4-header.sh 0.0.0.0:5000/route_5
Hello School!

$ ./5-post_params.sh 0.0.0.0:5000/route_6
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
```
## Resources

- [HTTP - MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [HTTP Cookies - MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [Curl Manual](https://curl.se/docs/)
