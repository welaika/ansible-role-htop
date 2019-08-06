Ansible Role Htop
===================

[![Build Status](https://travis-ci.org/welaika/ansible-role-htop.svg?branch=master)](https://travis-ci.org/welaika/ansible-role-htop)

Install htop with a custom htoprc

This repo is a fork of [ https://github.com/Oefenweb/ansible-htop ]( https://github.com/Oefenweb/ansible-htop ). Thanks!

Requirements
------------

None

Role Variables
--------------

None

Dependencies
------------

None :)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-htop, x: 42 }

License
-------

MIT

Testing
-------

Install molecule

`$ pip3 install --user 'molecule[docker]'`

Start docker and run

`$ molecule test`

Author Information
------------------

made with ❤️ and ☕️ by [weLaika](https://dev.welaika.com)
