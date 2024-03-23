# Configuration Management Project

## Project Overview

This project is part of the ALX DevOps curriculum and focuses on configuration management using Puppet. It includes tasks related to creating files, installing packages, and executing commands using Puppet manifests.

## Table of Contents

- [Configuration Management Project](#configuration-management-project)
	- [Project Overview](#project-overview)
	- [Table of Contents](#table-of-contents)
	- [Background Context](#background-context)
	- [Requirements](#requirements)
		- [General](#general)
		- [Note on Versioning](#note-on-versioning)

## Background Context

The background context provides insights into the significance of configuration management and its role in maintaining infrastructure.


## Requirements

### General

- All  files will be interpreted on Ubuntu 20.04 LTS.
- All your files should end with a new line.
- A README.md file at the root of the folder of the project is mandatory.
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
 Puppet manifests must run without error.
-  Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
-  Puppet manifests files must end with the extension .pp.

### Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

To install Puppet, run the following commands:

```shell
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
