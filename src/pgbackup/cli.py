from argparse import ArgumentParser, Action

class DriverAction(Action):
	def __call__(self, parser, namespace, values, option_string=None):
		driver, destination=values
		if driver.lower()!= "s3" and driver.lower()!="local":
			parser.error("Unknown driver. Available drivers are 'local' & 's3'")

		namespace.driver=driver.lower()
		namespace.destination=destination
		

def create_parser():
	parser=ArgumentParser(description="Back up PostgreSQL database locally or to AWS S3")
	parser.add_argument("url", help="url for database to backup")
	parser.add_argument("--driver", "-d", nargs=2, required=True, action=DriverAction, help="where and how to store the backup")
	return parser




