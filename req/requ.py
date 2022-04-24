import requests

headers = 'application/json'

data = {
"office" : "xyz",
"branch" : "xyz", 
"office_branch" :"xyz", 
"bill_number" : "xyz",
"mobile_number" : 8993758839, 
"customer" : "test", 
"bill_amount" : 43.23,
"card_number": "101201A",
"points": 54.34
}


# api to get particular user's data based on branch, office and mobile number
# response = requests.get('http://127.0.0.1:8000/reward_data_detail?office=nayan&branch=nayan&mobile_number=8979832280',
#                         headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})


# api to save reward point to DB
# response = requests.post('http://127.0.0.1:8000/save_reward', data=data,
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})


# api to save reward point discount DB
# response = requests.post('http://127.0.0.1:8000/save_discount_data', data=data,
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})


# api to reward status
# response = requests.get('http://127.0.0.1:8000/get_reward_status?office=nayan&branch=abc&mobile_number=8979832280',
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})


# api to get token
# response = requests.post('http://127.0.0.1:8000/api/token', data={username:username, password:password})

# api to update reward db
# response = requests.post('http://127.0.0.1:8000/update_reward_details', data=data,
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})


# api to update discount db
# response = requests.post('http://127.0.0.1:8000/update_discount_details', data=data,
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})


# api to get customer details based on office and mobile number
# response = requests.post('http://127.0.0.1:8000/get_customer_details_office_mobile?office=office&number=mobile_number,
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})



# api to get customer details based on office and card number
# response = requests.post('http://127.0.0.1:8000/get_customer_details_office_card?office=office&card_number=card_number,
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})



# api to get customer details based on office, mobile and card_number
# response = requests.post('http://127.0.0.1:8000/get_customer_details_office_mobile_card?office=office&mobile_number=mobile_number&card_number=card_number,
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})



#api to update customer details based on office, mob_number
# response = requests.post('    http://127.0.0.1:8000/customer_details_update?office=office&number=number,
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})



#api to get reward status based on office and card
# response = requests.post('http://127.0.0.1:8000/reward_status_for_office_card?office=office&card_number=card_number,
#     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MTM5MzIxLCJpYXQiOjE2NDc2MDMzMjEsImp0aSI6Ijc3MjVlYzJhYzE1MDQ3YWVhMjM2MDE0NGRiNjg0ZDA5IiwidXNlcl9pZCI6MX0.zZ2GWB4BQ4_EWOrEdIlvjZfBQYJvKMWtRkuKNF9JB7M'})

