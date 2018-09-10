from html.parser import HTMLParser
import os
import pickle
import MeCab

def wakati(text):
  tagger = MeCab.Tagger("-Owakati")
  return tagger.parse(text).split(' ')

def is_a_jp_noun(word):
  # Not really good...
  MecabMode = '-Ochasen'
  tagger = MeCab.Tagger(MecabMode)
  k = tagger.parse(word)
  return '名詞' in tagger.parse(word)

def only_noun(words):
  return list(filter(lambda x: is_a_jp_noun(x), words))

class MyHTMLParser(HTMLParser):
  title = ''
  buf = ''
  a_flag = False
  rst = []
  cnt = 0
  def handle_starttag(self, tag, attrs):
    if tag == 'doc':
      self.title = dict(attrs)['title']
      self.buf = ''
    if tag == 'a':
      self.a_flag = True

  def handle_endtag(self, tag):
    if tag == 'a':
      self.a_flag = False
    if tag == 'doc':
      words = wakati(self.buf.replace('\n', ''))
      print(words)
      nouns = only_noun(words)
      print(nouns)
      self.rst += nouns
      self.rst += ['\n']
      self.cnt += 1
      print(self.rst)
      if (self.cnt > 4):
        with open('data/t_a', 'a') as f:
          f.write(' ' + ' '.join(self.rst))
        exit()

  def handle_data(self, data):
    self.buf += data

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
