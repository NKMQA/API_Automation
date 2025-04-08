# ✅ FIXTURE OUTSIDE THE CLASS

import pytest
from src.helpers.api_resquest_wrapper import post_request
from src.Constants.api_constants import APIconstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.Common_verfication import verify_response_key_should_not_be_none, verify_http_status_data

@pytest.fixture()
def create_token():
    response = post_request(
        url=APIconstants.url_create_token(),
        headers=common_headers_json(),
        auth=None,
        payloads=payload_create_token(),
        in_json=False
    )
    verify_http_status_data(response, 200)
    token = response.json()["token"]
    verify_response_key_should_not_be_none(token)
    return token

@pytest.fixture()
def create_booking():
    response = post_request(
        url=APIconstants.url_create_booking(),
        auth=None,
        headers=common_headers_json(),
        payloads=payload_create_booking(),
        in_json=False
    )
    verify_http_status_data(response, 200)
    bookingid = response.json()["bookingid"]
    verify_response_key_should_not_be_none(bookingid)
    return bookingid
