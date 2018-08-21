from models.services import Service
import mlab

mlab.connect()

# all_service = Service.objects()

# first_service = all_service[0]
# print(first_service["name"])

id_to_find = "5b7825e66851511548c8af3f"

# one_service = Service.objects.get(id=id_to_find)
# print(one_service["name"])

Service.objects(id=id_to_find).delete()