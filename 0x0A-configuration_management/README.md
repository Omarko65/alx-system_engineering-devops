 
   0x0A. Configuration management
==============================

#### In a nutshell…

- **Auto QA review:** 0.0/9 mandatory
- **Altogether:** **0.0%**
    - Mandatory: 0.0%
    - Optional: no optional tasks
 
Background Context
------------------

[![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a0a8024f2b1c47a9d1e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221018T220607Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9a229e7821da751c130b596c031d8b76de1d61e333d4ad94a7b5e90708589e36)](https://youtu.be/ogYLFyp68cI)

When I was working for SlideShare, I worked on an auto-remediation tool called [Skynet](/rltoken/0zbIzBqH_ktMmRQvJwZs2A "Skynet") that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent `nil` to the filter method.

There were 2 pieces of bad news:

1. When MCollective receives `nil` as an argument for its filter method, it takes this to mean ‘all servers’
2. The action I sent was to terminate the selected servers

I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/292/4i8il3B.gif)

That was me ^\_^‘: [https://twitter.com/devopsreact/status/836971570136375296](/rltoken/jIyF-Oa80s40ssG21cyNAg "https://twitter.com/devopsreact/status/836971570136375296")

Resources
---------

**Read or watch**:

- [Intro to Configuration Management](/rltoken/GL30hu-aRcKzPOvK8JO-Bg "Intro to Configuration Management")
- [Puppet resource type: file](/rltoken/DjSqEUZh5jSvzQbr8Hn_hA "Puppet resource type: file") (*check “Resource types” for all manifest types in the left menu*)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](/rltoken/fZbIuIwhPZWQUQNTjsqu1A "Puppet's Declarative Language: Modeling Instead of Scripting")
- [Puppet lint](/rltoken/CRUMeEMdcX-UtbWsUM9xLQ "Puppet lint")
- [Puppet emacs mode](/rltoken/MzHXCntAkPzOqMnI6_rpWQ "Puppet emacs mode")

Requirements
------------

### General

- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension `.pp`

Note on Versioning
------------------

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Install `puppet`

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

```

You do **not** need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](/rltoken/u-eUjjYAqDDoxYFeyrA3GA "Puppet 5 Docs")

### Install `puppet-lint`

```
$ gem install puppet-lint

```

 Tasks
-----

 ###  0. Create a file 

  mandatory        Score: 0.0% (Checks completed: 0.0%)   Using Puppet, create a file in `/tmp`.

Requirements:

- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains `I love Puppet`

Example:

```
root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.5.2
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppetroot@6712bef7a528:~#

```

   **Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0A-configuration_management`
- File: `0-create_a_file.pp`
 
         Done?!   Help  ×#### Students who are done with "0. Create a file"

        Check your code  ×#### Correction of "0. Create a file"

   Start a new test Close        Requirement success   Requirement fail    Code success   Code fail    Efficiency success   Efficiency fail    Text answer success   Text answer fail    Skipped - Previous check failed       Get a sandbox  QA Review  ×#### 0. Create a file

  ##### Commit used:

- **User:** `` ---
- **URL:** Click here
- **ID:** `---`
- **Author:** ---
- **Subject:** *---*
- **Date:** ---
 
 
         ###  1. Install a package 

  mandatory        Score: 0.0% (Checks completed: 0.0%)   Using Puppet, install `flask` from `pip3`.

Requirements:

- Install `flask`
- Version must be `2.1.0`

Example:

```
root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1

```

   **Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0A-configuration_management`
- File: `1-install_a_package.pp`
 
         Done?!   Help  ×#### Students who are done with "1. Install a package"

        Check your code  ×#### Correction of "1. Install a package"

   Start a new test Close        Requirement success   Requirement fail    Code success   Code fail    Efficiency success   Efficiency fail    Text answer success   Text answer fail    Skipped - Previous check failed       Get a sandbox  QA Review  ×#### 1. Install a package

  ##### Commit used:

- **User:** `` ---
- **URL:** Click here
- **ID:** `---`
- **Author:** ---
- **Subject:** *---*
- **Date:** ---
 
 
         ###  2. Execute a command 

  mandatory        Score: 0.0% (Checks completed: 0.0%)   Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

- Must use the `exec` Puppet resource
- Must use `pkill`

Example:

Terminal #0 - starting my process

```
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow

```

Terminal #1 - executing my manifest

```
root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/# 

```

Terminal #0 - process has been terminated

```
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#

```

   **Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0A-configuration_management`
- File: `2-execute_a_command.pp`
 
         Done?!   Help  ×#### Students who are done with "2. Execute a command"

        Check your code  ×#### Correction of "2. Execute a command"

   Start a new test Close        Requirement success   Requirement fail    Code success   Code fail    Efficiency success   Efficiency fail    Text answer success   Text answer fail    Skipped - Previous check failed       Get a sandbox  QA Review  ×#### 2. Execute a command

  ##### Commit used:

- **User:** `` ---
- **URL:** Click here
- **ID:** `---`
- **Author:** ---
- **Subject:** *---*
- **Date:** ---
 
 
        ×#### Recommended Sandbox

  Copyright © 2022 ALX, All rights reserved.           ×#### Markdown Guide

 #### Emphasis

```
**bold**
*italics*
~strikethrough~~
```

#### Headers

```
# Big header
## Medium header
### Small header
#### Tiny header
```

#### Lists

```
* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item
```

#### Links

```
[Text to display](http://www.example.com)
```

#### Quotes

```
> This is a quote.
> It can span multiple lines!
```

#### Images

CSS style available: `width, height, opacity`

```
![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
```

#### Tables

```
| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

Or without aligning the columns...

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
```

#### Displaying code

`var example = "hello!";`

Or spanning multiple lines...

```
var example = "hello!";
alert(example);
```

    
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create',
        'UA-67152800-9',
        'auto', {
          userId: '26582'
        }
      );

    ga('send', 'pageview');

    $(document).ready(function() {
      ga(function(tracker) {
        var clientId = tracker.get('clientId');
        $('.ga-client-id').val(clientId);
      });
    }); 