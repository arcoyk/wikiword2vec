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

def path2dir(path):
  return '/'.join(path)

def create_title2link():
  parser = MyHTMLParser()
  root_path = ['data', 'pages']
  for d in os.listdir(path2dir(root_path)):
    if '.DS_Store' == d:
      continue
    page_path = root_path + [d]
    for f in os.listdir(path2dir(page_path)):
      if '.DS_Store' == f:
        continue
      file_path = page_path + [f]
      print(file_path)
      with open(path2dir(file_path)) as f:
        parser.feed(f.read())

def clear_file():
  with open('data/t_a', 'w') as f:
    f.write('')

clear_file()
create_title2link()
