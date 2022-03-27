"""gensim を動かすサンプル"""

from pathlib import Path

import MeCab
from gensim.models.doc2vec import Doc2Vec

model_path = Path(__file__).parent / "synchro.model"
model = Doc2Vec.load(str(model_path.resolve()))

tagger = MeCab.Tagger('-Owakati')


def wakati(text):
    """分かち書きをおこなう"""
    wakati_result = []
    text = str(text).lower()
    node = tagger.parseToNode(text)
    while node:
        if (not node.feature.startswith("BOS/EOS")) and (not node.feature.startswith("助詞")) and (not node.feature.startswith("助動詞")):
            wakati_result.append(node.surface)
        node = node.next
    return " ".join(wakati_result)


TEST_DOC = "最高な気分だ"
test_docvec = model.infer_vector(wakati(TEST_DOC))

result = model.docvecs.most_similar([test_docvec])

print(result)
