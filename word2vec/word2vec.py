from gensim.models import word2vec as wv
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import sys

TEXT_DIR = '../data/t_a'
D = 2
LEARN = False
MODEL_DIR = '../data/2d.model'
MODEL = None
LANG = 'jp'

def learn(path):
  sentences = wv.LineSentence(path, limit=500)
  print('Got sentences. Now learning...')
  model = wv.Word2Vec(sentences, size=D)
  for epoch in range(20):
    print(epoch)
    model.train(sentences,
                total_examples=model.corpus_count,
                epochs=model.iter)
    model.alpha -= (0.025 - 0.0001) / 19
    model.min_alpha = model.alpha
  model.save(MODEL_DIR)

def test(MODEL_DIR):
  model = wv.Word2Vec.load(MODEL_DIR)
  for w in model.wv.index2word[:10]:
    print()
    print('word:', w)
    print('simi:', model.wv.most_similar(w))
    print('vec:', model.wv[w])

# learn(TEXT_DIR)
test(MODEL_DIR)
