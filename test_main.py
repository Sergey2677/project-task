import requests

valid_paths_with_all_fields = [
    ({
         "field_name_1": "easfklsad@gmail.com",
         "field_name_2": "+79022452422",
         "field_name_3": "Hello how are you?",
         "field_name_4": "I`m fine, thanks",
     }, "First test template"),
    ({
         "user_email": "test@mail.ru",
         "user_phone": "+79052423431",
         "user_name": "Sergey",
         "order_date": "10.01.2023"
     }, "Second test template"),
    ({
         "customer_email": "jkdalf2120@icloud.com",
         "customer_phone": "+79318432232",
         "customer_name": "blablabla",
         "purchase_date": "25.01.2022"
     }, "Third test template"),
    ({
         "manager_email": "pwoqeprod@yandex.ru",
         "manager_phone": "+79391492134",
         "manager_name": "Albina",
         "description": "Test text",
         "last_entrance": "2000-12-12"
     }, "Fourth test template"),
]

valid_paths_not_all_fields = [
    ({
         "field_name_3": "Hello how are you?",
         "field_name_4": "I`m fine, thanks",
     }, "First test template"),
    ({
         "user_email": "test@mail.ru",
         "user_phone": "+79052423431",
     }, "Second test template"),
    ({
         "customer_email": "jkdalf2120@icloud.com",
         "customer_name": "blablabla",
         "purchase_date": "25.01.2022"
     }, "Third test template"),
    ({
         "manager_email": "pwoqeprod@yandex.ru",
         "manager_phone": "+79391492134",
         "last_entrance": "2000-12-12"
     }, "Fourth test template"),
]

invalid_pathes = [
    ({
         'field1': 'sadfsf',
         'field2': '+790523422332',
         'field3': '001.2031.0202',
     }, 'test1'),
    ({
         'field5': 'saldka@laskdla.ro',
         'field6': '+7905sada2332',
         'field7': '202.1.21',
     }, 'test2'),
    ({
         'field8': 'asdfs@askdks.or',
         'field9': '+79054424242',
         'field0': '2022-20-02',
     }, 'test3'),

]


def test_post_request_with_valid_pathes_and_all_field():
    for path in valid_paths_with_all_fields:
        valid_path = ('&').join([f'{key}={value}' for key, value in path[0].items()])
        response = requests.post(f"http://localhost:8000/get_form/{valid_path}")
        assert response.json() == path[1]



def test_post_request_with_valid_not_all_field():
    for path in valid_paths_not_all_fields:
        valid_path = ('&').join([f'{key}={value}' for key, value in path[0].items()])
        response = requests.post(f"http://localhost:8000/get_form/{valid_path}")
        assert response.json() == path[1]



def test_post_request_with_invalid_pathes():
    for path in invalid_pathes:
        valid_path = ('&').join([f'{key}={value}' for key, value in path[0].items()])
        response = requests.post(f"http://localhost:8000/get_form/{valid_path}")
        assert response.json() != path[1]



test_post_request_with_valid_pathes_and_all_field()
test_post_request_with_valid_not_all_field()
test_post_request_with_invalid_pathes()
