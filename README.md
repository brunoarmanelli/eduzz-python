
# Unoffical Eduzz Python Module

Eduzz requests made easy.

### Usage
  
````python
import eduzz

eduzz = eduzz.Eduzz(
	email='YOUR_EMAIL',
	public_key='YOUR_PUB_KEY',
	api_key='YOUR_API_KEY'
)
````

and then

````python
response = eduzz.get_sale_list(start_date='2020-01-01', end_date='2020-06-05')
print(response)
````
