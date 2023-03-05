from API_testing.Requests_folder.delete_order import delete_order
from API_testing.Requests_folder.submit_order import submit_order


class TestDeleteOrder:
		def test_delete_order(self):
			response = delete_order(submit_order(1,"Maria Anton").json()['orderId'])
			assert response.status_code == 204, f'Error expected 204, actual {response}'
			assert response.json()==""