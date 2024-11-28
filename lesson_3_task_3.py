from address import Address
from mailing import Mailing

to_address= Address(451254,"г.Москва", "ул.Лесная", 17,4)
from_address=Address(478906,"г.Казань","ул.Авиаторов",31,79)

mailing = Mailing (to_address, from_address, 747, 45668878798)

print (mailing)