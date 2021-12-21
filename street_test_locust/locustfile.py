from locust import HttpUser, task, between

class Api_User(HttpUser):
    wait_time = between(1, 1)

    @task
    def index(self):
        self.client.get(f'/people/1/')

#locust -f locustfile.py -H https://swapi.dev/api --headless -u 10 -r 10 -t 600s

