# test_in_swapi.py
![image](https://user-images.githubusercontent.com/80243681/146916591-4ff4511d-48fb-4aa5-8bc1-5a1493b66f0f.png)

* just run: `pytest`


# locustfile.py
![image](https://user-images.githubusercontent.com/80243681/146943689-db934882-5c8b-4e3a-af32-56ef89fd16ea.png)locust google -u 10 -r 10 -t 10s

![image](https://user-images.githubusercontent.com/80243681/146941136-04cf4133-5c66-442d-9cd8-c30aad9beda6.png)locust swapi -u 10 -r 10 -t 10s


* if current directory at street_test_locust run: `locust -f locustfile.py -H https://swapi.dev/api --headless -u 10 -r 10 -t 10s`

* if current directory is the main directory run: `locust -f ./street_test_locust/locustfile.py -H https://swapi.dev/api --headless -u 10 -r 10 -t 10s`
