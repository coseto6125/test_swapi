# test_in_swapi.py
![image](https://user-images.githubusercontent.com/80243681/146916591-4ff4511d-48fb-4aa5-8bc1-5a1493b66f0f.png)

* just run: `pytest`


# locustfile.py
![image](https://user-images.githubusercontent.com/80243681/146916796-083f0016-80ea-4af1-9fc9-b466a2c95c13.png)

* if current directory at street_test_locust run: `locust -f locustfile.py -H https://swapi.dev/api --headless -u 10 -r 10 -t 600s`

* if current directory is the main directory run: `locust -f ./street_test_locust/locustfile.py -H https://swapi.dev/api --headless -u 10 -r 1 -t 10s`
