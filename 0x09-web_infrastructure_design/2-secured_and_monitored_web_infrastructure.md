![My Image](https://github.com/hallumy/alx-system_engineering-devops/blob/master/images/rsz_task_2.jpg)

THE INFRASTRUCTURE

Upon request to access www.foobar.com, and the IP address is provided by the DNS, the domain is served under HTTPS which encrypts all requests and responses on the normal HTTP using a TLS (SSL). The web server sends a copy of its SSL certificate and the browser checks whether the SSL certificate can be trusted or not. If it trusts the SSL certificate, it sends a message to the web server and the web server sends back a digitally signed acknowledgement to start an SSL-encrypted session. The purpose of an SSL certificate is to encrypt traffic between a web server and external networks, preventing middle-men attacks which could expose valuable information. 

The purpose of a firewall is to protect data by blocking unwanted incoming networks and unauthorized users for the incoming traffic in a network. Each server has a firewall to increase reliability, in case one server fails the other one can take over. It is scalable horizontally because you can add another node without affecting the service currently being offered

Monitoring clients analyze the performance and operations of servers and alert the administrators if the servers are not working as expected. They automatically test the accessibility of the servers, measure response time, and alert for errors such as violations, missing files, and other security vulnerabilities. Three monitoring systems have been put in place to check:
Monitoring that CPU used and the network information of each and every server
Monitoring the speed and checking if the users have experienced an error: For example, using New relic
Monitoring that the website checks that the server is working in various regions

ISSUES WITH INFRASTRUCTURE

SSL termination
With the connection between the web browser/client and server being encrypted using SSL. Then we ensure to terminate the SSL addition in the individual servers and not the load balancer. This is because since the SSL is to ensure secure communication by terminating at the load balancer we end up having an unsecured line between the load balancer and the destination server where information is susceptible to attack from bad actors. 

One Mysql write server as a SPOF and/or bottleneck 
With the configuration employing one master/primary database as the sole server with write permissions can prove fatal to high availability. For example, if the database happens to fail permanently then we cannot write anymore in the database hence bringing up issues for our services. Secondly, in case of a high volume of write requests when employing one write database then there is a bottleneck introduced in the system since all write requests have to go through the same database leading to congestion and long queues. 

Having Servers with the same components is a problem since. 
It might be hard when monitoring to accurately pinpoint the server having à problem since the components are all equal. Secondly, when load balancing if the components are the same then the behavior will be the same for all components leading to the same bottleneck characteristic. Then if a problem is a hardware issue all servers might fail the same way at the same time leading to disruption of services. 



