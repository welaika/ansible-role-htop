import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_skeleton_htoprc_exists(host):
    f = host.file('/etc/skel/.config/htop/htoprc')
    assert f.exists


def test_htoprc_exists_for_user(host):
    f = host.file('/home/jerry/.config/htop/htoprc')
    assert f.exists
