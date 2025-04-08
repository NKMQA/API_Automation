
from src.helpers.api_resquest_wrapper import post_request
# from src.Constants.api_constants import BASE_URL,APIconstants,base_url
from src.Constants.api_constants import APIconstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.Common_verfication import verify_response_key_should_not_be_none, verify_http_status_data

import pytest
class Testcreatebooking(object):
    @pytest.mark.postive
    def test_create_booking_tc1(self):
        response= post_request(url=APIconstants.url_create_booking(),auth=None,headers=common_headers_json(),payloads=payload_create_booking(),in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_data(response,200)
        bookingid = response.json()["bookingid"]
        print(bookingid)

    @pytest.mark.negative
    def test_create_booking_tc2(self):
        response = post_request(
            url=APIconstants.url_create_booking(),
            auth=None,
            headers=common_headers_json(),
            payloads=None,
            in_json=False
        )

        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        # Negative test: expecting 400 Bad Request
        verify_http_status_data(response, 400)

        try:
            error_json = response.json()
            print("Error JSON:", error_json)
        except Exception as e:
            print("Response is not in JSON format. Error:", str(e))


