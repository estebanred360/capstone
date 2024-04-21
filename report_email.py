#!/usr/bin/env python3

import json
import emails
import os, sys
import datetime 
import reports

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data

def format_fruit(fruit):
  """Given a fruit dictionary, returns a nicely formatted name."""
  return "name: {}\rweight: {}\r {}\r".format(fruit[1], fruit[2], "")

def fruits_dict_to_table(fruit_data):
  """Turns the data in fruit_data into a list of lists."""
  table_data = []
  for item in fruit_data:
    table_data.append([format_fruit(item[1]), item[2]])
  return table_data

def body__builder(entire_jason_data):
  superbody = [[]]
  for item in entire_jason_data:
    superbody = fruits_dict_to_table(item)
  print(superbody)
  return superbody

def main(argv):
  data = load_data("fruit_dico.jason")
  print(data)
  body = body__builder(data)
  title_report = "Processed Update on {}\r\r".format(datetime.date.today())
  reports.generate_report("/tmp/processed.pdf", title_report, "", body)
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)