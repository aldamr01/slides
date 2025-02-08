from fastapi import FastAPI
from os_client import connect
from models.article import Article

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search")
def search(keyword: str, size: int = 100):
    connect()
    
    query = (
        Article.search(using="default")
        .query("bool", 
            must=[
                {"exists": {"field": "description"}},
                {"exists": {"field": "title"}},
                {
                    "multi_match": {
                        "query": keyword,
                        "fields": ["title^2", "description"],
                        "type": "best_fields"
                    }
                }
            ],
            filter=[
                {"terms": {"tags.slug": ["viral", "polisi"]}}
            ]
        )
        .sort({"_score": {"order": "desc"}})
        .extra(size=size)
    )
    
    response = query.execute()

    results = [
        {
            "title": hit.title,
            "description": hit.description,
            "score": hit.meta.score
        }
        for hit in response
    ]
        
    return {
        "success": True,
        "total": response.hits.total.value,
        "results": results
    }