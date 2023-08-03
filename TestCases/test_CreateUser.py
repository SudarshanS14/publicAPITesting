import requests
#from requests import request

#URL to use : https://reqres.in/  ---> here POST is  https://reqres.in/api/users

url="https://reqres.in/api/users"
import pytest
import json
import jsonpath

@pytest.fixture(scope="module")
def start_exec():
    global file
    file = open('C:/scriptExample/WebServerTesting/ApiAutomation/json/createNewUser.json', 'r')

#@pytest.mark.skip
@pytest.mark.smoke
def test_create_new_user(start_exec):
    json_input=file.read()
    request_json=json.loads(json_input)
    print(f"Post request is {request_json} \n")
    #Now we make POST request passing json content in body
    response=requests.post(url,request_json)
    print(f"Response code is {response.status_code} \n")
    assert response.status_code == 201        #201 is response code of PUT
    print(f'Response we get back = {response.content} \n')

a=1
@pytest.mark.skipif(a>10,reason="Condition only if a is greater than 10")
@pytest.mark.sanity
def test_create_new_user1(start_exec):
    json_input=file.read()
    import json
    request_json=json.loads(json_input)
    print(f"Post request is {request_json} \n")
    #Now we make POST request passing json content in body
    response=requests.post(url,request_json)
    print(f"Response code is {response.status_code} \n")
    assert response.status_code == 201         #201 is response code of PUT
    print(f'Response we get back = {response.content} \n')

