# Read the CSV or Excel file
# Create a function create_token which can take values from the excel file
# Verify the expected result

import requests
import pytest
from src.Constants.api_constants import APIconstants
from src.helpers.utils import common_headers_json

#read the excel -- openyxl

import openpyxl
import pytest
#step1 - read the file and put the content into a []

def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password = row
        credentials.append({"username":username,"password":password})
    return credentials



def make_request_auth(username,password):
    payload = {
        "username": username,
        "password" : password
    }

    response = requests.post(APIconstants.url_create_token(),headers=common_headers_json(),json = payload)
    assert response.status_code ==200
    return response


@pytest.mark.parametrize("user_cred",read_credentials_from_excel("testdata.xlsx"))
def test_post_create_token(user_cred):
    username = user_cred ["username"]
    password = user_cred ["password"]
    response = make_request_auth(username,password)
    assert response.status_code ==200



