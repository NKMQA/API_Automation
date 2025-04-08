# To make the post , put , patch, delete
import requests
import json

#HTTP methods - Generic functions

### Get
def get_request(url, auth, in_json):
    response = requests.get (url = url,auth = auth)
    if in_json is True:
        return response.json()
    return response


###Post
def post_request(url, auth, headers, payloads, in_json):
    post_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payloads))
    if in_json is True:
        return post_response.json()
    return post_response

###patch

def patch_request(url, auth,headers, payloads , in_json):
    patch_response = requests.patch(url = url, auth = auth , headers = headers , data = json.dumps(payloads))
    if in_json is True:
        return patch_response.json()
    return patch_request

# PUT
def put_request(url, auth, headers, payloads, in_json):
    put_response = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payloads))
    if in_json:
        return put_response.json()
    return put_response

# DELETE
def delete_request(url, auth, headers, payloads, in_json):
    delete_response = requests.delete(url=url, auth=auth, headers=headers, data=json.dumps(payloads))
    if in_json:
        return delete_response.json()
    return delete_response


###XML data we can convert to Json if we have paylaod on XML we can convert before sending

