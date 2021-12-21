#
if current directory at street_test_locust run: locust -f locustfile.py -H https://swapi.dev/api --headless -u 10 -r 10 -t 600s
if current directory is the main directory run: locust -f ./street_test_locust/locustfile.py -H https://swapi.dev/api --headless -u 10 -r 1 -t 10s
