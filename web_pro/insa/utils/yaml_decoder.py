import codecs
import yaml

config = yaml.load(codecs.open('../settings/settings.yaml', 'r'))
post_conn =(config['postgresql']['username'], config['postgresql']['passwd'], config['postgresql']['host'], config['postgresql']['db_name'])



