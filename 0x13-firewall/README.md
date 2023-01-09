0x13. Firewall
==============

### Concepts

_For this project, we expect you to look at this concept:_

*   [Web stack debugging](/concepts/68)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

Background Context
------------------

### Your servers without a firewall…

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

Resources
---------

**Read or watch**:

*   [What is a firewall](/rltoken/vjB4LyHRdtEImzZcuD89ZQ "What is a firewall")

More Info
---------

As explained in the **web stack debugging guide** concept page, `telnet` is a very good tool to check if sockets are open with `telnet IP PORT`. For example, if you want to check if port 22 is open on `web-02`:

    sylvain@ubuntu$ telnet web-02.holberton.online 22
    Trying 54.89.38.100...
    Connected to web-02.holberton.online.
    Escape character is '^]'.
    SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8
    
    Protocol mismatch.
    Connection closed by foreign host.
    sylvain@ubuntu$
    

We can see for this example that the connection is successful: `Connected to web-02.holberton.online.`

Now let’s try connecting to port 2222:

    sylvain@ubuntu$ telnet web-02.holberton.online 2222
    Trying 54.89.38.100...
    ^C
    sylvain@ubuntu$
    

We can see that the connection never succeeds, so after some time I just use `ctrl+c` to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on `web-01`, please perform the test from outside of the school network, like from your `web-02` server. If you SSH into your `web-02` server, the traffic will be originating from `web-02` and not from the school’s network, bypassing the firewall.

Warning!
--------

**Containers on demand cannot be used for this project (Docker container limitation)**

**Be very careful with firewall rules! For instance, if you ever deny port `22/TCP` and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.**

### Quiz questions

**Great!** You've completed the quiz successfully! Keep going!

#### Question #0

What is a firewall?

*   A software security system
    
*   A hardware or software security system
    
*   A hardware security system
    

#### Question #1

What is the main function of a firewall?

*   To filter outgoing traffic
    
*   To filter incoming and outgoing TCP traffic
    
*   To filter incoming and outgoing network traffic
    

#### Question #2

What is a firewall?

*   A software security system
    
*   A hardware or software security system
    
*   A hardware security system
    

#### Question #3

What is the main function of a firewall?

*   To filter outgoing traffic
    
*   To filter incoming and outgoing TCP traffic
    
*   To filter incoming and outgoing network traffic
    

#### Question #4

What are the 2 types of firewall?

*   Network and host-based firewall
    
*   Incoming and outgoing firewall
    
*   Soft and hard firewall
    

#### Question #5

What are the 2 types of firewall:

*   Network and host-based firewall
    
*   Incoming and outgoing firewall
    
*   Soft and hard firewall
    

Your servers
------------

Name

Username

IP

State

26582-web-01

`ubuntu`

`54.85.93.141`

running

Actions Toggle Dropdown

*   [Soft reboot](/servers/9669/soft_reboot)
*   [Hard reboot](/servers/9669/hard_reboot)

*   [Ask a new server](/servers/9669/ask_new)

26582-web-02

`ubuntu`

`34.201.165.179`

running

Actions Toggle Dropdown

*   [Soft reboot](/servers/10704/soft_reboot)
*   [Hard reboot](/servers/10704/hard_reboot)

*   [Ask a new server](/servers/10704/ask_new)

26582-lb-01

`ubuntu`

`35.153.98.191`

running

Actions Toggle Dropdown

*   [Soft reboot](/servers/10730/soft_reboot)
*   [Hard reboot](/servers/10730/hard_reboot)

*   [Ask a new server](/servers/10730/ask_new)

Tasks
-----

### 0\. Block all incoming traffic but

mandatory

Let’s install the `ufw` firewall and setup a few rules on `web-01`.

Requirements:

*   The requirements below must be applied to `web-01` (feel free to do it on `lb-01` and `web-02`, but it won’t be checked)
*   Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
    *   `22` (SSH)
    *   `443` (HTTPS SSL)
    *   `80` (HTTP)
*   Share the `ufw` commands that you used in your answer file

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x13-firewall`
*   File: `0-block_all_incoming_traffic_but`

Done?! Help

×

#### Students who are done with "0. Block all incoming traffic but"

Check your code

×

#### Correction of "0. Block all incoming traffic but"

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

Copyright © 2023 ALX, All rights reserved.

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
