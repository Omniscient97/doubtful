
class ConfigurationLoader(object):
	def __init__(self, version):

		# nosetests uses python2.7 so it needs ti use the ConfigParser module instead of the configparser.
		# TODO: make nosetests use python3 so this hack can be avoided

		if version == '3':
			import configparser
			class MyConfigParser(configparser.ConfigParser):
				def getlist(self,section,option):

					value = self.get(section,option)
					return list(filter(None, (x.strip() for x in value.splitlines())))
		if version == '2':
			import ConfigParser
			class MyConfigParser(ConfigParser.ConfigParser):
				def getlist(self,section,option):
					value = self.get(section,option)
					return list(filter(None, (x.strip() for x in value.splitlines())))


		self.config = MyConfigParser()

	def load(self, target):
		self.config.read(target)

	def sections(self):
		return self.config.sections()

	def options(self, section):
		return self.config.options(section)

	def get(self, section, option):
		return self.config.get(section, option)

	def getlist(self, section, option):
		return self.config.getlist(section, option)
