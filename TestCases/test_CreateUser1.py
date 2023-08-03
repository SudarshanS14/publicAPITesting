import requests
#from requests import request

#URL to use : https://reqres.in/  ---> here POST is  https://reqres.in/api/users

url="https://reqres.in/api/users"
import pytest
import json
import jsonpath

import pytest
@pytest.mark.sanity
def test_get_user_details():
    import requests

    url = "https://reqres.in/api/users?page=2"

    from requests import request

    response = requests.get(url)

    print(response)  # we get the response as 200 stating its a success
    print(response.status_code, "\n")
    assert response.status_code == 200  # assert is used to validae. Stops in case we get response other than 200

    # get response header only without body
    print(response.headers, "\n")
    print(response.headers.get('Date'), "\n")
    print(response.cookies, "\n")
    print(response.encoding, "\n")
    print(response.elapsed, "\n")  # time taken to get the response from the server

    # to display content
    print(response.content, "\n")

    import json
    json_response = json.loads(response.text)
    print(json_response, "\n")

    # Fetch value from json path now stored above
    import jsonpath
    pages = jsonpath.jsonpath(json_response, 'total_pages')  # to fetch value from json path
    print(pages)  # gets o/p in a list
    print(pages[0])  # get o/p as value

    assert pages[0] == 2  # to calidate if pages is 2

    data = jsonpath.jsonpath(json_response, 'data')
    print(data, '\n')
    print(data[0], '\n')
    firstname = jsonpath.jsonpath(json_response, 'data[0].first_name')  # to get first_name from 1st index
    print(firstname, '\n')

    # IMPORTANT we pass the calue in loop by [+i+] since loop accepts string we use ['+str(i)+']
    # how to get first_name from all index
    for i in range(0, 3):
        firstname = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')  # we use +i+ to string +str(i)+
        print(firstname)

