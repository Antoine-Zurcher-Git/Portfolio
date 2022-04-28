# regularite-TER.py
# Correpond au corrigé du dernier exercice du TD3+4 (TD3-s7.py)

import http.server
import socketserver
from urllib.parse import urlparse, parse_qs, unquote
import json

import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as pltd

import sqlite3

PORT = 8080

#
# Définition du nouveau handler
#
class RequestHandler(http.server.SimpleHTTPRequestHandler):

  static_dir=''

  def do_GET(self):

    self.init_params()
    if self.path_info[0] == 'cv':
      self.send_cv()
    else:
      self.send_static()
  
  def do_HEAD(self):
    self.send_static()

  def send_static(self):

    self.path = self.static_dir+self.path

    if (self.command=='HEAD'):
        http.server.SimpleHTTPRequestHandler.do_HEAD(self)
    else:
        http.server.SimpleHTTPRequestHandler.do_GET(self)

  def init_params(self):
    # analyse de l'adresse
    info = urlparse(self.path)
    self.path_info = [unquote(v) for v in info.path.split('/')[1:]]  # info.path.split('/')[1:]
    self.query_string = info.query
    self.params = parse_qs(info.query)

    # récupération du corps
    length = self.headers.get('Content-Length')
    ctype = self.headers.get('Content-Type')
    if length:
      self.body = str(self.rfile.read(int(length)),'utf-8')
      if ctype == 'application/x-www-form-urlencoded' : 
        self.params = parse_qs(self.body)
    else:
      self.body = ''
   
    # traces
    # print('info_path =',self.path_info)
    # print('body =',length,ctype,self.body)
    # print('params =', self.params)
 
  def send_cv(self):
    headers = [('Content-Type','text/html;charset=utf-8')]
    html = '<!DOCTYPE html><title>{}</title><link rel="stylesheet" type="text/css" href="css/style.css"/><meta charset="utf-8">{}' \
      .format(self.path_info[0],'<embed style="width:100% height: 100%; margin:0;" type="application/pdf" src="cv.pdf" background-color="4283586137" javascript="allow" full-frame pdf-viewer-update-enabled>')#<iframe class="pdf" src="resources/contact/CV_Antoine_Zurcher.pdf">
    self.send(html,headers)

  def send(self,body,headers=[]):
    encoded = bytes(body, 'UTF-8')

    self.send_response(200)

    [self.send_header(*t) for t in headers]
    self.send_header('Content-Length',int(len(encoded)))
    self.end_headers()

    self.wfile.write(encoded)
  
#
# Instanciation et lancement du serveur
#
httpd = socketserver.TCPServer(("", PORT), RequestHandler)
print ("serveur sur port : {}".format(PORT))
httpd.serve_forever()

