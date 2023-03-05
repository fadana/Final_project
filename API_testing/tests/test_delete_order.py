from API_testing.Requests_folder.delete_order import delete_order
from API_testing.Requests_folder.submit_order import submit_order


class TestDeleteOrder:
		def test_delete_order(self):
			order_response = submit_order(2, "Maria Anton").json()
			assert len(order_response['orderId']) > 0, f" {order_response}"
			response = delete_order(submit_order(2,"Maria Anton").json())
			assert response.status_code == 204, f'Error expected 204, actual {response}'
			assert response.json()==""