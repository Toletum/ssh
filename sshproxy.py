import paramiko
import sys
import time
import threading

hostname = 'pi'
myuser = 'pi'
sshcon = paramiko.SSHClient()  # will create the object

private_key = paramiko.RSAKey.from_private_key_file("/home/toletum/.ssh/id_rsa")

sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshcon.connect(hostname, username=myuser, pkey=private_key)

def leer(stdout):
    while True:
        r = stdout_.read(1)
        while r:
            print(r.decode(), end="")
            r = stdout_.read(1)
        time.sleep(0.01)


stdin_, stdout_, stderr_ = sshcon.exec_command("bash", get_pty=True)
stdin_.flush()
x = threading.Thread(target=leer, args=(stdout_,))
x.start()
while True:
    char = sys.stdin.read(1)
    if char:
        stdin_.write(char)
    time.sleep(0.01)
stdin_.close()
sshcon.close()
