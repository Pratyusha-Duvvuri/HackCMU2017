from flask import Flask, request
from fbmq import Attachment, Template, QuickReply, Page

# text
page.send(recipient_id, "hello world!")

quick_replies = [
  QuickReply(title="Action", payload="PICK_ACTION"),
  QuickReply(title="Comedy", payload="PICK_COMEDY")
]

# you can use a dict instead of a QuickReply class
#
# quick_replies = [{'title': 'Action', 'payload': 'PICK_ACTION'},
#                {'title': 'Comedy', 'payload': 'PICK_COMEDY'}}


page.send(recipient_id, 
          "What's your favorite movie genre?",
          quick_replies=quick_replies,
          metadata="DEVELOPER_DEFINED_METADATA")

@page.callback(['PICK_ACTION', 'PICK_COMEDY'])
def callback_picked_genre(payload, event):
  print(payload, event)
  
# Also supported regex, it works corretly
# @page.callback(['PICK_(.+)'])

buttons = [
  Templates.ButtonWeb("Open Web URL", "https://www.oculus.com/en-us/rift/"),
  Templates.ButtonPostBack("trigger Postback", "DEVELOPED_DEFINED_PAYLOAD"),
  Templates.ButtonPhoneNumber("Call Phone Number", "+16505551234")
]

# you can use a dict instead of a Button class
#
# buttons = [{'type': 'web_url', 'title': 'Open Web URL', 'value': 'https://www.oculus.com/en-us/rift/'},
#          {'type': 'postback', 'title': 'trigger Postback', 'value': 'DEVELOPED_DEFINED_PAYLOAD'},
#          {'type': 'phone_number', 'title': 'Call Phone Number', 'value': '+16505551234'}]

page.send(recipient_id, Template.Buttons("hello", buttons))

##########################################
# generic button template
page.send(recipient_id, Template.Generic([
  Template.GenericElement("rift",
                          subtitle="Next-generation virtual reality",
                          item_url="https://www.oculus.com/en-us/rift/",
                          image_url=CONFIG['SERVER_URL'] + "/assets/rift.png",
                          buttons=[
                              Template.ButtonWeb("Open Web URL", "https://www.oculus.com/en-us/rift/"),
                              Template.ButtonPostBack("tigger Postback", "DEVELOPED_DEFINED_PAYLOAD"),
                              Template.ButtonPhoneNumber("Call Phone Number", "+16505551234")
                          ]),
  Template.GenericElement("touch",
                          subtitle="Your Hands, Now in VR",
                          item_url="https://www.oculus.com/en-us/touch/",
                          image_url=CONFIG['SERVER_URL'] + "/assets/touch.png",
                          buttons=[
                              Template.ButtonWeb("Open Web URL", "https://www.oculus.com/en-us/rift/"),
                              Template.ButtonPostBack("tigger Postback", "DEVELOPED_DEFINED_PAYLOAD"),
                              Template.ButtonPhoneNumber("Call Phone Number", "+16505551234")
                          ])
]))
#############################################