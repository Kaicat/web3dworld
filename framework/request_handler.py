class RequestHandler:
	def __init__(self, app):
		self.app = app

	def GET(self, *args, **kwargs):
		return "404"

	def POST(self, *args, **kwargs):
		return "404"

	def HEAD(self, *args, **kwargs):
		return "404"

	def DELETE(self, *args, **kwargs):
		return "404"

	def OPTIONS(self, *args, **kwargs):
		return "404"
