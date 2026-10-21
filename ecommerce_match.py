import math

class Matchmaker:
    def __init__(self):
        # Sample product database with category tags
        self.products = [
            {"id": 1, "name": "Wireless Headphones", "tags": ["tech", "music", "portable"]},
            {"id": 2, "name": "Running Shoes", "tags": ["fitness", "outdoor", "shoes"]},
            {"id": 3, "name": "Coffee Maker", "tags": ["home", "kitchen", "morning"]},
            {"id": 4, "name": "Smart Watch", "tags": ["tech", "fitness", "portable"]}
        ]

    def calculate_score(self, user_prefs, product_tags):
        # Simple intersection to find matching tags
        matches = set(user_prefs).intersection(set(product_tags))
        return len(matches)

    def find_best_matches(self, user_preferences, top_n=2):
        print(f"Finding matches for preferences: {user_preferences}...")
        
        scored_products = []
        for prod in self.products:
            score = self.calculate_score(user_preferences, prod["tags"])
            if score > 0:
                scored_products.append({"product": prod["name"], "score": score})
                
        # Sort by highest score
        scored_products.sort(key=lambda x: x["score"], reverse=True)
        return scored_products[:top_n]

if __name__ == "__main__":
    app = Matchmaker()
    # Test user who likes technology and working out
    user_likes = ["tech", "fitness"]
    
    results = app.find_best_matches(user_likes)
    print("\nTop Matches Found:")
    for res in results:
        print(f"- {res['product']} (Match Score: {res['score']})")
