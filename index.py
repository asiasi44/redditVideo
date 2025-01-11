from makeVideo import makeVideo
from makeDescriptions import makeDescriptions
from combineAudioAndVideo import combineAudioAndVideo, editTheVideo
from makeIntro import make_intro

content = {
    "title": "Cheat on your wife with mine? I will burn your life to the ground.",
    "description": """
Way back in the early 2000’s, I began to suspect that my wife was up to something. Our two kids were about 4 and 6, still young, but not so young they couldn’t tell you something about what had happened in their day. They started talking a lot about staying with my wife’s parents during the day which wasn’t really that strange in and of itself, but since they lived about 90 minutes away, doing so two or three times a week seemed a bit much (that was basically every day she wasn’t working at her part time job).

When I asked her about it, she denied it, but was never a good liar. So, I started tracking the mileage on her car and sure enough, she was driving an extra 400 or so miles per week. I knew some shit was going on.

Then one day I sat down at the computer and she had left a sticky note with her AOL password written on it next to the keyboard. I could not resist and logged in to read her emails and saw a few email exchanges between her and her college BFF where they discussed how my wife was regularly fucking one of her ex bf’s from high school. No mention of details about him other than my wife also talking shit about his wife making fun of how she’d gotten fat after having kids. Anyway, I printed out these email exchanges and stashed them.

I still needed to know the details, so I called a friend who was a cop and he suggested I call a guy he knew that had left the force to become a PI. “Ron” was great, I paid his retainer and gave him the emails and what little I knew about my wife’s activities and he figured out exactly what she was doing. His report detailed with photos and times/dates/locations all about how she would take the kids to her parent’s, then go meet this guy for lunch, then they’d go to a dumpy motel for a few hours, after which she’d pick up the kids and return home.

At this point, I hired a divorce lawyer. My parents cheated on each other and the fallout absolutely fucked mine and my siblings’ childhood. It was something that was totally unacceptable.

I also asked Ron to find out what he could about this guy. Ron absolutely came through. I learned his name (“Bob”) , that he was married and had 3 kids. I also found out that he worked as a VP of sales for his father in law’s business. Hmmmm.

At this point, I had my lawyer draw up the divorce papers. I also asked Ron for a couple more copies of his report and I one more thing I wanted him to do for me.

On the same day I had my wife served with the divorce papers at her work, I had Ron meet with this guy’s wife and show her everything he’d found out. She seemed nice and I figured that she deserved to know what her dear hubby was up to. What she did with that information was up to her.

While the information about my wife’s infidelity didn’t really matter in my divorce proceedings, Bob’s wife did a real number on him. According to the publicly available court documents from the divorce and other related proceedings, she cleaned out their joint account, took the kids and left. As soon as her dad found out what he’d done, Bob was fired and since her parents actually owned the house where Bob and his wife lived, he also got evicted. Their divorce was ugly. Lots of fighting in ( and evidently out of) court. I guess Bob went to the house and started arguing with his wife and it escalated to the point the her brother stepped in and Bob got his nose broken. There were restraining orders, a few more incidents with police reports, criminal charges, jail time and so on.

I can’t find Bob on the internet anywhere these days. Last I heard, he’d left the state and His ex wife did ok, she went to work at her dad’s company and took over after he retired.

As for me, my ex and I got along well enough, I didn’t engage with her on anything that wasn’t related to the kids and now that they’re both adults, I don’t talk to her at all anymore. I don’t hate her or anything, but I only care in the context that she is my kids’ mom and is important to them, nothing beyond that.
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

makeVideo(listOfFourWords, content["title"], questionTime)

combineAudioAndVideo("savedVideo", "combined_output", "combinedVideo")

make_intro()

# editTheVideo("finalVideoComplete.mp4")