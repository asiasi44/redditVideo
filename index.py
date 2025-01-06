from makeVideo import makeVideo
from makeDescriptions import makeDescriptions
from combineAudioAndVideo import combineAudioAndVideo, editTheVideo
from makeIntro import make_intro

content = {
    "title": "Am i wrong or is tejesh mad",
    "description": "I met tejesh today and he talks nonsense. So I think he is mad"
}

listOfFourWords = makeDescriptions(content=content)

makeVideo(listOfFourWords)

combineAudioAndVideo("savedVideo", "combined_output", "combinedVideo")

make_intro()

editTheVideo("finalVideoComplete.mp4")