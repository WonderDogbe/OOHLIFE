from datetime import datetime
from flask import Flask, render_template, request

from life_paths import LIFE_PATHS

app = Flask(__name__)

# Curated life insights mapped to indices 0 through 9
# You can easily customize these 10 outputs.
LIFE_OUTPUTS = [
    # 0:
    "Embrace new beginnings with an open heart; stillness before action brings great clarity.",
    # 1:
    "Your leadership and independence are your greatest strengths—trust your unique vision today.",
    # 2:
    "Harmony and partnership will unlock doors that sheer effort alone cannot move.",
    # 3:
    "Unleash your creative voice and express your genuine truth without hesitation.",
    # 4:
    "Consistent daily discipline will build the sturdy foundation for your biggest ambitions.",
    # 5:
    "Welcome change and adventure; the unexpected detours often lead to the best destinations.",
    # 6:
    "Nurture your loved ones and your surroundings; compassion is your superpower.",
    # 7:
    "Take time for introspection and learning; inner wisdom is your truest compass.",
    # 8:
    "Balance ambition with integrity; your capability to manifest real-world results is at a peak.",
    # 9:
    "Let go of what no longer serves your growth and make space for your highest potential.",
]


@app.route("/", methods=["GET", "POST"])
def index():
    today_str = datetime.now().strftime("%Y-%m-%d")

    if request.method == "POST":
        raw_name = request.form.get("name", "").strip()
        dob_raw = request.form.get("dob", "").strip()

        if not raw_name or not dob_raw:
            return render_template(
                "index.html",
                error="Please enter both your first name and date of birth.",
                name=raw_name,
                dob=dob_raw,
                max_date=today_str,
            )

        if " " in raw_name:
            return render_template(
                "index.html",
                error="Please enter only your first name (no spaces or last names).",
                name=raw_name,
                dob=dob_raw,
                max_date=today_str,
            )

        name = raw_name.capitalize()

        try:
            # Parse the date format YYYY-MM-DD
            dob_parsed = datetime.strptime(dob_raw, "%Y-%m-%d")

            # Date of birth must be in the past
            if dob_parsed.date() >= datetime.now().date():
                return render_template(
                    "index.html",
                    error="Date of birth must be in the past.",
                    name=name,
                    dob=dob_raw,
                    max_date=today_str,
                )

            # Extract the day of the month as a two-digit string
            day_number = dob_parsed.day
            day_str = f"{day_number:02d}"

            # Extract the second digit (0 through 9)
            second_digit = int(day_str[1])

            # Retrieve the corresponding life path profile
            profile = LIFE_PATHS.get(second_digit)
            insight_message = profile.get("summary") if profile else LIFE_OUTPUTS[second_digit]

            return render_template(
                "index.html",
                name=name,
                dob=dob_raw,
                day_str=day_str,
                digit=second_digit,
                message=insight_message,
                profile=profile,
                max_date=today_str,
            )
        except ValueError:
            return render_template(
                "index.html",
                error="Invalid date format. Please select a valid date.",
                name=name,
                dob=dob_raw,
                max_date=today_str,
            )

    return render_template("index.html", max_date=today_str)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
