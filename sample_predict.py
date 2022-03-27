"""
推論を行う関数を入れるモジュール
"""
from pathlib import Path

import MeCab
from gensim.models.doc2vec import Doc2Vec

model_path = Path(__file__).parent / "synchro.model"
model: Doc2Vec = Doc2Vec.load(str(model_path.resolve()))

tagger = MeCab.Tagger('-Owakati')


def _wakati(text):
    """分かち書きをおこなう"""
    result = []
    text = str(text).lower()
    node = tagger.parseToNode(text)
    while node:
        if (
                (not node.feature.startswith("BOS/EOS"))
                and (not node.feature.startswith("助詞"))
                and (not node.feature.startswith("助動詞"))
        ):
            result.append(node.surface)
        node = node.next
    return " ".join(result)


def sample_predict(keyword: str) -> list[tuple[str, float]]:
    """入力（キーワード）に応じて、類似している曲を返す"""
    keyword_vec = model.infer_vector(_wakati(keyword))
    return model.docvecs.most_similar([keyword_vec])
