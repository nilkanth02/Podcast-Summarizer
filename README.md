
# Podcast Summarizer

Welcome to the **Podcast Summarizer**! This tool leverages cutting-edge AI to help you turn YouTube video transcripts into clear, concise summaries, making it easier to digest key takeaways from podcasts and other long-form videos.

## Overview

The Podcast Summarizer allows you to input a YouTube video URL, and it will automatically extract the video’s transcript and generate a detailed, easy-to-read summary. This summary focuses on the key points of the video, structured as bullet points to provide you with a quick overview.

Whether you're trying to catch up on your favorite podcast or want to review important content from a YouTube lecture, this tool is perfect for you.

## Features

- **Summarizes YouTube videos:** Input a YouTube video URL and receive a summary of the key points in a concise format.
- **Bullet-point summaries:** The summary is neatly organized in bullet points, so you can quickly skim through the most important takeaways.
- **AI-powered summarization:** Using the Gemini model by Google, the content is automatically processed to highlight critical information and make it easily digestible.
- **Easy to use interface:** Just input the video URL and click "Get Detailed Notes"—it’s that simple!

## How it Works

1. **Extract Transcript**: The app pulls the transcript from a YouTube video using the `youtube_transcript_api`.
2. **Generate Summary**: The transcript is then passed to an AI model (Gemini) which generates a structured summary of the key points.
3. **Display the Results**: The generated summary is presented in a clean and user-friendly interface for easy reading.

## Installation

To use this project, you’ll need to install the required dependencies and set up the necessary environment variables. Here's how:

### Prerequisites

- Python 3.7 or higher
- Streamlit for the web interface
- `google.generativeai` library for AI summarization
- `youtube_transcript_api` for fetching transcripts
- `.env` file for storing your API key

### Steps

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/nilkanth002/podcast-summarizer.git
    cd podcast-summarizer
    ```

2. **Install Dependencies**:

    Make sure you have Python 3.7 or higher, and then install the required dependencies using pip:

    ```bash
    pip install streamlit google-generativeai youtube-transcript-api python-dotenv
    ```

3. **Setup the Environment**:

    Create a `.env` file in the root directory of the project and add your API key for Gemini. It should look like this:

    ```
    GEMINI_API_KEY=your-api-key-here
    ```

4. **Run the App**:

    To start the app locally, use the following Streamlit command:

    ```bash
    streamlit run app.py
    ```

    Open the link provided in your browser to access the web interface.

## Usage

1. Open the web interface by running the app.
2. Paste the YouTube video link of your podcast or lecture into the input box.
3. Click the **"Get Detailed Notes"** button.
4. The AI will process the transcript and return a bullet-point summary of the key points.

The output summary will look something like this:

```
- Key takeaway #1 from the video
- Key takeaway #2 with additional details
- Important point discussed around X topic
```

## Example

Here's an example of how the application works:

1. You input a YouTube link like `https://www.youtube.com/watch?v=dQw4w9WgXcQ`.
2. The transcript is extracted, and the AI processes it to provide a summary in bullet points, such as:

```
- Rick Astley’s hit song "Never Gonna Give You Up" was released in 1987.
- The music video became a popular meme in the 2000s.
- The impact of memes on modern pop culture is discussed.
```

## Contributing

We welcome contributions! If you find any issues or have ideas for improvements, please feel free to open an issue or submit a pull request.




Thanks for using Podcast Summarizer! We hope it helps you save time and quickly catch up on the most important content in podcasts and YouTube videos.
