from makeVoiceOvers import makeVoiceOvers
from audioDuration import calculate_audio_duration
from combineAudioAndVideo import combineAudioAndVideo

def split_into_chunks(sentence, chunk_size=1):
    words = sentence.split()
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
    return chunks

def adjust_times(data, newTime):
    result = []

    start_time = newTime

    for item in data:
        sentence = item['description']
        end_time = item['endTime']
        words = sentence.split()
        num_words = len(words)
        num_character = 0   
        for i in range(num_words):
            num_character = len(words[i]) + num_character
        # Calculate time per word (proportional to sentence length)
        time_per_word = (end_time - start_time )/ num_words
        time_per_character = (end_time - start_time)/ num_character
        # Split words into chunks of 4 and assign time for each chunk
        chunks = split_into_chunks(sentence)
        
        for idx, chunk in enumerate(chunks):
            chunk_size = len(chunk)
            character_length = len(chunk[0])
            chunk_end_time_for_word = start_time + (time_per_word * chunk_size)

            chunk_end_time_using_char = start_time + (time_per_character * character_length)
            result.append({
                'description': " ".join(chunk),
                'endTime': chunk_end_time_using_char
            })
            # start_time = chunk_end_time_for_word # Update the start time for the next chunk
            start_time = chunk_end_time_using_char
    return result

def makeDescriptions(content):
    getSentences = makeVoiceOvers(content)
    questionTime = 0
    newTime = questionTime

    for idx, eachSentence in enumerate(getSentences):
        newTime = newTime + calculate_audio_duration("audio/sentence"+ str(idx))
        getSentences[idx] = {
            "description": eachSentence,
            "endTime": newTime
        }
    
    output = adjust_times(data=getSentences, newTime=questionTime)
    return output, questionTime