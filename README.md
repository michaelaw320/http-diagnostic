# http-diagnostic

Simple webserver in docker container that will tell:
- Requester IP address
- X-Forwarded-For IP
- The container's public IP(v4 and v6)
- Request headers

This tool is build to check load balancer connections

Under the assumption of:

`Client` --> LB --> Container

Client IP should show Load Balancer's IP
and X-Forwarded-For should show real `Client` IP if the configuration of LB is correct.
