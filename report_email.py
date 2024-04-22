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

def format_fruit(val1, val2):
  """Given a fruit dictionary, returns a nicely formatted name."""
  print("name: {} weight: {}  {} ".format(val1, val2, " "))
  return "name: {} \r weight: {} \r {} \r".format(val1, val2, " ")

def fruits_dict_to_table(entire_jason_fruit_data):
  """Turns the data in fruit_data into a list of lists."""
  table_data = [[]]
  for fruit in entire_jason_fruit_data:
    # print(type(fruit))
    fruitQ = []
    for feature, value in fruit.items():
      # print(fruitQ)
      # print(feature,value, type(feature), type(fruit))
      if feature == "name":
        fruitQ.append(value)
        # print(fruitQ)
      if feature == "weight":
        fruitQ.append(value)
        # print(fruitQ, fruitQ[0], fruitQ[1])
    table_data.append(format_fruit(fruitQ[0], fruitQ[1]))
  return table_data

# def body__builder(entire_jason_data):
#   superbody = [[]]
#   for item in entire_jason_data:
#     superbody = fruits_dict_to_table(item)
#     # print(item, type(item))
#   return superbody

def main(argv):
  data = load_data("fruit_dico.jason")
  # print(data)
  # body = body__builder(data)
  body = fruits_dict_to_table(data)
  print(body)
  title_report = "Processed Update on {} \r \r".format(datetime.date.today())
  reports.generate_report("/tmp/processed.pdf", title_report, "", body)
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  message = emails.generate(sender, receiver, subject, str(body), "/tmp/processed.pdf")
  print(message)
  # emails.send(message)

if __name__ == "__main__":
  main(sys.argv)