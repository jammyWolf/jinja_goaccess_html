#encoding:utf-8
import os

JSON_LOG_PATH = os.path.join(os.path.dirname(__file__), 'nginx_json_log')
HTML_LOG_PATH = os.path.join(os.path.dirname(__file__), 'nginx_html_log')

mailto_list=["XXX@qiyi.com"] #receiver
mail_host='mail.companyname.com:port'
mail_user="your_name" 
mail_pass="your_password"
mail_postfix="host_postfix"

service_list = [ 'log_1', 'log_2', 'log_3', 'log_4']
goaccess_service ={
        'log_1':'log_1_real_log_name', 
        'log_2':'log_2_real_log_name', 
        'log_3':'log_3_real_log_name', 
        'log_4':'log_4_real_log_name', 
        }

