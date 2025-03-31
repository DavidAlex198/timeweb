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

# Check for an apppropriate response code given after being passed a bad route
def test_not_found(client):
	response = client.get('/nothingtoseehere')
	assert response.status_code == 404

# Check that the app is giving correct data after a couple calls.
def test_multiple_calls(client, freezer):
	time1 = datetime.datetime.now()
	response1 = client.get('/')
	time1.strftime("%b %d, %Y, %H:%M")
# assert that the response is expected, similar to test_time
	assert response1.data == (time1.strftime("%b %d, %Y, %H:%M")).encode()
# then we move time forward 5 minutes
	freezer.tick(datetime.timedelta(minutes=5))
	time2 = datetime.datetime.now()
	# assert that the two times are not equal
	assert time1 != time2
	response2 = client.get('/')
	# and finally assert that the two responses do not have the same data
	assert response1.data != response2.data
