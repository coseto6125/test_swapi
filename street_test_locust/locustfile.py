from locust import HttpUser, task
from locust.user.wait_time import constant_pacing
from locust.contrib.fasthttp import FastHttpUser

#class Api_User(FastHttpUser):
class Api_User(HttpUser):
    wait_time = constant_pacing(1)
    network_timeout = 5.0
    connection_timeout = 5.0
    @task
    def test_locust(self):
        with self.client.get("https://swapi.dev/api/people/1/",catch_response=True) as r:
            Vehicles_size = len(r.json()['vehicles'])
            assert Vehicles_size >= 1                       #------Vehicles_size >= 1
            assert r.status_code == 200                     #------http status check == 200
            if r.status_code ==200:                         #------http status check != 200 will be [Failed!]
                r.success()
            else:
                r.failure("GetActConfig[Failed!]")
                
#locust -f locustfile.py -H https://swapi.dev/api --headless -u 10 -r 10 -t 10s
#locust -f ./street_test_locust/locustfile.py -H https://swapi.dev/api --headless -u 10 -r 10 -t 10s
