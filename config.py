import itertools

SITE_CONFIG = {
    "names": {"partner1": "Kruthisver", "partner2": "Grishma"},
    "anniversary_date": "June 6, 2025 00:00:00",
    
    "timeline": [
        {
            "title": "The Day It Started", 
            "date": "June 6, 2025", 
            "desc": "The universe aligned, and a simple 'I Like You' and a cuddle changed everything forever.", 
            "img": "1st.jpeg"
        },
        {
            "title": "First Outing In Hyd", 
            "date": "October 20, 2025", 
            "desc": "Nervous butterflies, endless laughter with beer in Forge...The start of something Beautiful in my life.", 
            "img": "2nd.jpeg"
        },
        {
            "title": "Our Prom", 
            "date": "October 26, 2025", 
            "desc": "A beautiful moment in our life where I promised myself I will give you a life full of kisses and fun dances. You looked so beautiful my babootie.", 
            "img": "3rd.jpeg"
        },
        {
            "title": "Your Birthday", 
            "date": "January 13, 2026", 
            "desc": "The most beautiful day of our life, your birthday. I still remeber seeing you again in a bodycon after a long time and realised once again how beautiful you are. Hope you liked the heart pendant I gave you my papa.", 
            "img": "4th.jpeg"
        },
        {
            "title": "TNY Celebration", 
            "date": "April 12, 2026", 
            "desc": "I looked at you doing something just for me, waiting in the crowd to watch me just dance even though you did'nt know anyone in the crowd, I realized my heart will forever be yours. Thanks for showing up my Baby Panda", 
            "img": "5th.jpeg"
        },
        {
            "title": "Our Last Movie Date As a Student", 
            "date": "April 14, 2026", 
            "desc": "Even though the cafe was not as good as we expected, just being with you, chit-chatting, Playing UNO made me realise the place doesn't matter but the person you are with. You will always be the 'Person' for me my cutie patootie.", 
            "img": "6th.jpeg"
        },
        {
            "title": "Farewell", 
            "date": "May 3, 2026", 
            "desc": "The day I got knocked out seeing you in a beautiful saree, can't express my emotions with just words. The day it also hit me that we will be apart for a while and I am so sorry for the fight we had before leaving. Please forgive your bun bun.", 
            "img": "7th.jpeg"
        },
        {
            "title": "One Year Down", 
            "date": "May 30, 2026", 
            "desc": "365 days of loving, and it feels like we've just begun. Missing you a lot my busu busu.", 
            "img": "8th.jpeg"
        }
    ],

    "love_letter": """My Dearest Busu Busu,

As I sit down to write this, I find myself going through all the beautiful memories we had in this past 365 days. How do I even begin to put into words what this year has meant to me. One year sounds like a long time, but it has flown by in the blink of an eye. 

I still remember the day i met you for the first time in Bangalore. I came for the internship thinking it is gonna be tough as i didn't know anyone here but you came to me like an angel. Included me into your group and made me feel like one among ur group. I still remember all the walks we went, the quests we did, the lakes we discovered, the late night snacks we had, the movies we watched, the IPL final, the first sip of alcohol, everything is still like a day dream to me that I spent this much time with a girl before being in a relationship with her. Somewhere along this road i fell for you hard. I still remember the times I sort of felt jealous seeing you talking with other guys, without knowing that this is something I felt because I was already in Love with you. Before I realised this you proposed me a year ago on this same day. Made me the most happiest person in the world and I didn't have a single doubt in my mind at that moment when i said 'Yes' to you that this will be the best decision i will ever make in my life. Thanks for proposing me my Baby. 

This road has not just been roses and violins for us, we had our fights. Some silly fights, some very big fights which almost drove us to break up, but we never did. We both love each other that every fight we had, we somehow resolved and overcame that and here we are spending our first anniversary. I have not been the most ideal boyfriend, but I will try my hard to be the one. Thanks for puttting up with me and still loving me the way you loved me a year ago. I have always made it hard for you on every occasions doing something stupid, and I am not gonna promise you that I am not gonna do anything stupid in future, but one thing I promise you is I will always love you and will never leave you even if you ask me to. You will always be my busu busu and that bond is something that will never be broken until I die.

Thank you for choosing me. Thank you for loving me exactly as I am. Happy First Anniversary, my Baby Panda. Here is to us, today, tomorrow, and for all the days that follow.

Your bun bun forever.""",
}

# --- Generate 10 Cute Notes ---
base_notes = [
    "I love you more today than yesterday my baby.", "You are my favorite notification my babootie.",
    "Home is wherever I'm with you my papa.", "I still get butterflies every time I see you my cutie patootie.",
    "You are the best thing that ever happened to me in my life my Griboo.", "You are always my first thought of the day my sweet potato chip.",
    "You make the ordinary moments magical my chubby cheeks.", "I am so lucky to be yours my busu busu.","You are my constant sweet dream every night my big booty papa.", "I love you and miss you more than ever my cutie little baby hippopotamus.",
]
SITE_CONFIG["notes"] = [f"{base_notes[i % len(base_notes)]} (Note #{i+1} 💌)" for i in range(10)]

# --- Generate 100 unique Happiness Button Reasons ---
subjects = ["Your smile", "Your energy", "The way you care", "Your laugh", "Your voice"]
verbs = ["lights up", "gives peace to", "completely transforms", "brings joy to"]
objects = ["my world", "my heart", "every single day", "my soul", "my life"]
combinations = list(itertools.product(subjects, verbs, objects))
SITE_CONFIG["smile_reasons"] = [f"{s} {v} {o} ❤️" for s, v, o in combinations[:100]]