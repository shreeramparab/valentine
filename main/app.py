DEV_MODE = False # set to False for production and True for developement
from flask import Flask, render_template
from datetime import datetime
import os 

app = Flask(__name__)

DAYS = [
    ("rose", "🌹 Rose Day", "02-07"),
    ("propose", "💍 Propose Day", "02-08"),
    ("chocolate", "🍫 Chocolate Day", "02-09"),
    ("teddy", "🧸 Teddy Day", "02-10"),
    ("promise", "🤞 Promise Day", "02-11"),
    ("hug", "🤗 Hug Day", "02-12"),
    ("kiss", "😘 Kiss Day", "02-13"),
    ("valentine", "💖 Valentine’s Day", "02-14"),
]

CAPTIONS = {
    "rose": [
        "Just like this rose, you make my world bloom 🌹",
        "Every petal reminds me of how special you are to me 💕",
        "You are the most beautiful part of my life"
    ],
    "propose": [
        "This was the moment I knew my heart was yours 💍",
        "I’d choose you today, tomorrow, and always",
        "You are my forever"
    ],
    "chocolate": [
        "Life is sweeter with you 🍫",
        "You melt my heart more than chocolate ever could",
        "Every sweet moment reminds me of you"
    ],
    "teddy": [
        "You are my comfort, my safe place 🧸",
        "Whenever I need warmth, I think of you",
        "Holding you feels like home"
    ],
    "promise": [
        "I promise to stand by you, no matter what 🤞",
        "I promise to love you more every single day",
        "You are my always",
        "I promise to love you more every single day",
        "I promise you to be with you forever"
    ],
    "hug": [
        "Every hug from you fixes everything 🤗",
        "I wish I could hold you like this forever",
        "Your arms are my favorite place"
    ],
    "kiss": [
        "Every kiss feels like magic 😘",
        "Time stops when I’m close to you",
        "My heart races every time"
    ],
    "valentine": [
        "You are my today, my tomorrow, my forever ❤️",
        "Happy Valentine’s Day, my love",
        "This love story is my favorite"
    ]
}

def today_str():
    now = datetime.now()
    return f"{now.month:02d}-{now.day:02d}"

@app.route("/")
def index():
    today = today_str()
    days=[]

    for slug, name, date in DAYS:
        days.append({
            "slug": slug,
            "name": name,
            "date": date,
            "unlocked": DEV_MODE or today >= date
        })

    return render_template("index.html", days=days)


@app.route("/day/<slug>")
def day(slug):
    today = today_str()

    for d in DAYS:
        if d[0] == slug:
            if DEV_MODE or today >= d[2]:
                image_folder = os.path.join(
                    app.static_folder, "images", slug
                )

                images = []
                if os.path.exists(image_folder):
                    images = [
                        f"images/{slug}/{img}"
                        for img in os.listdir(image_folder)
                        if img.lower().endswith((".png", ".jpg", ".jpeg",".mp4"))
                    ]

                captions = CAPTIONS.get(slug, [])

                return render_template(
                    "day.html",
                    title=d[1],
                    images=images,
                    captions=captions
                )


            else:
                return "This surprise is not unlocked yet 💕", 403

    return "Not found", 404



if __name__ == "__main__":
    port=int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port,debug=True)