from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
  buf = []
  title = ''
  a_flag = False
  def handle_starttag(self, tag, attrs):
    if tag == 'doc':
      self.title = dict(attrs)['title']
    if tag == 'a':
      self.a_flag = True

  def handle_endtag(self, tag):
    self.a_flag = False

  def handle_data(self, data):
    if self.a_flag:
      self.buf.append(self.title + ' ' + data)
      if len(self.buf) > 1000:
        with open('data/t_a', 'a') as f:
          f.write('\n'.join(self.buf))
      print(self.title, data)

def create_title2link():
  parser = MyHTMLParser()
  root = 'data/AA'
  for filename in os.listdir(root): 
    path = '/'.join([root, filename])
    with open(path) as f:
      parser.feed(f.read())

def clear_file():
  with open('data/t_a', 'w') as f:
    f.write('')

clear_file()
create_title2link()
