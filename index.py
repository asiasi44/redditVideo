from makeVideo import makeVideo
from makeDescriptions import makeDescriptions
from combineAudioAndVideo import combineAudioAndVideo, editTheVideo
from makeIntro import make_intro

content = {
    "title": "Hello my name is asim",
    "description": """
I am twenty-five years old. My best friend, whose name is Emma, is twenty-six years old. She has been in my life for as long as I can remember, and I genuinely cannot imagine my life without her in it. She has always been that person I can count on, my closest friend and my biggest support system. She was the very first person I confided in when I came out during high school, and her response was simply to smile and ask if I wanted to get some pizza. That is just the kind of person she is, and it is part of the reason she is so special to me.
To be honest, I was head over heels in love with Emma during my teenage years. My feelings for her were so deep that it felt overwhelming. However, I never acted on those feelings because, at the time, she had never expressed any interest in girls. Besides, I was terrified of ruining what we already had, which was such a profound and meaningful friendship. Over time, I eventually moved on and had relationships with other women, but none of them worked out the way I had hoped. Every heartbreak, every disappointment—Emma was always there for me, ready to pick up the pieces.
Emma, for her part, has always been a private person when it comes to her love life. During high school, she was not really interested in dating, which was completely understandable given the tragic loss of both her parents when she was only sixteen years old. The grief she endured was unimaginable, and it created walls around her heart that few people could get through. Over the years, she managed to rebuild herself, and by college, she met a guy named Adam. They were together for almost six years, and during that time, I genuinely thought they were happy together.
Last summer, Emma and Adam decided to part ways. From what Emma told me, it was a mutual decision based on growing apart. Around the same time, my own relationship ended in a devastating way when I discovered that the girl I had been dating for three years had cheated on me with multiple people. That heartbreak was one of the hardest things I had ever endured, and Emma was once again there to support me.
With both of us newly single, we naturally started spending more time together. We would watch movies, grab dinner, go on drives, and just be there for each other. Our bond deepened even more, and while I thought it was just us reconnecting as best friends, there was something beneath the surface that neither of us was acknowledging yet.
Fast-forward to February, and we had a trip planned to the Caribbean with Emma’s sister, Julie, and Julie’s girlfriend. The night before our flight, we all stayed at Emma’s apartment to make things easier for travel the next morning. While waiting for Julie and her girlfriend to arrive, Emma and I started playing Mario Kart together. As usual, she was extremely competitive, and when I beat her, she tried to wrestle the controller away from me in frustration.
That playful moment led to something I could never have predicted. Emma pinned me down on the couch, and suddenly her expression changed. She leaned in, hesitated for only a moment, and then kissed me. The kiss caught me completely off guard, but instead of pulling away, I kissed her back. For the first time in years, every buried feeling I had for Emma came rushing to the surface.
The sound of Julie knocking on the door shattered the moment, and Emma quickly pulled away. For the rest of the evening, everything felt awkward between us. Julie and her girlfriend even noticed and commented on how strange we were acting, but we brushed it off.
Emma and I were sharing her bed that night, something we had done many times before, but this time it felt entirely different. I almost left the apartment altogether, but I could not bring myself to run away. When I got into bed, Emma was already lying down, looking emotional. She apologized for kissing me and admitted she had no idea why she had done it, but she did not regret it either. She asked if we could have a proper conversation about it when we arrived at the resort because she was not ready to unpack everything that night.
When we finally got to our hotel, Emma opened up to me in a way she never had before. She admitted that she was not straight, that she had always been interested in both men and women, but that she had kept it to herself. She explained that when we were teenagers, she had been aware of my crush on her, and because she was not ready to explore her own feelings back then, she kept that side of herself hidden. She said she loved being with Adam, but now that they were over, her feelings for me had taken her by surprise.
When I reminded her that we were cousins, she simply shrugged and said it did not matter to her. That moment broke something inside me. Everything I had ever felt for Emma came rushing back, and I could not deny it anymore. For the rest of the trip, Emma and I decided to quietly explore what it would mean to be a couple.
We spent that week growing closer than ever. Sharing a room, holding hands when nobody was looking, and talking late into the night felt so natural, so right. I had never experienced a connection like this with anyone else before, and every moment with her felt like it was exactly where I was meant to be.
Now that we are back home, we agreed to take some time apart to sort through our feelings and figure out what we want. It has been two weeks, and I can barely sleep at night because I miss her so much. Tonight, Emma is coming over because I called her and told her I could not keep going like this without seeing her. I do not know what we will say or where this will go, but I know one thing for sure. I love her.
"""
}

def format_text_for_ascii(input_text):
    # Define replacements for common problematic characters
    replacements = {
        "’": "'",
        "‘": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",
        "…": "...",
        "é": "e"  # Example of accented replacement, add more as needed
    }
    # Replace each special character with its plain-text equivalent
    for old_char, new_char in replacements.items():
        input_text = input_text.replace(old_char, new_char)
    return input_text

# Example usage
content["description"] = format_text_for_ascii(content["description"])

listOfFourWords, questionTime = makeDescriptions(content=content)

makeVideo(listOfFourWords)

combineAudioAndVideo("savedVideo", "combined_output", "combinedVideo")

make_intro()

# editTheVideo("finalVideoComplete.mp4")