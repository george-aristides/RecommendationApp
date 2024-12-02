# Movie Recommendation App

A web-based application that provides personalized book recommendations based on user's movie preferences using Ollama.

This application was built to help users be encouraged to read.

It works on the principal of creating a user profile based on their movie preferences instead of correlating movies to books. Our goal was to find a methodology to use extremely limited inputs to and generate a high likelihood of interaction with the recommendation.

## Features

- **Multi-genre Movie Picking**: Choosing up to three movies across multiple genres.
- **Detailed Recommendation Reasoning**: Gives you a description on your user profile and why the recommendations were made.

## Installation

To set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/george-aristides/RecommendationApp.git
2. **Navigate to Project Directory:**
    ```
    cd RecommendationApp
3. **Install Dependancies:**
    - For the backend:
    ```
    cd backend
    pip install -r requirements.txt
    ```
    - For the front end:
    ```
    cd ../frontend
    npm install
    ```
4. Configure Environment Variables
    - Create a new ```.env``` file in both the backend and frontend directories.
    - Add necessary environment variables as specified in ```.env.example``` files.

5. Ollama installation:
    - Follow instructions here:
    ```https://github.com/ollama/ollama```
    - Make sure to run this in your terminal before running the Recommendation Application:
    ```ollama pull llama 3.1```
