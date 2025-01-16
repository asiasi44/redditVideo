from voiceover import voiceover_function
import re
from combineAudio import combineAudio

def split_sentences(text):
    # Regular expression to match sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    return sentences

def clean_sentences(sentences):
    # Remove empty, whitespace-only, or newline-only entries
    cleaned = [sentence.strip() for sentence in sentences if sentence.strip()]
    return cleaned

def makeVoiceOvers(content):
    sentences = split_sentences(content["description"])

    valid_sentences = clean_sentences(sentences)

    voiceover_function(content["title"], "audio/question", totalSentences = len(valid_sentences))
    for idx, sentence in enumerate(valid_sentences):
        voiceover_function(sentence, "audio/sentence" + str(idx), totalSentences = len(valid_sentences))
    
    combineAudio(numberOfSentences=len(valid_sentences))
    return valid_sentences