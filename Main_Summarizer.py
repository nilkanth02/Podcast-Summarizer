import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load all the enviremnets Variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key='AIzaSyBtjP6EaaNsVypO5vuGQNr9zh8gLfzlACs')

prompt = """You are a YouTube video summarizer. You will be provided with the full transcript of a YouTube video. Your task is to summarize the key points of the video in a clear, concise format.

Follow these guidelines:
1. Summarize the video in **bullet points**.
2. Provide **key takeaways** and any **important details** discussed in the video.
3. Keep the summary within **250 words**.
4. Focus on the most **important information** and avoid unnecessary details.
5. Structure your summary logically, with each point addressing a unique takeaway.

Here is the transcript:

{TRANSCRIPT_TEXT}
"""


## Getting the transcript data from YouTube Videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = " "
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e


## Getting the summary based on the prompt
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text


st.title("Youtube Transcript to Detailed Notes Converter")
youtube_link = st.text_input(" Enter YouTube Video Link: ")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes "):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown(" ##Detailed Notes:")
        st.write(summary)
