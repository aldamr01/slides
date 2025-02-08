from opensearchpy import OpenSearch

host = 'https://vpc-opensearchopens-gkzcvvmfqgvm-7f2ehag5tjzugijlonkjttb3re.ap-southeast-1.es.amazonaws.com'
port = 9200
passwd = "WAHOf\\3>Jv{kU94yKOH5T}Vwdh=9^-|\\"
auth = ('idnadmin', passwd) # For testing only. Don't store credentials in code.


# Create the client with SSL/TLS and hostname verification disabled.
client = OpenSearch(
    hosts = host,
    http_compress = True, # enables gzip compression for request bodies
    http_auth = auth,
    use_ssl = False,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False
)

q = 'Voluptates'
query = {
  'size': 5,
  'query': {
    'multi_match': {
      'query': q,
      'fields': ['title^2', 'description']
    }
  }
}

response = client.search(
    body = query,
    index = 'aldion-articles'
)

if "hits" in response and "hits" in response["hits"]:
    results = response["hits"]["hits"]
    if results:
        print(f"🔎 Found {len(results)} articles:")
        for hit in results:
            title = hit["_source"].get("title", "Untitled")
            description = hit["_source"].get("description", "No description available")
            score = hit.get("_score", 0)
            print(f"📌 [{score:.2f}] {title}: {description}")
    else:
        print("❌ No articles found.")
else:
    print("⚠️ Unexpected response format:", response)

