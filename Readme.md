## 携带token访问

```shell
curl -i localhost:8001/service/1 -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRlc3QifQ.eyJzdWIiOiJ3d3cuc2VydmljZS5jb20iLCJpc3MiOiJ3d3cuc2VydmljZS5jb20iLCJqdGkiOiI1NDMzM2IzOS1hZDUwLTRlYzYtODYxYS03Mjc2YjE2ZTBjNWYiLCJleHAiOjM0NTk1NjA4MTEsIm5iZiI6MTU2NzQwMDgxMSwiYXVkIjoiaHR0cDovL3d3dy5zZXJ2aWNlLmNvbSJ9.qkt0s9hBl0jDIJDfaUBG2y1XD3O8YA7D_ZeSjkFYXuNJZHeRgZNm4iq0H8ZJX3Mvz9o4kepKsgpFB0PB-oaHQZmJQSyeuFEkrNAYQ7MlOyuvy_8UFRTZwLPfy7BU3poltpiKL_NGcGF7nL1tR3JVP31h2Fdg6to0l2S1O0DeRO1LzPfrmm128ZknXD9blge8gi11bXBAvm5oQDo8_MyTVhwhJbAztM9c8bP_a0CcIhBaPdeanptlkJTzJzBL2Oz4oqqH6QdoLkl0TyhCO-a30Byo2P6iORPi1WZ72VfFTf9vl2Z3ElLoMPhUeihn3abOjw4FU-hy4Rgd1nuodyko7g"
HTTP/1.1 200 OK
content-type: text/html; charset=utf-8
content-length: 89
server: envoy
date: Mon, 02 Sep 2019 05:07:32 GMT
x-envoy-upstream-service-time: 6

Hello from behind Envoy (service 1)! hostname: d9640887bc7f resolved hostname: 172.23.0.2%  
```


## 不携带token访问

```shell
curl -i localhost:8001/service/1
HTTP/1.1 401 Unauthorized
content-length: 14
content-type: text/plain
date: Mon, 02 Sep 2019 04:08:11 GMT
server: envoy

Jwt is missing%  
```

## 携带错误的token访问

```shell
curl -i localhost:8001/service/1   -H "Authorization: Bearer dd"
HTTP/1.1 401 Unauthorized
content-length: 50
content-type: text/plain
date: Mon, 02 Sep 2019 04:58:34 GMT
server: envoy

Jwt is not in the form of Header.Payload.Signature%
```