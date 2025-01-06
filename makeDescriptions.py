from makeVoiceOvers import makeVoiceOvers
from audioDuration import calculate_audio_duration
from combineAudioAndVideo import combineAudioAndVideo

def split_into_chunks(sentence, chunk_size=3):
    words = sentence.split()
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
    return chunks

def adjust_times(data):
    result = []
    
    start_time = 0
    for item in data:
        sentence = item['description']
        end_time = item['endTime']
        
        words = sentence.split()
        num_words = len(words)
        
        # Calculate time per word (proportional to sentence length)
        time_per_word = (end_time - start_time )/ num_words
        
        # Split words into chunks of 4 and assign time for each chunk
        chunks = split_into_chunks(sentence)
        
        for idx, chunk in enumerate(chunks):
            chunk_size = len(chunk)  # Check if the chunk is less than 4 words in case of the last chunk
            chunk_end_time = start_time + (time_per_word * chunk_size)
            
            result.append({
                'description': " ".join(chunk),
                'endTime': chunk_end_time
            })
            
            start_time = chunk_end_time  # Update the start time for the next chunk
            
    return result

def makeDescriptions(content):
    getSentences = makeVoiceOvers(content)

    newTime = 0

    for idx, eachSentence in enumerate(getSentences):
        newTime = newTime + calculate_audio_duration("audio/sentence"+ str(idx))
        getSentences[idx] = {
            "description": eachSentence,
            "endTime": newTime
        }
    output = adjust_times(data=getSentences)
    return output