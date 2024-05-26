This script has been tested with python3. 
Paramicon must be installed for SSH connection. 

Install paramiko using the command below
pip install paramiko or pip3 install paramiko

--------------------------------------------------
SET SSH Connection 
# Device connection details
hostname = 'yourfirewallipaddress'
port = 22
username = 'admin'
password = 'password'
-------------------------------------------
SET Capture filter for collect PCAP and Global Counter

ssh_shell.send('debug dataplane packet-diag set filter match source 172.16.200.201 destination 8.8.8.8\n')
ssh_shell.send('debug dataplane packet-diag set filter match source 8.8.8.8 destination 172.16.200.201\n')
-------------------------------------------
SET repetitions and interval "for show counter global" command

    repetitions = 5  # Number of times to repeat the command
    interval = 5  # Interval in seconds between each command execution
--------------------------------------------------
SET OUTPUT FILE NAME

    output_file = 'counters.txt'  # File to save the command output
   
