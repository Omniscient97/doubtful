import configparser

class MyConfigParser(configparser.ConfigParser):
    def getlist(self,section,option):
        value = self.get(section,option)
        return list(filter(None, (x.strip() for x in value.splitlines())))

class ConfigurationLoader(object):
	def __init__(self):
		self.config = MyConfigParser()

	def load(self):
		self.config.read('doubtful/example.config')