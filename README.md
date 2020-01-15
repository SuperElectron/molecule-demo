Molecule Demo
=========

This is a demo made by following this page: https://www.jeffgeerling.com/blog/2018/testing-your-ansible-roles-molecule

Setup
=========
- check ```python --version``` and ensure that you are using python 3.
- your commands may need to be ```python3``` or some variable where you see ```python``` below.
- read INSTALL.rst inside /molecule
- read the getting started guide for molecule: https://molecule.readthedocs.io/en/latest/getting-started.html

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -e .
$ pip install 'molecule[docker]'
$ molecule test
```

Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: molecule.example, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
