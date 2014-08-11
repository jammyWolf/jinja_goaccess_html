#coding:utf8
import os
from global_path import goaccess_service, service_list
from fabric.api import env, task, parallel, local, run, cd, settings, roles

env.roledefs = {
        'test':
            [
                "10.10.10.10",
            ],
        }

#global varibles
NGINX_LOG_PATH = '/data/log/nginx/'
TMP_JSON_PATH = '/tmp/nginx_json_log/'
DIRNAME = os.path.abspath(os.path.dirname(__file__)).replace('\\','/')
LOCAL_JSON_PATH = os.path.join(DIRNAME, 'nginx_json_log')
PROCESS_NAME = "create_rendered.py"
env.user = "root"

@task
@parallel
def json(log_list):
    run('mkdir -p %s' %(TMP_JSON_PATH))
    for each in log_list:
        run('goaccess -f %s -o json > %s' %( os.path.join(NGINX_LOG_PATH, goaccess_service[each]), os.path.join(TMP_JSON_PATH, each+'.json')))
    exclude_file =  """ --exclude="*.pyc" --exclude="*.*~" --exclude="*.log*"  --exclude="sweeper.sh" --exclude=".*.swp" --exclude="HEARTBEAT" --exclude="fabfile.py" """
    local('&&'.join([
        'rsync -rv %s:%s %s %s' % ( env.host, TMP_JSON_PATH, LOCAL_JSON_PATH, exclude_file),
        ]))

@task
@parallel
def mail(log_list):
    cd(DIRNAME)
    for each in log_list:
        local('&&'.join([
            'python %s %s' %(PROCESS_NAME, each),
            ]))

@task
@parallel
def deploy(service=None):
    if service: 
        log_list = [service]
    else:
        log_list = service_list
    json(log_list)
    mail(log_list)

