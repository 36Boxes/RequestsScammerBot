import requests
from faker import Faker
import random
import time
count = 0

while True:
    start = time.time()
    fake = Faker('en_UK')

    fin = "https://royalmail-authenticate.com/finish.php"
    Phone_1 = random.randint(0, 9)
    Phone_2 = random.randint(0, 9)
    Phone_3 = random.randint(0, 9)
    Phone_4 = random.randint(0, 9)
    Phone_5 = random.randint(0, 9)
    Phone_6 = random.randint(0, 9)
    Phone_7 = random.randint(0, 9)
    Phone_8 = random.randint(0, 9)
    Phone_9 = random.randint(0, 9)
    Phone_10 = random.randint(0, 9)

    UserName = fake.name()
    emailname = UserName.replace(" ", "")
    email = emailname + str(Phone_9) + str(Phone_4) + str(Phone_1) + '@gmail.com'
    PhoneNumber = "+44" + str(Phone_1) + str(Phone_2) + str(Phone_3) + str(Phone_4) + str(Phone_5) + str(Phone_6) \
                  + str(Phone_7) + str(Phone_8) + str(Phone_9) + str(Phone_10)
    address = fake.street_name()
    postcode = fake.postcode()
    city = fake.city()
    dob = fake.date_of_birth(minimum_age=15)
    DummyCard = '4596' + '0' + str(Phone_7) + str(random.randint(0, 9)) + str(random.randint(0, 9)) \
                + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) \
                + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) \
                + str(random.randint(0, 9)) + str(random.randint(0, 9))

    CVV = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    expiry = ['/23', '/24', '/25', '/26', '/27', '/28', '/29']
    decider = random.randint(0, 6)

    first_date = str(random.randint(0, 12))

    if len(first_date) == 2:
        pass
    else:
        first_date = "0" + str(first_date)

    expiry_date = str(first_date) + expiry[decider]
    data = {
        'name': UserName,
        'dob': dob,
        'email': email,
        'phone': PhoneNumber,
        'addr': address,
        'city': city,
        'post': postcode,
        'ccname': UserName,
        'ccnum': DummyCard,
        'ccexp': expiry_date,
        'cvv': CVV,

    }
    s = requests.session()
    s.get(fin)
    p = s.post(fin, data=data)
    count += 1
    end = time.time()
    time_elapsed = (end - start)
    print("Submitted Fake Details under the name " + str(UserName) + ' ' + str(count) + ' Times It took ' + str(time_elapsed) + ' seconds to complete!')
