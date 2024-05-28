from googlesearch import search
from pytrends.request import TrendReq

class KeywordResearch:
    def __init__(self):
        pass

    def search_keywords(self, query, num_results=10):
        keywords = []
        # Using list comprehension to limit the number of search results
        results = list(search(query, num=num_results))
        for result in results:
            keywords.append(result)
        return keywords

    def analyze_trends(self, keyword):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=[keyword])
        interest_over_time_df = pytrend.interest_over_time()
        return interest_over_time_df

class SEOStrategy:
    def __init__(self):
        self.keyword_research = KeywordResearch()

    def automate_keyword_research(self, query, num_results=10):
        keywords = self.keyword_research.search_keywords(query, num_results)
        for keyword in keywords:
            trend_data = self.keyword_research.analyze_trends(keyword)
            # Placeholder for analysis and insights generation
            print("Keyword:", keyword)
            print("Trend Data:", trend_data)

# Example usage:
if __name__ == "__main__":
    seo_strategy = SEOStrategy()
    query = "digital marketing"
    seo_strategy.automate_keyword_research(query)
