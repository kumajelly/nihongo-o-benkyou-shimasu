import os
import re
import requests
import sys

ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
API_URL = "https://api.elevenlabs.io/v1/text-to-speech"
VOICE_ID = "Mv8AjrYZCBkdsmDHNwcB"
processed_dir = "processed"
output_dir = "processed-audio"
os.makedirs(output_dir, exist_ok=True)

def extract_translation(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    match = re.search(r"\*\*Translation\*\*:\n(.*?)\n\n", content, re.DOTALL)
    if match:
        return match.group(1).strip().split("\n")
    return []

def generate_audio(text, output_path):
    headers = {
        "Authorization": f"Bearer {ELEVEN_LABS_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "text": text,
        "voice_id": VOICE_ID
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        with open(output_path, "wb") as audio_file:
            audio_file.write(response.content)
        print(f"Audio saved to {output_path}")
    else:
        print(f"Failed to generate audio: {response.text}")

def main():
    if len(sys.argv) > 1:
        selected_date = sys.argv[1]
        filename = f"{processed_dir}/{selected_date}.txt"
        if os.path.exists(filename):
            files_to_process = [filename]
        else:
            print(f"File for date {selected_date} not found!")
            sys.exit(1)
    else:
        # Process all new files automatically
        files_to_process = [os.path.join(processed_dir, f) for f in os.listdir(processed_dir) if f.endswith(".txt")]

    for filepath in files_to_process:
        translations = extract_translation(filepath)
        if translations:
            base_filename = os.path.basename(filepath).replace(".txt", "")
            for idx, line in enumerate(translations, start=1):
                audio_output_path = os.path.join(output_dir, f"{base_filename}-{idx}.mp3")
                generate_audio(line, audio_output_path)

if __name__ == "__main__":
    main()
