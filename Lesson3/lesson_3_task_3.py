from class_Address import Address
from class_Mailing import Mailing

to_addr = Address('123321', 'Moscow', 'Tverskaya', '1', '52')
from_addr = Address('603000', 'Nizny Novgorod', 'B.Pokrovskaya', '3', '21')

mail = Mailing(to_addr, from_addr, 300, 183648751641)
# Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в
# <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.
print('Отправление', mail.getTrack(), 'из', mail.getFromAddr(), 'в',
      mail.getToAddr() + '. ' + 'Стоимость', mail.getCost(), 'рублей.')

