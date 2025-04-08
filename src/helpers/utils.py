# Common headers

#This is for content type json
def common_headers_json():
    headers = {
        "Content-type": "application/json",
    }
    return headers


def common_headers_for_put_delete_patch():
    headers={
        "content-type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM"
    }
    return headers

# This for content type xml
def common_headers_xml():
    headers = {
        "content-type": "application/xml"
    }
    return headers




#Read data from excel , csv,json , yaml - keep the functions in future

