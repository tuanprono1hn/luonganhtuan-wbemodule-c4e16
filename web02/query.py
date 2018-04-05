from  models.service import Service
import mlab
mlab.connect()
# all_services = Service.objects()
# print(all_services[10].name)
id_to_find = "5ac0946d481e4119d86798fe"

# kieu_anh = Service.objects(id=id_to_find)[0]
# kieu_anh = Service.objects.get(id=id_to_find)
service = Service.objects.with_id(id_to_find)

if service is None:
    print("Service not found")
else:
    # print(kieu_anh.to_mongo())
    # kieu_anh.delete()
    service.update(set__address="Hanoi")
    service.reload()
    print(service.address)
    # print("Deleted")
