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

These are the default variables:

```yaml
htop_htoprc_destinations:
  skell:
    dest: /etc/skel/.config/htop
htop_replace_htoprc: true
```

You can define more destinations if you want. Per each destination, you can set owner,
grop and permission for `htoprc` file. See the example below.


Dependencies
------------

None :)

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: ansible-role-htop
       vars:
         htop_htoprc_destinations:
           skell:
             dest: /etc/skel/.config/htop
           another_user:
             dest: "/home/pippo/.config/htop"
             owner: "pippo"  # if missing, `root`
             group: "pippo"  # if missing, same as owner, or `root`
             mode: "0644"  # this is the default
         htop_replace_htoprc: true
```

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
