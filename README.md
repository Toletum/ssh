# SSH
## Add a ssh private key from environment with passphrase

<pre>
MYPASS="passphrase"
PK="-----BEGIN OPENSSH PRIVATE KEY----- ...... -----END OPENSSH PRIVATE KEY-----"
</pre>

### create a ssh_askpass
<pre>
cat <<EOF > ./myaskpass
echo $MYPASS
EOF

chmod 700 ./myaskpass
</pre>

### Add
<pre>
SSH_ASKPASS=./myaskpass ssh-add - <<<"${PK}"

# Check
ssh-add -l
</pre>

### Revome
<pre>
ssd-add -D
</pre>