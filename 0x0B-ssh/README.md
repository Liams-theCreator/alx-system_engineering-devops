# Project 0x0B. SSH

## Table of Contents
- [Project 0x0B. SSH](#project-0x0b-ssh)
	- [Table of Contents](#table-of-contents)
	- [Project Description](#project-description)
		- [Background Context](#background-context)
		- [Learning Objectives](#learning-objectives)
	- [Tasks](#tasks)
		- [0. Use a private key](#0-use-a-private-key)
		- [1. Create an SSH key pair](#1-create-an-ssh-key-pair)
		- [2. Client configuration file](#2-client-configuration-file)
		- [3. Let me in!](#3-let-me-in)
	- [Copyright and License](#copyright-and-license)

---

## Project Description

This project focuses on SSH (Secure Shell) and covers topics related to server management, SSH key pairs, and client configuration. You will be working with an Ubuntu server and learning how to use SSH to connect securely.

### Background Context

In this project, you have been assigned an Ubuntu server hosted in a datacenter. You will connect to this server using SSH, but instead of using a password, you will use an RSA key pair. Your server is configured with the public key you created in a previous project.

### Learning Objectives

By the end of this project, you should be able to:

- Explain what a server is and where servers are typically hosted.
- Describe what SSH (Secure Shell) is and its importance in secure communication.
- Create an SSH RSA key pair.
- Connect to a remote host using an SSH RSA key pair.
- Understand the advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` in script shebangs.

---

## Tasks

### 0. Use a private key

Write a Bash script that uses SSH to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

Requirements:
- Use only SSH single-character flags (do not use `-l`).
- You do not need to handle the case of a private key protected by a passphrase.

### 1. Create an SSH key pair

Write a Bash script that creates an RSA key pair.

Requirements:
- Name of the created private key must be `school`.
- The number of bits in the created key should be 4096.
- The created key must be protected by the passphrase `betty`.

### 2. Client configuration file

Your machine has an SSH configuration file for the local SSH client. Configure it to use the private key `~/.ssh/school` and refuse to authenticate using a password.

### 3. Let me in!

Add the provided SSH public key to your server so that others can connect using the `ubuntu` user.

---

## Copyright and License

© 2023 ALX, All rights reserved.