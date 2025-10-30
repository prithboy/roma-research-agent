from roma import tool
import arxiv

@tool("search_arxiv", description="Searches arXiv for research papers.")
def search_arxiv(query: str, max_results: int = 3):
    results = []
    search = arxiv.Search(query=query, max_results=max_results)
    for r in search.results():
        results.append({
            "title": r.title,
            "summary": r.summary,
            "authors": [a.name for a in r.authors],
            "pdf_url": r.pdf_url,
        })
    return results
