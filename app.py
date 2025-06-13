# app.py
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, redirect
import smtplib
import random
import os
from email.mime.text import MIMEText

app = Flask(__name__)

# Update these with your Gmail
YOUR_EMAIL = os.getenv("EMAIL_USER")
YOUR_PASSWORD = os.getenv("EMAIL_PASS")  # use Gmail App Password, not your regular one
TO_EMAIL = "shivkarthikeyan1p618@gmail.com"

@app.route("/")
def home():
    quotes = [
        "⋆｡‧˚ʚ🍓ɞ˚‧｡⋆ You're the prettiest girl in the whole world! ⋆｡‧˚ʚ🍓ɞ˚‧｡⋆ ",
        "⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ Im always with you bangaram ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆",
        "𓂃˖˳·˖ ִֶָ ⋆🌷͙⋆ ִֶָ˖·˳˖𓂃 ִֶָ  You make this world better just by existing 𓂃˖˳·˖ ִֶָ ⋆🌷͙⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
        "˚˖𓍢🌷✧˚.🎀⋆ It's okay to have bad days. You're doing amazing bujji baby.˚˖𓍢🌷✧˚.🎀⋆",
        "⋆˚✿🍒𐙚⋆˚ Thousand Kissies all over your face ⋆˚✿🍒𐙚⋆˚"
    ]
    selected_quote = random.choice(quotes)
    return render_template("index.html", quote=selected_quote)


@app.route("/submit", methods=["POST"])
def submit():
    selected = request.form.get("mood_item")
    custom = request.form.get("custom_need")

    final_choice = custom if selected == "Other" else selected

    # Email body
    message = f"What might help bujjibaby:\n{final_choice}"

    msg = MIMEText(message)
    msg["Subject"] = "Bujji baby needs you! 💌"
    msg["From"] = YOUR_EMAIL
    msg["To"] = TO_EMAIL

    # Motivational quote options
    quotes = [
        "⋆｡‧˚ʚ🍓ɞ˚‧｡⋆ You're the prettiest girl in the whole world! ⋆｡‧˚ʚ🍓ɞ˚‧｡⋆ ",
        "⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ Im always with you bangaram ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆",
        "𓂃˖˳·˖ ִֶָ ⋆🌷͙⋆ ִֶָ˖·˳˖𓂃 ִֶָ  You make this world better just by existing 𓂃˖˳·˖ ִֶָ ⋆🌷͙⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
        "˚˖𓍢🌷✧˚.🎀⋆ It's okay to have bad days. You're doing amazing ˚˖𓍢🌷✧˚.🎀⋆",
        "⋆˚✿🍒𐙚⋆˚ Thousand Kissies all over your face ⋆˚✿🍒𐙚⋆˚"
    ]
    selected_quote = random.choice(quotes)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.sendmail(YOUR_EMAIL, TO_EMAIL, msg.as_string())

        # 👇 Show thankyou page with selected quote
        return render_template("thankyou.html", message=final_choice, quote=selected_quote)

    except Exception as e:
        return f"Something went wrong: {e}"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port =10000)

