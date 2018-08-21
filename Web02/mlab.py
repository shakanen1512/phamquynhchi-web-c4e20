import mongoengine

# mongodb://<c4e20>:<jessemac87>@ds125892.mlab.com:25892/muadongkhonglanh

host = "ds125892.mlab.com"
port = 25892
db_name = "muadongkhonglanh"
user_name = "c4e20"
password = "jessemac87"


def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password
        )