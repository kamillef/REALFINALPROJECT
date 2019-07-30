# import webapp2
#
# from google.appengine.ext import ndb
#
# class CssiUser(ndb.Model):
#   first_name = ndb.StringProperty()
#   last_name = ndb.StringProperty()
#   email = ndb.StringProperty()

from google.appengine.ext import ndb

class UserDataStore(ndb.Model):
    username = ndb.StringProperty()
    psw = ndb.StringProperty()


class MessageDataStore(ndb.Model):
    CurrentStatus = ndb.StringProperty()
    StatusTime = ndb.DateTimeProperty(auto_now_add=True)
