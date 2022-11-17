# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# import requests
# import json
# import jsonpath
# baseUrl = "http://127.0.0.1:8000/users/"
# def test_create_delete_user() :
#     file = open('TestData/user.json',"r")
#     path = "api/users"
#     inputData = json.loads(file.read())
#     response = requests.post(url=baseUrl+path,json=inputData)
#     responseJson = json.loads(response.text)
#     assert response.status_code == 201
#     assert jsonpath.jsonpath(responseJson,'$.name')[0] == inputData["name"]
#     id = jsonpath.jsonpath(responseJson,'$.id')[0]
#     response = requests.delete(url=baseUrl+path+'/'+id)
#     assert response.status_code == 204