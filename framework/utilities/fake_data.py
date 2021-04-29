from faker import Faker


fake = Faker()


def generate_fake_user() -> dict:
    """Generates fake user in a form of dictionary"""
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.ascii_free_email()
    address_street = fake.street_address()
    address_city = fake.city()
    address_postcode = fake.postcode()
    address_state = fake.state()
    address_country = fake.country()

    payload = {
      "email": email,
      "first_name": first_name,
      "last_name": last_name,
      "username": fake.user_name(),
      "billing": {
        "first_name": first_name,
        "last_name": last_name,
        "company": "",
        "address_1": address_street,
        "address_2": "",
        "city": address_city,
        "state": address_state,
        "postcode": address_postcode,
        "country": address_country,
        "email": email,
        "phone": fake.phone_number()
      },
      "shipping": {
        "first_name": first_name,
        "last_name": last_name,
        "company": "",
        "address_1": address_street,
        "address_2": "",
        "city": address_city,
        "state": address_state,
        "postcode": address_postcode,
        "country": address_country
      }
    }
    return payload


def generate_filename(extension: str = None) -> str:
    filename = fake.file_name(extension=extension)
    return filename.replace('.', f'{fake.date()}.')
