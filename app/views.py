# Create your views here.
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('a', 'conf'))
template = env.get_template('heartbeat.conf')
print template.render(ACTIVEMQ_OUT_QUEUE_NAME="/queue/test_jinja2", ACTIVEMQ_USER="jammy" )
