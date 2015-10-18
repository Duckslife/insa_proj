import codecs
import yaml
import os

path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),'../settings/settings.yaml')
config = yaml.load(codecs.open(path, 'r'))
post_conn =(config['postgresql']['username'], config['postgresql']['passwd'], config['postgresql']['host'], config['postgresql']['db_name'])

