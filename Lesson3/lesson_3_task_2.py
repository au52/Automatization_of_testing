from smartphone import Smartphone

smartphone0 = Smartphone('Ulefone', 'ArmorX5', '+79998887766')
smartphone1 = Smartphone('Xiaomi', 'Redmi9', '+71112223344')
smartphone2 = Smartphone('Huawey', 'Honor90', '+70001112233')
smartphone3 = Smartphone('Apple', 'iPhone12', '+73332221100')
smartphone4 = Smartphone('Samsung', 'GalaxyS23', '+71113332288')

catalog = [smartphone0, smartphone1, smartphone2, smartphone3, smartphone4]

for elem in catalog:
    print(elem.getSmartAttr())