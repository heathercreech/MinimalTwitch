from datetime import date

from .api import GiantBombAPI


api = GiantBombAPI("game")
id_base = "3030"

def release_date(id_unique, **params):
	call_data = api.call("{0}-{1}".format(id_base, id_unique), field_list="expected_release_year,expected_release_month,expected_release_day", **params)
	
	r_year	= call_data["expected_release_year"]
	r_month	= call_data["expected_release_month"]
	r_day	= call_data["expected_release_day"]
	
	if r_year and r_month and r_day:
		return date(r_year, r_month, r_day)