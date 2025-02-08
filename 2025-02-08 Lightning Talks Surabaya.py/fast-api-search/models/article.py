from opensearch_dsl import Document, Text, Keyword

class Article(Document):
    title = Text(fields={'raw': Keyword()})
    description = Text()

    class Index:
        name = "article_index"

    def save(self, ** kwargs):
        return super(Article, self).save(** kwargs)
    
    

