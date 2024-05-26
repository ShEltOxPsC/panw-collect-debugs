SET Capture filter for collect PCAP and Global Counters

ssh_shell.send('debug dataplane packet-diag set filter match source 172.16.200.201 destination 8.8.8.8\n')

ssh_shell.send('debug dataplane packet-diag set filter match source 8.8.8.8 destination 172.16.200.201\n')

SET repetitions and interval "for show counter global" command

    repetitions = 5  # Number of times to repeat the command
    interval = 5  # Interval in seconds between each command execution

SET OUTPUT FILE NAME

    output_file = 'counters.txt'  # File to save the command output
   
