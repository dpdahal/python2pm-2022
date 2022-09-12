# data = {'ram', 'sita', 'gita', 'ram'}
# set is unordered collection of unique elements
# [],(),{}
# print(data)

data = {
    'name': 'ram',
    'age': 20,
    'address': 'kathmandu'
}
print(data.keys())
print(data.values())
print(data.items())
print(data.get('name'))

# print(dir(data))
#
# print(data['name'])
# users = [
#     {'name': 'ram', 'address': 'kathmandu'},
#     {'name': 'sita', 'address': 'bhaktapur'},
#     {'name': 'gita', 'address': 'lalitpur'},
# ]
# print(f"My name is: {users[0]['name']} and I live in {users[0]['address']}")
# student = {
#     'name': 'Sophia',
#     'province': {
#         'province_name': 'province 1',
#         'district': {
#             'district_name': 'Bhojpur'
#         }
#     }
# }
# print(f"{student['name']} {student['province']['province_name']} {student['province']['district']['district_name']}")
