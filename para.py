import paramiko
import io

skey = """-----BEGIN OPENSSH PRIVATE KEY-----
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXX
-----END OPENSSH PRIVATE KEY-----"""

hostname = 'pi'
myuser = 'pi'
sshcon = paramiko.SSHClient()  # will create the object

not_really_a_file = io.StringIO(skey)
private_key = paramiko.RSAKey.from_private_key(not_really_a_file, password="111111")
not_really_a_file.close()

sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshcon.connect(hostname, username=myuser, pkey=private_key)

stdin_, stdout_, stderr_ = sshcon.exec_command("find", get_pty=True)
stdin_.close()
print("1")
for line in iter(stdout_.readline, ""):
    print(f"OUT: {line.rstrip()}")

sshcon.close()
