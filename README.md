# Network-Time-Protocol
A short and simple implementation of an NTP server and client coordinating to synchronize time!

## What is Network Time Protocol (NTP)
[[From Wikipedia](https://en.wikipedia.org/wiki/Network_Time_Protocol)]: The Network Time Protocol (NTP) is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks. In operation since before 1985, NTP is one of the oldest Internet protocols in current use. NTP was designed by David L. Mills of the University of Delaware. NTP is intended to synchronize all participating computers to within a few milliseconds of Coordinated Universal Time (UTC).

## How does NTP work?
The simplest way to understand the clock synchronization algorithm is as follows: An NTP client communicates with one or more NTP servers usually over UDP by sending a (let's say) "time_request" message timestamped $t_0$ to the server(s). The server(s), upon receiving this message, timestamp it as $t_1$. And sometime after $t_1$, respond to the "time_request" containing two timestamps: $t_1$ and $t_2$, where $t_2$ is the timestamp for this "time_response" message. The client, upon receiving the "time_response", timestamps $t_3$. This might not seem like much, but it is in fact all that the client needs! Assuming equal one-way delays for both the "time_request" and the "time_response", we can calculate the time offset ($\theta$) by just taking the absolute time difference between the two clocks and divide by 2 to account for the two way communication using this formula:  
$\theta = \frac{(t_1 - t_0) + (t_2 - t_3)}{2}$

For more detailed info, I recommend checking out this youtube video: [NTP by Computerphile](https://youtu.be/BAo5C2qbLq8) or if you'd like to read about the algorithm instead, here's the [anchor link](https://en.wikipedia.org/wiki/Network_Time_Protocol#Clock_synchronization_algorithm) in the Wikipedia page.

## How to execute my version of NTP?
Note: For simplicity I have used TCP sockets and only implement one server.
1. Download the TSClient.py and TSServer.py source files.
2. cd into the code directory and run TSServer.py using this command: ```python TSServer.py```. This will start an NTP server bound to localhost and listening on port 13202.
3. Then run TSClient.py using: ```python TSClient.py```. This will send a "time_request" to the server and print the server's response and offset. The offset here will be very small because both processes are running on the same machine and therefore share a common clock (No synchronization needed). If you would like to test between a client and server with a time difference, you can set up an EC2 instance with a faster (or slower) clock to host the server. Just remember to change the IP address in TSClient.py to match the EC2 instance's IP address!
