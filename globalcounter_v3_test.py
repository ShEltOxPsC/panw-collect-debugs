# Created By Palo Alto Networks PSC IDEUS #
import paramiko
import time

# Device connection details
hostname = '172.16.200.50'
port = 22
username = 'sezgi'
password = 'GbAdv123!!'

def disable_pager_and_repeat_show_counters(repetitions, interval, output_file):
    # Create an SSH client
    client = paramiko.SSHClient()
    
    # Automatically add untrusted hosts (make sure to use this with caution)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect to the device
    client.connect(hostname, port, username, password)
    print("Collecting START :)")
    # Open a shell
    ssh_shell = client.invoke_shell()

    # Disable CLI pager
    ssh_shell.send('set cli pager off\n')
    time.sleep(1)  # Give it a second to process the command
    #show clock
    ssh_shell.send('show clock\n')
    time.sleep(1)  # Give it a second to process the command
    ssh_shell.send('show system info\n')
    time.sleep(1)  # Give it a second to process the command
    ssh_shell.send('debug dataplane packet-diag set filter match source 172.16.200.201 destination 8.8.8.8 destination-port 53\n')
    time.sleep(1)  # Give it a second to process the command
    ssh_shell.send('debug dataplane packet-diag set filter match source 8.8.8.8 destination 172.16.200.201 source-port 53\n')
    time.sleep(1)  # Give it a second to process the command
    ssh_shell.send('debug dataplane packet-diag set capture stage drop file drp\n')
    time.sleep(1)  # Give it a second to process the command
    ssh_shell.send('debug dataplane packet-diag set capture stage receive file rx\n')
    time.sleep(1)  # Give it a second to process the command
    ssh_shell.send('debug dataplane packet-diag set capture stage transmit file tx\n')
    time.sleep(1)  # Give it a second to process the command
    ssh_shell.send('debug dataplane packet-diag set capture stage firewall file fw\n')
    time.sleep(1)  # Give it a second to process the command
    ssh_shell.send('debug dataplane packet-diag set filter on\n')
    time.sleep(1)  # Give it a second to process the command
    ssh_shell.send('debug dataplane packet-diag set capture on\n')
    time.sleep(1)  # Give it a second to process the command
    print('Filters Activated')

with open(output_file, 'w') as file:
    # Repeat the command the specified number of times
    for i in range(repetitions):
        # Run the command to show counters
        ssh_shell.send('show counter global filter packet-filter yes delta yes\n')
        time.sleep(interval)  # Wait for the command to complete and pause before next iteration
        print("Counters OK")
      
        if some_condition:('show counter global filter packet-filter yes delta yes\n')
            ssh_shell.send('debug dataplane packet-diag set capture off\n')
            time.sleep(10)  # Give it a second to process the command
            #show clock
            ssh_shell.send('show clock\n')
            time.sleep(1)  # Give it a second to process the command
            ssh_shell.send('exit\n')
            time.sleep(1)  # Give it a second to process the command
            
            # Receive the command output
            output = ssh_shell.recv(65535).decode('utf-8')
            
            # Write the command output to the file
            file.write(f"Iteration {i+1}:\n{output}\n")
            print(f"Iteration {i+1} output saved to {output_file}")

    # Close the connection
    ssh_shell.close()
    client.close()
    print("Collecting END :)Please share outputs email to sdogan@paloaltonetworks.com")
if __name__ == '__main__':
    repetitions = 5  # Number of times to repeat the command
    interval = 5  # Interval in seconds between each command execution
    output_file = 'counters.txt'  # File to save the command output
    disable_pager_and_repeat_show_counters(repetitions, interval, output_file)
