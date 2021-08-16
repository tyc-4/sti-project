# STI Project Demo - Open Source IDS using RouterOS

## Project Description
This project is a prototype of an IDS that uses open-source and one-time license applications to monitor traffic flowing in a network. It will be able to flag out suspicous traffic and send an alert to the administrator. This alert is then picked up by TagUI, a RPA tool, to block the offending device off the network to prevent further attacks.

The actions taken can be easily modified through the script as it uses TagUI, which has a human-language-like syntax that can be learnt quickly. Currently, it is configured to get the offending IP address and add a firewall rule on the router CLI to block off traffic from it. 

## Network Environment
Main network: **192.168.88.0/24**

Router's IP address: **192.168.88.1**

The ntopng server is running on a Ubuntu LTS 20.04 VM and listening at **192.168.88.3**

The attacker machine and the client running the network monitoring script are set get an IP address automatically through DHCP.

*All IP addresses can be changed in the Python script*

## Setup Guide
You can replicate this setup using the following guides:

- [Configuring MikroTik Router NetFlow](https://www.ntop.org/ntopng/how-to-analyse-mikrotik-traffic-using-ntopng/)
    
- [ntop Installation Guide](https://www.ntop.org/guides/ntopng/what_is_ntopng.html)
    
- [TagUI Python Github](https://github.com/tebelorg/RPA-Python)


## Demo Video
[![YouTube Demo Video](https://img.youtube.com/vi/OGnJ9xy6rMU/0.jpg)](https://www.youtube.com/watch?v=OGnJ9xy6rMU)
