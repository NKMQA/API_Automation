# HTTP Status verifcation

#Verify the string --

def verify_http_status_data(response_data, expect_data):
    assert response_data.status_code == expect_data, "Expected HTTP Status Code " + str(expect_data) + ", but got " + str(response_data.status_code)



#Verfiy the token is exists or not ..
def verify_json_key_for_not_null(key):
    assert key !=0, "Key is non empty" + key
    assert key > 0, "Key is grater than zero"


def verify_response_key_should_not_be_none(key):
    assert key is not None

#Verify the response time

def verify_response_time():
    pass



# common verifcation
#HTTP sttaus code
# Headers
# data verifcation
#JSON Schema verifcation


#Why we need to verify whenver we create token token should be exists

# tEST CASE

# STATUS CODE , HEADERS , TOKEN SHOULD NOT BE NULLL AND ITS SHOULD BE STRING