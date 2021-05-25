# task_varo

test_server module used to run tests with pytest

run pytest test_server.py

or you can run each test by specifing the test after :: 
e.g pytest --capture=no test_server.py::test_get_object_by_id


Before each test a fixture run to get a valid token from server


## Tests

I created several tests for each api

Get - 

1. valid 200 response check - API is alive and can return answer 
2. number of object returns match the existing number

Post - 

  1. valid 200 response check - API is alive and can  return answer 
  2. object saved correctly - API save the data in the right manner with correct values
  3. Bad request - API can handle bad input and return indication of the issue

Get by id - 

  1. valid 200 response check - API is alive and can return answer 


Delete - 

  1. valid 204 response check - API is alive and can return answer 
  2. negative test - try to delete resource which not exists and expect to get correct indication




# bugs found

delete does not return 204 if succeed

when deleting not existing object the API returns 200 instead of 404 (or some other error response code)
