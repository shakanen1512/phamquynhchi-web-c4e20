from models.services import Service
import mlab

mlab.connect()

# all_service = Service.objects()

# first_service = all_service[0]
# print(first_service["name"])

#id_to_find = "5b7824df68515112b82b6727"

#one_service = Service.objects.get(id=id_to_find) #get service object
#one_service = Service.objects.with_id(id_to_find)

#if one_service is not None:
    #print(one_service.name)

    #one_service.delete()
    #print("Deleted")

#     one_service.update(set__yob=2005, set__name="Linh Ka")
#     one_service.reload()
#     print(one_service.to_mongo())

# else:
#     print("Not found")

#Service.objects(id=id_to_find).delete()

Service.objects.delete()