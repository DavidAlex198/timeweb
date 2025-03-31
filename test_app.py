import pytest
import datetime

from app import app

@pytest.fixture
def client():
    with app.test_client() as app_client:
        yield app_client

# With the app dealing with time, I wanted to make sure that it remained constant to avoid any potential issues
# with calling the test and asserting a different time. Found that the pytest module freezegun works great for that.
def test_time(freezer, client):
	time = datetime.datetime.now()
	response = client.get('/')
	assert response.status_code == 200
	data = time.strftime("%b %d, %Y, %H:%M")
	assert response.data == data.encode()


# Check that the IP address is not being messed with
def test_ip(client):
#	response = client.get('/')
#	assert response.remote_addr == '10.92.21.104'
	pass
# Check for an apppropriate response code given after being passed a bad route
def test_not_found(client):
	response = client.get('/nothingtoseehere')
	assert response.status_code == 404

# Check that the app is giving correct data after a couple calls.
def test_multiple_calls(client, freezer):
	pass
