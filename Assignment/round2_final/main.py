def recommend_books(members, books):
    recommendation = []
    
    for member in members:
        recommend_books = None
        preferred_genre = member["preferred_genre"]
        
        for book in books:
            if book["genre"] == preferred_genre:
                recommend_books = book["title"]
                break
            
        recommendation.append({"member": member["name"], "book": recommend_books})
        
    return recommendation


members = [
    {"name": "Alice", "preferred_genre": "Romance"},
    {"name": "Bob", "preferred_genre": "Sci-Fi"},
]

books = [
    {"title": "Love in the Rain", "genre": "Romance"},
    {"title": "Historical", "genre": "Histroy"},
]


recommendations = recommend_books(members, books)

for recommendation in recommendations:
    print(recommendation)