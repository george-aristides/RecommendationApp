from flask import Flask, render_template, request, jsonify
import movie_logic as logic

app = Flask(__name__)

@app.route("/")
def index():
    # Render the main page
    genres = logic.fetch_genres()
    return render_template("index.html", genres=genres)

@app.route("/get_movies", methods=["POST"])
def get_movies():
    # Fetch movies by genre
    genre_id = request.json.get("genre_id")
    page = request.json.get("page", 1)
    movies = logic.get_movies_by_genre(genre_id, page)
    return jsonify(movies)

@app.route("/generate_traits", methods=["POST"])
def generate_traits():
    # Generate personality traits
    selected_movies = request.json.get("movies")
    prompt = f"The user selected these movies: {', '.join(selected_movies)}. Describe this user in three traits."
    traits = logic.generate_response_with_ollama("llama3.1", prompt)
    return jsonify({"traits": traits})

@app.route("/determine_mbti", methods=["POST"])
def determine_mbti():
    # Determine MBTI type
    traits = request.json.get("traits")
    mbti_type = logic.determine_mbti_type(traits, "llama3.1")
    return jsonify({"mbti_type": mbti_type})

@app.route("/recommend_books", methods=["POST"])
def recommend_books():
    # Recommend books
    mbti_type = request.json.get("mbti_type")
    recommendations = logic.recommend_books(mbti_type, "llama3.1")
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
