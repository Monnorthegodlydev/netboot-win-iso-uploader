from scp import SCPClient
from paramiko import SSHClient
from sys import argv

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com', username='user', password='password')

scp = SCPClient(ssh.get_transport())

scp.put('')

