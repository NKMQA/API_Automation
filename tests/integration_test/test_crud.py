
from src.helpers.api_resquest_wrapper import post_request,put_request,delete_request
# from src.Constants.api_constants import BASE_URL,APIconstants,base_url
from src.Constants.api_constants import APIconstants
from src.helpers.utils import common_headers_json,common_headers_for_put_delete_patch
from src.helpers.payload_manager import payload_create_booking,payload_create_token
from src.helpers.Common_verfication import verify_response_key_should_not_be_none, verify_http_status_data

import pytest

class Testcreatebooking:

    def test_update_booking(self, create_token, create_booking):
        bookingid = create_booking
        put_url = APIconstants.url_create_booking() + "/" + str(bookingid)

        headers = common_headers_for_put_delete_patch()
        headers["Cookie"] = "token=" + create_token  # <-- Use the token here

        response = put_request(
            url=put_url,
            auth=None,
            headers=headers,
            payloads=payload_create_booking(),
            in_json=False
        )
        print(response.status_code)
        print(response.text)

    def test_delete_booking(self, create_token, create_booking):
        bookingid = create_booking
        delete_url = APIconstants.url_create_booking() + "/" + str(bookingid)

        headers = common_headers_for_put_delete_patch()
        headers["Cookie"] = "token=" + create_token  # Inject token into headers

        response = delete_request(
            url=delete_url,
            auth=None,
            headers=headers,
            payloads=None,
            in_json=False
        )
        print(response.status_code)
        print(response.text)
