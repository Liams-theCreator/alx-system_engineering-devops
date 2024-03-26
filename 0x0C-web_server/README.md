# Web Server Configuration Tasks

This repository contains scripts and configurations for configuring a web server using Nginx. Below are the tasks and their descriptions:

## Task 0: Transfer a File to Your Server

**File:** 0-transfer_file

This task involves writing a Bash script that transfers a file from a client to a server using the `scp` command. The script accepts four parameters:

- Path to the file to be transferred
- IP of the server
- Username for the `scp` connection
- Path to the SSH private key used by `scp`

Usage:
```bash
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
```

## Task 1: Install Nginx Web Server

**File:** 1-install_nginx_web_server

In this task, a Bash script is provided to install Nginx on a web server. The requirements for this task include:

- Installing Nginx on the server
- Configuring Nginx to listen on port 80
- Verifying that a GET request to the root `/` returns a page containing the string "Hello World!"

Usage:
```bash
./1-install_nginx_web_server
```

## Task 2: Setup a Domain Name

**File:** 2-setup_a_domain_name

This task involves setting up a domain name for the web server. The requirements include:

- Providing the root domain name (e.g., foobar.tech)
- Configuring DNS records with an A entry to point to the web server's IP address
- Entering the domain name in the Project website URL field

Example:
```bash
cat 2-setup_a_domain_name
myschool.tech
```

## Task 3: Redirection

**File:** 3-redirection

In this task, a Bash script is provided to configure Nginx for URL redirection. The requirements include:

- Setting up a 301 Moved Permanently redirection for `/redirect_me` to another page

Usage:
```bash
./3-redirection
```

## Task 4: Not Found Page 404

**File:** 4-not_found_page_404

This task involves configuring Nginx to display a custom 404 page with the message "Ceci n'est pas une page" when a resource is not found. The page must return an HTTP 404 error code.


