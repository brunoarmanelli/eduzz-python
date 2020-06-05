import requests

class Eduzz:
	def __init__(self, email, public_key, api_key):
		self.email = email
		self.public_key = public_key
		self.api_key = api_key

	def get_token(self):
		method_url = 'https://api2.eduzz.com/credential/generate_token'
		payload = {'email': self.email, 'publickey': self.public_key, 'apikey' : self.api_key}

		try:
			r = requests.post(url = method_url, params = payload)
			data = r.json()
			return data.get('data', None).get('token', None)
		except:
			return None
		
	def get_sale_list(self, start_date, end_date, page = None, contract_id=None, affiliate_id=None,
					content_id=None, invoice_status=None, client_email=None,
					client_document=None, date_type=None):

		method_url = 'https://api2.eduzz.com/sale/get_sale_list'
		headers = {'token': self.get_token()}
		payload = {'start_date': start_date, 'end_date': end_date}
		
		if page:
			payload['page'] = page
		if contract_id:
			payload['contract_id'] = contract_id
		if affiliate_id:
			payload['affiliate_id'] = affiliate_id
		if content_id:
			payload['content_id'] = content_id
		if invoice_status:
			payload['invoice_status'] = invoice_status
		if client_email:
			payload['client_email'] = client_email
		if client_document:
			payload['client_document'] = client_document
		if date_type:
			payload['date_type'] = date_type
		
		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None