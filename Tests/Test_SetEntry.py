import sugarcrm
import unittest

class TestSetEntry(unittest.TestCase):

	hostname = "http://ruttanvm.cs.kent.edu:4080/service/v2/rest.php"
	login = "class"
	password = "class123"
	module = "Contacts"
	query = [{'name': 'first_name', 'value': 'Jim'},
		{'name': 'last_name', 'value': 'Ball'},
		{'name': 'title', 'value': 'CEO'}]
		
	linkName = [{'name': 'email_addresses', 'value': ['id', 'email_address']}]
	selectFields = ['first_name', 'last_name', 'title']
    
	def test_set_entry(self):
		response = sugarcrm.Sugarcrm(self.hostname, self.login, self.password)
		result = response.set_entry(self.module, self.query)
		self.assertIsNotNone(result)
		checkForEntry = response.get_entry(self.module, result['id'], self.selectFields, self.linkName)
		self.assertIsNotNone(checkForEntry)
		
if __name__ == '__main__':
    unittest.main()