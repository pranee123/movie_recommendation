# movie_recommendation
![Screenshot 2024-10-04 123720](https://github.com/user-attachments/assets/d7675bed-00a4-49cd-beae-501d1422b6de)


### Created Virtual Environment
* Used '''python -m venv .venv''' to create the Virtual environment
* Activationg the Virtual Environment
'''source .venv/Scripts/activate'''
## install requirements
use ''' pip install -r requirements.txt'''

Readme File for Movie Recommender Streamlit App
**Overview**
This Streamlit app leverages Google's Generative AI capabilities to provide personalized movie recommendations based on user input. Users can enter a movie title, genre, song, or keyword, and the app will generate tailored recommendations.

**Requirements**
Python 3.x
Streamlit
Google Generative AI
Langchain
Langchain Google Generative AI
dotenv (for environment variable management)
Installation
Create a virtual environment:
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Use code with caution.

Install required packages:
Bash
pip install streamlit google-generativeai langchain langchain-google-genai dotenv
Use code with caution.

## Set up
-Set up your Google Cloud Platform API key:
-Obtain an API key from the Google Cloud Platform console.
-Create a .env file in your project directory and add the following line:
GOOGLE_API_KEY=your_api_key

Usage
Run the Streamlit app:
Bash
streamlit run app.py
Use code with caution.

-Enter your movie input: In the web interface, type a movie title, genre, song, or keyword into the text box.
-View recommendations: The app will generate and display personalized movie recommendations.
Customization
-Model: You can experiment with different Google Generative AI models (e.g., "gemini-ultra") to potentially achieve different results.
-Prompt engineering: Modify the demo_template to fine-tune the prompts and improve the quality of recommendations.
-Additional features: Consider adding features like user ratings, genre filters, or integration with external movie databases.

Note:
-Ensure you have a valid Google Cloud Platform API key and have enabled the necessary services.
-For production use, consider implementing error handling and logging to monitor app performance.
-Explore the capabilities of Google Generative AI and Langchain to further enhance your movie recommendation system.






