0x0F. Load balancer
===================

#### In a nutshell…

*   **Auto QA review:** 0.0/4 mandatory & 0.0/2 optional
*   **Altogether:**  **0.0%**
    *   Mandatory: 0.0%
    *   Optional: 0.0%
    *   Calculation:  0.0% + (0.0% \* 0.0%)  == **0.0%**

### Concepts

_For this project, we expect you to look at these concepts:_

*   [Load balancer](/concepts/46)
*   [Web stack debugging](/concepts/68)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)

Background Context
------------------

You have been given 2 additional servers:

*   gc-\[STUDENT\_ID\]-web-02-XXXXXXXXXX
*   gc-\[STUDENT\_ID\]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is [redundancy](/rltoken/xnAaJdhmAxx7PoH3l6EwDg "redundancy") for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

Resources
---------

**Read or watch**:

*   [Introduction to load-balancing and HAproxy](/rltoken/B7f3oz8i3Xvvom_YQZzLnQ "Introduction to load-balancing and HAproxy")
*   [HTTP header](/rltoken/sZ9v3Vq2tgLwN_PWVQketw "HTTP header")
*   [Debian/Ubuntu HAProxy packages](/rltoken/2VRAgtKKR9g6Xfb0xzGiSg "Debian/Ubuntu HAProxy packages")

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted on Ubuntu 16.04 LTS
*   All your files should end with a new line
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   All your Bash script files must be executable
*   Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
*   The second line of all your Bash scripts should be a comment explaining what is the script doing

Your servers
------------

Name

Username

IP

State

26582-web-01

`ubuntu`

`54.236.28.84`

running

Actions Toggle Dropdown

*   [Soft reboot](/servers/7743/soft_reboot)
*   [Hard reboot](/servers/7743/hard_reboot)

*   [Ask a new server](/servers/7743/ask_new)

26582-web-02

`ubuntu`

`100.26.173.135`

running

Actions Toggle Dropdown

*   [Soft reboot](/servers/9029/soft_reboot)
*   [Hard reboot](/servers/9029/hard_reboot)

*   [Ask a new server](/servers/9029/ask_new)

26582-lb-01

Actions Toggle Dropdown

*   [Ask a server](/servers/ask_new_by_name?name=26582-lb-01&project_id=275)

Tasks
-----

### 0\. Double the number of webservers

mandatory

Score: 0.0% (Checks completed: 0.0%)

In this first task you need to configure `web-02` to be identical to `web-01`. Fortunately, you built a Bash script during your [web server project](/rltoken/-JluPVwfvXMOYMzNOqvgsQ "web server project"), and they’ll now come in handy to easily configure `web-02`. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:

*   Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
    *   The name of the custom HTTP header must be `X-Served-By`
    *   The value of the custom HTTP header must be the hostname of the server Nginx is running on
*   Write `0-custom_http_response_header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
    *   [Ignore](/rltoken/k3Bt6zu1On_-mDszxi0Z9w "Ignore") [SC2154](/rltoken/9KwKHb9H8OJqcSK0saRIOA "SC2154") for `shellcheck`

Example:

    sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
    X-Served-By: 03-web-01
    sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
    X-Served-By: 03-web-02
    sylvain@ubuntu$
    

If your server’s hostnames are not properly configured (`[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`.), follow this [tutorial](/rltoken/tLVI0yDpGJXb-Op5Lo0JtQ "tutorial").

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0F-load_balancer`
*   File: `0-custom_http_response_header`

Done?! Help

×

#### Students who are done with "0. Double the number of webservers"

Check your code

×

#### Correction of "0. Double the number of webservers"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 0\. Double the number of webservers

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 1\. Install your load balancer

mandatory

Score: 0.0% (Checks completed: 0.0%)

Install and configure HAproxy on your `lb-01` server.

Requirements:

*   Configure HAproxy so that it send traffic to `web-01` and `web-02`
*   Distribute requests using a roundrobin algorithm
*   Make sure that HAproxy can be managed via an init script
*   Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. If not, follow this [tutorial](/rltoken/YkfzgEa6xNHrQbkKmJN4zg "tutorial").
*   For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

Example:

    sylvain@ubuntu$ curl -Is 54.210.47.110
    HTTP/1.1 200 OK
    Server: nginx/1.4.6 (Ubuntu)
    Date: Mon, 27 Feb 2017 06:12:17 GMT
    Content-Type: text/html
    Content-Length: 30
    Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
    Connection: keep-alive
    ETag: "58abea7c-1e"
    X-Served-By: 03-web-01
    Accept-Ranges: bytes
    
    sylvain@ubuntu$ curl -Is 54.210.47.110
    HTTP/1.1 200 OK
    Server: nginx/1.4.6 (Ubuntu)
    Date: Mon, 27 Feb 2017 06:12:19 GMT
    Content-Type: text/html
    Content-Length: 612
    Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
    Connection: keep-alive
    ETag: "5315bd25-264"
    X-Served-By: 03-web-02
    Accept-Ranges: bytes
    
    sylvain@ubuntu$
    

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0F-load_balancer`
*   File: `1-install_load_balancer`

Done?! Help

×

#### Students who are done with "1. Install your load balancer"

Check your code

×

#### Correction of "1. Install your load balancer"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 1\. Install your load balancer

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Recommended Sandboxes

Copyright © 2022 ALX, All rights reserved.

×

#### Markdown Guide

#### Emphasis

\*\***bold**\*\*
\*_italics_\*
~strikethrough~~

#### Headers

\# Big header
## Medium header
### Small header
#### Tiny header

#### Lists

\* Generic list item
\* Generic list item
\* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item

#### Links

\[Text to display\](http://www.example.com)

#### Quotes

\> This is a quote.
> It can span multiple lines!

#### Images

CSS style available: `width, height, opacity`

!\[\](http://www.example.com/image.jpg)
!\[\](http://www.example.com/image.jpg | width: 200px)
!\[\](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)

#### Tables

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

_Or without aligning the columns..._

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |

#### Displaying code

\`var example = "hello!";\`

_Or spanning multiple lines..._

\`\`\`
var example = "hello!";
alert(example);
\`\`\`
