select
	customer_key
	, full_name
	, date_of_birth
	, date_diff('year', date_of_birth, '{report_date}') as age
	, marital_status
	, gender
	, yearly_income
	, number_of_children
	, occupation
	, house_owner_flag
	, number_cars_owned
	, first_purchase_date
	, date_diff('year', first_purchase_date, '{report_date}') as duration
from customers
where
	first_purchase_date <= '{report_date}'