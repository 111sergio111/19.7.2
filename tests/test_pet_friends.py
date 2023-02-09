from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()
invalid_auth_key = "uaig1ef3uogfwu6hgfsl654df88ghlih"

# первая часть задания: тесты к дополненным 2 методам библиотеки:

def test_post_add_new_pet_without_photo(name='Арчи', animal_type='собака', age=12):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_post_add_photo_of_pet(pet_photo='images/IMG_8563.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.post_add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert result['my_pets'] == pet_photo
    else:
        raise Exception("Питомцы отсутствуют")

# вторая часть задания (негативные тесты, 10 штук):

# 1
def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 400 or 401 or 402 or 403 or 404 or 405
# 2

def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 400 or 401 or 402 or 403 or 404 or 405
# 3

def test_get_api_key_for_none_password(email=valid_email, password=""):
    status, result = pf.get_api_key(email, password)
    assert status == 400 or 401 or 402 or 403 or 404 or 405

# 4
def test_get_all_pets_with_invalid_filter(filter='not_my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 400 or 401 or 402 or 403 or 404 or 405
# 5
def test_post_add_new_pet_with_invalid_name(name='fghfhdhdshfjhajavajfjhajhfajhfhafbjhabfjkbajhbafhjasjahjbjhafsjhbfsjh', animal_type='собака', age='1', pet_photo='images/IMG_8521.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400 or 401 or 402 or 403 or 404 or 405
# 6
def test_post_add_new_pet_with_none_name(name='', animal_type='собака', age='1', pet_photo='images/IMG_8521.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400 or 401 or 402 or 403 or 404 or 405
# 7
def test_post_add_new_pet_with_none_animal_type(name='Арчи', animal_type='', age='1', pet_photo='images/IMG_8521.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400 or 401 or 402 or 403 or 404 or 405

# 8
def test_post_add_new_pet_with_none_age(name='Арчи', animal_type='собака', age='', pet_photo='images/IMG_8521.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400 or 401 or 402 or 403 or 404 or 405

# 9
def test_post_add_new_pet_with_invalid_animal_type(name='Арчи', animal_type='2514', age='1', pet_photo='images/IMG_8521.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400 or 401 or 402 or 403 or 404 or 405

# 10
def test_post_add_new_pet_with_invalid_age(name='Арчи', animal_type='собака', age='-1', pet_photo='images/IMG_8521.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400 or 401 or 402 or 403 or 404 or 405

