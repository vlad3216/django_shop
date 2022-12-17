from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


def test_login_user(client, faker):
    email = faker.email()
    password = faker.password()
    phone = faker.phone_number()
    url = reverse('login')
    user = User.objects.create(
        email=email,
        first_name=email,
        phone=phone,
        is_phone_valid=True
    )
    user.set_password(password)
    user.save()
    # get login page
    response = client.get(url)
    assert response.status_code == 200

    data = {
        'password': faker.password()
    }
    # post data to login form
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.context['form'].errors['__all__'][
               0] == 'Email or phone number is required.'

    data['username'] = faker.email()
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.context['form'].errors['__all__'][
               0] == 'Please enter a correct email address and password. Note that both fields may be case-sensitive.'

    del data['username']
    data['phone'] = faker.word()
    data['password'] = password
    response = client.post(url, data=data)
    assert response.status_code == 200

    data['username'] = email
    data['password'] = password
    response = client.post(url, data=data)
    assert response.status_code == 302


def test_registration_user(client, faker):
    url = reverse('registration')

    response = client.get(url)
    assert response.status_code == 200

    email = faker.email()
    password = faker.password()
    phone = faker.phone_number()
    assert not  User.objects.filter(email=email, is_active=False).exists()

    data = {
        'email': email,
        'phone': phone,
        'password1': password,
        'password2': password,
    }

    response = client.post(url, data=data, follow=True)
    assert response.status_code == 200
    breakpoint()
    assert User.objects.filter(email=email).exists()
    assert b"Borgir corporation" in response.content