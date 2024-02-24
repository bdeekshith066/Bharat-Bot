import streamlit as st
import openai
from googletrans import Translator


# Typing animation HTML code with "Project by Deekshith B"
typing_animation = """
<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=500&height=70&lines=Project+by+Deekshith+B" alt="Typing Animation" />
</h1>
"""

# Display the typing animation
st.markdown(typing_animation, unsafe_allow_html=True)

# Function to generate response using GPT-3
def generate_response(prompt, input_lang, output_lang):
    translated_prompt = translate_to_lang(prompt, 'en') if input_lang != 'en' else prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": translated_prompt},
        ]
    )
    generated_response = response['choices'][0]['message']['content'].strip()
    return translate_to_lang(generated_response, output_lang)

# Supported languages
supported_languages = {
    'en': 'English',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'mr': 'Marathi',
    'bn': 'Bengali',
    'gu': 'Gujarati',
    'ur': 'Urdu',
    'pa': 'Punjabi',
    'ml': 'Malayalam',
    'or': 'Odia',
    'kn': 'Kannada',  
    'as': 'Assamese',  
    'kok': 'Konkani',  
    'ne': 'Nepali',  
    'sd': 'Sindhi',  
    'mni': 'Manipuri',  
    'doi': 'Dogri', 
    'mai': 'Maithili', 
    'bho': 'Bhojpuri', 
    'sat': 'Santali', 
    'ks': 'Kashmiri',  
    'chr': 'Chhattisgarhi',  
    'new': 'Newari',  
    'awa': 'Awadhi', 
}

# Function to translate text to English
def translate_to_english(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='en')
    return translated_text.text

# Function to translate text to the desired language
def translate_to_lang(text, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_lang)
    return translated_text.text

def main():
    # Set your OpenAI API key
   
    openai.api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")

    st.title("Bharat Bot 🇮🇳🤖")
    col1, col2 = st.columns([2, 1])
    col1.write("Bharat Bot connects people across India by comprehending")
    col2.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/1200px-Flag_of_India.svg.png", width=150)
    col1.write("and embracing the diverse spectrum of Indian languages.")
    
    st.sidebar.image("https://www.ccjk.com/wp-content/uploads/2021/03/How-many-languages-are-spoken-in-India.png",caption="Unity in Diversity", width=300)
    input_lang = st.sidebar.selectbox("Choose your input language:", list(supported_languages.keys()), format_func=lambda x: f"{x} - {supported_languages[x]}")
    output_lang = st.sidebar.selectbox("Choose your output language:", list(supported_languages.keys()), format_func=lambda x: f"{x} - {supported_languages[x]}")

    for i in range(10):
        user_input = st.text_input(f"Enter your question {i+1}:", key=f"question_{i+1}")

        if st.button(f"Submit {i+1}"):
            if openai.api_key:
                chatgpt_response = generate_response(user_input, input_lang, output_lang)
                st.write(f"Response {i+1}:", chatgpt_response)
            else:
                st.error("Please enter your OpenAI API key.")

if __name__ == "__main__":
    main()
