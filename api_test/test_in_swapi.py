import pytest
from json import loads
import requests

var_people_id = 10
var_vehicles_count= 20
var_height= 30
var_films_id= 5

class swapitest:
    def __init__(self):
        self.api_target_url = 'https://swapi.dev/api/'
        
    def api_1(self,people_id:int):
        r = requests.get(f'{self.api_target_url}people/{people_id}')
        r_data = loads(r.text)
        Vehicles_count= len(r_data['vehicles'])
        height= int(r_data['height'])
        return r.status_code,Vehicles_count,height,
    
    def api_2(self,people_id:int,film:int):
        r_film = requests.get(f'{self.api_target_url}films/{film}')
        r_film_data = loads(r_film.text)
        r_p_status,vehicles_count_people,__ = self.api_1(people_id)
        r_f_status = r_film.status_code
        vehicles_count_films= len(r_film_data['vehicles'])
        return r_p_status,r_f_status,vehicles_count_people,vehicles_count_films


class Test_01(object):
    def test_api_1_people(self):
        rs_status,vehicles_count,height = swapitest().api_1(var_people_id)
        assert rs_status == 200                     #------check http code 200
        assert height > var_height                  #------height must > var_height
        assert vehicles_count == var_vehicles_count #------Vehicles_count must == var_vehicles_count
        return
    def test_api_2_films(self):
        r_p_status,r_f_status,\
        vehicles_count_p,vehicles_count_f = swapitest().api_2(var_people_id,var_films_id)
        assert r_p_status == r_f_status == 200      #------check http code 200
        assert vehicles_count_f > vehicles_count_p  #------api_2 > api_1 (vehicles_count)
        return
    
if __name__ == '__main__':
    pytest.main(['-s'])