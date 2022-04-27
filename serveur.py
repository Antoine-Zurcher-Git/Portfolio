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

  # sous-répertoire racine des documents statiques
  static_dir = ''

  #
  # On surcharge la méthode qui traite les requêtes GET
  #
  # def do_GET(self):

  #   # On récupère les étapes du chemin d'accès
  #   self.send_static()

  #
  # On surcharge la méthode qui traite les requêtes HEAD
  #
  # def do_HEAD(self):
  #   self.send_static()

  #
  # On envoie le document statique demandé
  #
  # def send_static(self):

  #   # on modifie le chemin d'accès en insérant un répertoire préfixe
  #   self.path = self.static_dir + self.path

  #   # on appelle la méthode parent (do_GET ou do_HEAD)
  #   # à partir du verbe HTTP (GET ou HEAD)
  #   if (self.command=='HEAD'):
  #       http.server.SimpleHTTPRequestHandler.do_HEAD(self)
  #   else:
  #       http.server.SimpleHTTPRequestHandler.do_GET(self)
      
    
  #
  # On envoie les entêtes et le corps fourni
  #
  # def send(self,body,headers=[]):

  #   # on encode la chaine de caractères à envoyer
  #   encoded = bytes(body, 'UTF-8')

  #   # on envoie la ligne de statut
  #   self.send_response(200)

  #   # on envoie les lignes d'entête et la ligne vide
  #   [self.send_header(*t) for t in headers]
  #   self.send_header('Content-Length',int(len(encoded)))
  #   self.end_headers()

  #   # on envoie le corps de la réponse
  #   self.wfile.write(encoded)

 
#
# Instanciation et lancement du serveur
#
httpd = socketserver.TCPServer(("", PORT), RequestHandler)
print ("serveur sur port : {}".format(PORT))
httpd.serve_forever()

