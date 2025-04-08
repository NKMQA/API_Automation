
from src.helpers.api_resquest_wrapper import post_request
# from src.Constants.api_constants import BASE_URL,APIconstants,base_url
from src.Constants.api_constants import APIconstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking,payload_create_token
from src.helpers.Common_verfication import verify_response_key_should_not_be_none, verify_http_status_data

import pytest
class Testcreatebooking(object):

    def test_create_token(self):
        response = post_request(
            url=APIconstants.url_create_token(),
            headers=common_headers_json(),
            auth=None,
            payloads=payload_create_token(),
            in_json=False
        )
        verify_http_status_data(response, 200)
        print(response.json())  # ✅ properly calls the method

    def test_create_booking(self):
        response= post_request(url=APIconstants.url_create_booking(),auth=None,headers=common_headers_json(),payloads=payload_create_booking(),in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_data(response,200)
        bookingid = response.json()["bookingid"]
        print(bookingid)

    def test_update_booking(self):  #token and booking id from the create booking , token
        token = "e839e29c4253907"
        put_url= payload_create_booking() + "/3483"
        auth= ("admin","password123")
        response = put_request(url=put_url, auth=None, headers=common_headers_json(),
                                payloads=payload_create_booking(), in_json=False)
        print(response)





    def test_delete_booking(self):  #token and booking id from the create booking , token
        pass








