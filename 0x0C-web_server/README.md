0x0C. Web server
================

#### In a nutshell…

*   **Auto QA review:** 0.0/13 mandatory & 0.0/4 optional
*   **Altogether:**  **0.0%**
    *   Mandatory: 0.0%
    *   Optional: 0.0%
    *   Calculation:  0.0% + (0.0% \* 0.0%)  == **0.0%**

### Concepts

_For this project, we expect you to look at this concept:_

*   [What is a Child Process?](/concepts/110)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

Background Context
------------------

[![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/Screenshot+2017-07-06+19.24.05.png)](https://www.youtube.com/watch?v=AZg4uJkEa-4&feature=youtu.be&hd=1)

In this project, some of the tasks will be graded on 2 aspects:

1.  Is your `web-01` server configured according to requirements
2.  Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use `emacs` on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But my answer file would contain:

    sylvain@ubuntu cat 88-script_example
    #!/usr/bin/env bash
    # Configuring a server with specification XYZ
    echo hello world > /tmp/test
    sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
    sylvain@ubuntu
    

As you can tell, I am not using `emacs` to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](/rltoken/9I0WufjKdW3TZA2EVrGnlQ "SRE"), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the `root` user, you do not need to use the `sudo` command.

A good Software Engineer is a [lazy Software Engineer](/rltoken/sRY__axKNHhNW0SVmsUC_A "lazy Software Engineer"). ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

*   start a `Ubuntu 16.04` sandbox
*   run your script on it
*   see how it behaves

Resources
---------

**Read or watch**:

*   [How the web works](/rltoken/6TI3HiyFdwrbXWKVF24Gxw "How the web works")
*   [Nginx](/rltoken/vkVMGlaf39j2DWAQWzo6EA "Nginx")
*   [How to Configure Nginx](/rltoken/zKrpVxWuUHVdW4URAjdFbw "How to Configure Nginx")
*   [Child process concept page](/rltoken/Ar18u5sRis1fkvkVgzdcqg "Child process concept page")
*   [Root and sub domain](/rltoken/xi3peVqYl02PfpHHHlCtxQ "Root and sub domain")
*   [HTTP requests](/rltoken/sBrrP4EAmI3NoYjIgZrUhw "HTTP requests")
*   [HTTP redirection](/rltoken/Eaa4ZuKvye941hTkP8VlBQ "HTTP redirection")
*   [Not found HTTP response code](/rltoken/eJSp2QFTY6jqqNtz8OVDEw "Not found HTTP response code")
*   [Logs files on Linux](/rltoken/7WMNY5CWD-CBrxmQrdmfPg "Logs files on Linux")

**For reference:**

*   [RFC 7231 (HTTP/1.1)](/rltoken/BGa6RrS0dnM6EdBGS_ZDUw "RFC 7231 (HTTP/1.1)")
*   [RFC 7540 (HTTP/2)](/rltoken/IZ2fyYn1qNZ9RXXsg5vG1g "RFC 7540 (HTTP/2)")

**man or help**:

*   `scp`
*   `curl`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/EHyxcIwPtD2SzEGRKOnT3g "explain to anyone"), **without the help of Google**:

### General

*   What is the main role of a web server
*   What is a child process
*   Why web servers usually have a parent process and child processes
*   What are the main HTTP requests

### DNS

*   What DNS stands for
*   What is DNS main role

### DNS Record Types

*   `A`
*   `CNAME`
*   `TXT`
*   `MX`

### Copyright - Plagiarism

*   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
*   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
*   You are not allowed to publish any content of this project.
*   Any form of plagiarism is strictly forbidden and will result in removal from the program.

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
*   You can’t use `systemctl` for restarting a process

### Quiz questions

**Great!** You've completed the quiz successfully! Keep going!

#### Question #0

The main role of a web server is to

*   serve dynamic content
    
*   serve static content
    
*   host files
    

#### Question #1

A web server is

*   a physical machine
    
*   a software
    

#### Question #2

The main role of DNS is to

*   translate domain name into IP address
    
*   translate domain name into port
    
*   name websites
    

#### Question #3

What was one of the most important reason for which DNS was created

*   because humans are not good at remembering long sequences of numbers (IP address)
    
*   to connect the Internet
    
*   to index the web
    

#### Question #4

A HTTP GET request is to

*   request data
    
*   submit data
    
*   delete data
    

#### Question #5

A HTTP POST request is to

*   request data
    
*   submit data
    
*   delete data
    

#### Question #6

A DNS A record translates to

*   an IP
    
*   a domain
    

#### Question #7

A DNS CNAME record translates to

*   an IP
    
*   a domain
    

#### Question #8

What is TTL within the context of DNS

*   a time period when DNS query results are cached
    
*   a time period when DNS is not answering requests
    
*   a time period for DNS maintenance
    

#### Question #9

Why web servers usually use child processes?

*   That’s just a subjective technical choice from the developers who created the software
    
*   So that the web server can dynamically change the number of child process to accommodate the volume of requests to be processed
    
*   To prevent memory leak
    

Your servers
------------

Name

Username

IP

State

26582-web-01

`ubuntu`

`3.85.41.9`

running

Actions Toggle Dropdown

*   [Soft reboot](/servers/7178/soft_reboot)
*   [Hard reboot](/servers/7178/hard_reboot)

*   [Ask a new server](/servers/7178/ask_new)

Tasks
-----

### 0\. Transfer a file to your server

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that transfers a file from our client to a server:

Requirements:

*   Accepts 4 parameters
    1.  The path to the file to be transferred
    2.  The IP of the server we want to transfer the file to
    3.  The username `scp` connects with
    4.  The path to the SSH private key that `scp` uses
*   Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
*   `scp` must transfer the file to the user home directory `~/`
*   Strict host key checking must be disabled when using `scp`

Example:

    sylvain@ubuntu$ ./0-transfer_file
    Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
    sylvain@ubuntu$
    sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
    afile
    sylvain@ubuntu$ 
    sylvain@ubuntu$ touch some_page.html
    sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
    some_page.html                                     100%   12     0.1KB/s   00:00
    sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
    afile
    some_page.html
    sylvain@ubuntu$
    

In this example, I:

*   remotely execute the `ls ~/` command via `ssh` to see what `~/` contains
*   create a file named `some_page.html`
*   execute my `0-transfer_file` script
*   remotely execute the `ls ~/` command via `ssh` to see that the file `some_page.html` has been successfully transferred

That is one way of publishing your website pages to your server.

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0C-web_server`
*   File: `0-transfer_file`

Done?! Help

×

#### Students who are done with "0. Transfer a file to your server"

Check your code

×

#### Correction of "0. Transfer a file to your server"

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

#### 0\. Transfer a file to your server

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 1\. Install nginx web server

mandatory

Score: 0.0% (Checks completed: 0.0%)

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/01cab59e881e31842b8d47a0974e8d3b6f0f2001.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221020%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221020T211150Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f3c6acd75999ee04a3b21d4046279b63cbd2117356e2d0af92c73f4e86264dd2)

Readme:

*   [\-y on apt-get command](/rltoken/KJiFZ4yJyTGp_cv3DYQLaQ "-y on apt-get command")

Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

*   Install `nginx` on your `web-01`
*   server
*   Nginx should be listening on port 80
*   When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
*   As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
*   You can’t use `systemctl` for restarting `nginx`

Server terminal:

    root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
    root@sy-web-01$ 
    root@sy-web-01$ curl localhost
    Hello World!
    root@sy-web-01$ 
    

Local terminal:

    sylvain@ubuntu$ curl 34.198.248.145/
    Hello World!
    sylvain@ubuntu$ curl -sI 34.198.248.145/
    HTTP/1.1 200 OK
    Server: nginx/1.4.6 (Ubuntu)
    Date: Tue, 21 Feb 2017 23:43:22 GMT
    Content-Type: text/html
    Content-Length: 30
    Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
    Connection: keep-alive
    ETag: "58abea7c-1e"
    Accept-Ranges: bytes
    
    sylvain@ubuntu$
    

In this example `34.198.248.145` is the IP of my `web-01` server. If you want to query the Nginx that is locally installed on your server, you can use `curl 127.0.0.1`.

If things are not going as expected, make sure to check out Nginx logs, they can be found in `/var/log/`.

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0C-web_server`
*   File: `1-install_nginx_web_server`

Done?! Help

×

#### Students who are done with "1. Install nginx web server"

Check your code

×

#### Correction of "1. Install nginx web server"

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

Ask for a new correction : in progress... : an error occurred QA Review

×

#### 1\. Install nginx web server

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 2\. Setup a domain name

mandatory

Score: 0.0% (Checks completed: 0.0%)

[.TECH Domains](/rltoken/Hcb-pfK8UiDBfwsDJPyZZw ".TECH Domains") is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your [tools space](/rltoken/CprZO4m1rUm5C6ZgvROpgg "tools space"). Feel free to drop a thank you tweet for [.TECH Domains](/rltoken/y3_YCbJ5bGKgPYqP0LyVBA ".TECH Domains").

Provide the domain name in your answer file.

Requirement:

*   provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
*   configure your DNS records with an A entry so that your root domain points to your `web-01` IP address **Warning: the propagation of your records can take time (~1-2 hours)**
*   go to [your profile](/rltoken/hH2hPj0jwETzZL-AvFJkwQ "your profile") and enter your domain in the `Project website url` field

Example:

    sylvain@ubuntu$ cat 2-setup_a_domain_name
    myschool.tech
    sylvain@ubuntu$
    sylvain@ubuntu$ dig myschool.tech
    
    ; <<>> DiG 9.10.6 <<>> myschool.tech
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
    
    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;myschool.tech.     IN  A
    
    ;; ANSWER SECTION:
    myschool.tech.  7199    IN  A   184.72.193.201
    
    ;; Query time: 65 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8)
    ;; WHEN: Fri Aug 02 09:44:36 PDT 2019
    ;; MSG SIZE  rcvd: 65
    
    sylvain@ubuntu$
    

When your domain name is setup, please verify the Registrar here: [https://whois.whoisxmlapi.com/](/rltoken/UVCb6LeF54ktxR6lZSUyTQ "https://whois.whoisxmlapi.com/") and you must see in the JSON response: `"registrarName": "Dotserve Inc"`

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0C-web_server`
*   File: `2-setup_a_domain_name`

Done?! Help

×

#### Students who are done with "2. Setup a domain name"

Check your code

×

#### Correction of "2. Setup a domain name"

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

Ask for a new correction : in progress... : an error occurred QA Review

×

#### 2\. Setup a domain name

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 3\. Redirection

mandatory

Score: 0.0% (Checks completed: 0.0%)

Readme:

*   [Replace a line with multiple lines with sed](/rltoken/RRP9hX3MlQdABaKZD-Y_cA "Replace a line with multiple lines with sed")

Configure your Nginx server so that `/redirect_me` is redirecting to another page.

Requirements:

*   The redirection must be a “301 Moved Permanently”
*   You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
*   Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

Example:

    sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
    HTTP/1.1 301 Moved Permanently
    Server: nginx/1.4.6 (Ubuntu)
    Date: Tue, 21 Feb 2017 21:36:04 GMT
    Content-Type: text/html
    Content-Length: 193
    Connection: keep-alive
    Location: https://www.youtube.com/watch?v=QH2-TGUlwu4
    
    sylvain@ubuntu$
    

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0C-web_server`
*   File: `3-redirection`

Done?! Help

×

#### Students who are done with "3. Redirection"

Check your code

×

#### Correction of "3. Redirection"

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

#### 3\. Redirection

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 4\. Not found page 404

mandatory

Score: 0.0% (Checks completed: 0.0%)

Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

Requirements:

*   The page must return an HTTP 404 error code
*   The page must contain the string `Ceci n'est pas une page`
*   Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task

Example:

    sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
    HTTP/1.1 404 Not Found
    Server: nginx/1.4.6 (Ubuntu)
    Date: Tue, 21 Feb 2017 21:46:43 GMT
    Content-Type: text/html
    Content-Length: 26
    Connection: keep-alive
    ETag: "58acb50e-1a"
    
    sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
    Ceci n'est pas une page
    
    sylvain@ubuntu$
    

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0C-web_server`
*   File: `4-not_found_page_404`

Done?! Help

×

#### Students who are done with "4. Not found page 404"

Check your code

×

#### Correction of "4. Not found page 404"

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

#### 4\. Not found page 404

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

(function(i,s,o,g,r,a,m){i\['GoogleAnalyticsObject'\]=r;i\[r\]=i\[r\]||function(){ (i\[r\].q=i\[r\].q||\[\]).push(arguments)},i\[r\].l=1\*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)\[0\];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) })(window,document,'script','//www.google-analytics.com/analytics.js','ga'); ga('create', 'UA-67152800-9', 'auto', { userId: '26582' } ); ga('send', 'pageview'); $(document).ready(function() { ga(function(tracker) { var clientId = tracker.get('clientId'); $('.ga-client-id').val(clientId); }); });
