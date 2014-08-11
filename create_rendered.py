# Create your views here.
#encoding: utf-8 
import os
import sys
import json
from global_path import JSON_LOG_PATH, HTML_LOG_PATH, service_list
from jinja2 import Environment, PackageLoader, Template 
from send_mail import send_mail
from global_path import mailto_list

class CreateHtml(object):
    def __init__(self, arg_dict, service):
        self.create_dict = arg_dict
        self.service = service
        self.env = Environment(loader=PackageLoader('app', 'template'))

    def get_template(self):
        template = self.env.get_template('template.html')
        return template

    def get_rendered(self):
        template = self.get_template()
        output = template.render(table_list = self.create_dict, service =self.service)
        return output

    def save_html(self, fp_path=None):
        result_html = self.get_rendered()
        fp = open(fp_path, "wb+")
        fp.write(result_html)
        fp.close()

def main(argv):
    if len(argv) == 1:
        log_list = service_list
    else:
        log_list = [argv[1]]
    for each in log_list:
        fp = open(os.path.join(JSON_LOG_PATH, each + ".json"))
        json_content = json.loads(fp.read())
        c = CreateHtml(json_content, each)
        c.get_template()
        c.get_rendered()
        c.save_html(os.path.join(HTML_LOG_PATH, each+'.html'))
    #send_mail
    print log_list
    for each in log_list:
        fp = open(os.path.join(HTML_LOG_PATH, each+'.html'),"r")
        content = fp.read()
        fp.close()
        if send_mail(mailto_list, "GoAccess Nginx", each, content):
            print "Mail Send Successed!"
        else:
            print "Mail Send Failed!"

if __name__ == '__main__':
    argv = sys.argv
    main(argv)
