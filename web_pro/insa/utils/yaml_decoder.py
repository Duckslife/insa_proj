import codecs
import yaml
import os

path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),'../settings/settings.yaml')
config = yaml.load(codecs.open(path, 'r'))
post_conn =(config['postlocal']['username'], config['postlocal']['passwd'], config['postlocal']['host'], config['postlocal']['db_name'])

