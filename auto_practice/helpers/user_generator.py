from faker import Faker
from auto_practice.helpers.user import User


def make_user() -> User:
    genders = ['male', 'female', 'other']
    faker = Faker('En')
    user = User(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        gender=faker.word(ext_word_list = genders),
        current_address=faker.address(),
        mobile=faker.msisdn()[0:10],
        subject='English',
        dob=faker.date_of_birth(minimum_age = 18, maximum_age = 90)
    )
    return user
