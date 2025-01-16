from pyt2s.services import stream_elements
import os
from pydub import AudioSegment

def validate_audio(file_path):
    """
    Validates an audio file by attempting to load it with Pydub.
    Ensures the file has valid content and is not corrupted.

    :param file_path: Path to the audio file
    :return: True if valid, False otherwise
    """
    try:
        audio = AudioSegment.from_file(file_path)
        duration = audio.duration_seconds

        # A valid file should have a duration greater than zero
        return duration > 0
    except Exception as e:
        print(f"Audio validation failed for {file_path}: {e}")
        return False

def voiceover_function(voiceoverText, ouputFileName, totalSentences, max_retries=3):
    """
    Generates a voiceover MP3 file and validates it. If the audio is invalid,
    it will retry generating it up to a specified number of times.

    :param voiceoverText: The text for the voiceover.
    :param ouputFileName: The desired file name for the audio output.
    :param max_retries: Maximum number of retries for generating valid audio.
    """
    attempt = 0
    output_path = ouputFileName + '.mp3'

    while attempt < max_retries:
        try:
            print(f"Attempt {attempt + 1} to generate audio.", ouputFileName , "/ ", totalSentences)
            
            # Generate audio using StreamElements
            data = stream_elements.requestTTS(voiceoverText, voice='Salli')
            
            # Write the audio data to the output file
            with open(output_path, 'wb') as file:
                file.write(data)

            # Validate the generated audio file
            if validate_audio(output_path):
                print("Audio generated and validated successfully.")
                return True
            else:
                print("Generated audio is invalid, retrying...")

        except Exception as e:
            print(f"An error occurred during audio generation: {e}")

        attempt += 1

    # If all retries fail, raise an exception
    print(f"Failed to generate valid audio after {max_retries} attempts.")
    raise RuntimeError("Unable to generate valid audio.")

# Example usage
# voiceover_function("This is a test voiceover", "output")
