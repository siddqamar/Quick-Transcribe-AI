# Quick Transcribe AI

 If you take notes, you already know how useful it is to have transcriptions of lectures, meetings, phone calls, even YouTube videos. With that in mind, I’ve built an app and making it public for everyone as a Docker container.


## Prerequisites

- Docker installed on your system
- A Hugging Face API token (get one from [Hugging Face](https://huggingface.co/settings/tokens))

## Setup

1. Fork/Clone this repository
2. Copy the example environment file and add your Hugging Face token:
   ```bash
   cp .env.example .env
   ```
3. Edit `.env` and replace `<your-token>` with your actual Hugging Face API token

## Building and Running

1. Build the Docker image:
   ```bash
   docker build -t quick-transcribe-ai .
   ```

2. Run the container:
   ```bash
   docker run -d -p 7860:7860 -v $(pwd)/.env:/app/.env:ro quick-transcribe-ai
   ```

3. Access the application at `http://localhost:7860`

## Features

- Supports audio and video both
- Real-time transcription using Whisper large-v3-turbo model
- Clean and intuitive Gradio interface
- Downloadable transcription results
- Dockerized for easy deployment

## Notes

- The application uses the `openai/whisper-large-v3-turbo` model from Hugging Face
- Make sure your Hugging Face API token has sufficient permissions
- The container exposes port 7860 for the Gradio interface 