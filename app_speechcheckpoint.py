import streamlit as st
import speech_recognition as sr




def transcribe_speech(): 
    # Initialize recognizer class 
    r = sr.Recognizer() 

# Define available APIs
api_options = {
    "google": "Google Speech Recognition",
    "sphinx": "CMU Sphinx (offline)",
    "wit": "Wit.ai",
    "ibm": "IBM Speech to Text"
}

# Let user choose API
print("Choose your Speech Recognition API:")
for key, name in api_options.items():
    print(f"- {key}: {name}")

user_choice = input("Enter API name (e.g. 'google'): ").strip().lower()

    # Reading Microphone as source
with sr.Microphone() as source: 
            st.info("Speak now...") 
    # listen for speech and store in audio_text variable 
            audio_text = r.listen(source) 
            st.info("Transcribing...") 
            try: 
    # using Google Speech Recognition 
                text = r.recognize_google(audio_text)
                return text 
            except:
                return "Sorry, I did not get that."
    
    user_input = st.text_input("You:", key="text")  

try:
    if user_choice == "google":
        text = recognizer.recognize_google(audio_data)
    elif user_choice == "sphinx":
        text = recognizer.recognize_sphinx(audio_data)
    elif user_choice == "wit":
        text = recognizer.recognize_wit(audio_data, key="YOUR_WIT_AI_KEY")
    elif user_choice == "ibm":
        text = recognizer.recognize_ibm(audio_data, username="YOUR_IBM_USERNAME", password="YOUR_IBM_PASSWORD")
    else:
        print("Unsupported API selected.")
        text = None

    if text:
        print(f"📝 Recognized Text: {text}")

except sr.UnknownValueError:
    print("Couldn't understand the audio.")
except sr.RequestError as e:
    print(f"🔧 API error: {e}")


def main(): 
    st.title("Speech Recognition App") 
    st.write("Click on the microphone to start speaking:") 
# add a button to trigger speech recognition 
    if st.button("Start Recording"): 
        text = transcribe_speech() 
        st.write("Transcription: ", text) 
    
    
if __name__ == "__main__": 
     main()

     
#error with indentartion, code does not run 