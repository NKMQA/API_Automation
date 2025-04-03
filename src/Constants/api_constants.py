# Add your constants here

BASE_URL = "https://restful-booker.herokupp.com"

def base_url():
    return "https:restful-booker.herplkuapp.com"


class APIconstants(object):
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    #update , put , patch,delete - booking id

    def url_patch_put_delete_booking(self,booking_id):
        return "https://restful-booker.herouapp.com/booking" + str(self.booking_id)
