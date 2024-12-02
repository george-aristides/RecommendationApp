import requests
import subprocess

API_KEY = "aab8aada07f42dfe8906834df0736c5a"
BASE_URL = "https://api.themoviedb.org/3"

def fetch_genres(language="en-US"):
    """
    Fetch the list of movie genres from the TMDB API.
    """
    endpoint = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY, "language": language}
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return {genre["id"]: genre["name"] for genre in response.json().get("genres", [])}
    return {}

def get_movies_by_genre(genre_id, page=1, language="en-US"):
    """
    Fetch movies by genre using TMDB API, filtered to include only movies from 2021 or earlier.

    :param genre_id: The ID of the genre to fetch movies for.
    :param page: The page number to fetch.
    :param language: Language of the movie results (default is English).
    :return: JSON response containing the list of movies.
    """
    endpoint = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": language,
        "with_genres": genre_id,
        "page": page,
        "primary_release_date.lte": "2021-12-31"  # Only include movies released in 2021 or earlier
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error: Unable to fetch data (status code {response.status_code})")
        return []

def generate_response_with_ollama(model_name, prompt):
    """
    Generate a response using the LLaMA model via Ollama.
    """
    command = ['ollama', 'run', model_name, prompt]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    return None

def determine_mbti_type(personality_traits, model_name="llama3.1"):
    """
    Determine the user's MBTI type based on their personality traits.
    """
    prompt = f"The user has these personality traits: {personality_traits}. Determine their MBTI type."
    return generate_response_with_ollama(model_name, prompt)

def recommend_books(mbti_type, model_name="llama3.1"):
    """
    Recommend books based on the user's MBTI type.
    """
    prompt = f"The user's MBTI type is {mbti_type}. Recommend three books for this personality type."
    return generate_response_with_ollama(model_name, prompt)
