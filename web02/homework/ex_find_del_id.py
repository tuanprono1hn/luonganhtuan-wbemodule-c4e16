from models.customer import Customer
import mlab
id_to_find = "5ac4d81168f6fc35b4deb351"
mlab.connect()
customer_to_find = Customer.objects.get(id = id_to_find).delete()
