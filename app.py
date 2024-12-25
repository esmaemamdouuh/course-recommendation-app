from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import re
app = Flask(__name__)


# Configure the API key
genai.configure(api_key="AIzaSyAg9LG2pOcjPu9yabWGFRP-Y3kqswm8xuA")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config)


courses = {
    "CS201": {"name": "Discrete Structures", "prerequisites": ["MATH102"], "hours": 3, "level": 2},
    "CS241": {"name": "Object-Oriented Programming", "prerequisites": ["CS141"], "hours": 3, "level": 2},
    "HUM232": {"name": "Technical Writing", "prerequisites": ["HUM111"], "hours": 2, "level": 2},
    "IS221": {"name": "Project Management", "prerequisites": ["IT101"], "hours": 2, "level": 2},
    "MATH201": {"name": "Mathematics III", "prerequisites": ["MATH102"], "hours": 3, "level": 2},
    "HUM231": {"name": "Business Administration", "prerequisites": [], "hours": 2, "level": 2},
    "EE201": {"name": "Digital Signal Processing", "prerequisites": ["MATH201"], "hours": 3, "level": 2},
    "IS201": {"name": "Foundations of Information Systems", "prerequisites": ["IT101"], "hours": 3, "level": 2},
    "CS141": {"name": "Programming Fundamentals", "prerequisites": [], "hours": 3, "level": 1},
    "MATH102": {"name": "Mathematics II", "prerequisites": [], "hours": 3, "level": 1},
    "HUM111": {"name": "English Language I", "prerequisites": [], "hours": 2, "level": 1},
    "IT101": {"name": "IT Fundamentals", "prerequisites": [], "hours": 3, "level": 1}
}



def generate_recommendation( gpa, selected_courses):
    recommendations = ""
    prompt = f"Summary in 2 line  Recommend courses for a second year student with a GPA of {gpa} who has already taken {', '.join(selected_courses)}.provide personalized course recommendations and advice"
    response = model.generate_content(prompt)

    # Use a more concise regular expression to remove unwanted characters
    cleaned_recommendations = re.sub(r'[#\*,\[\]]', '', response.text)

    return cleaned_recommendations



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", courses=courses)


@app.route("/review", methods=["POST"])
def review():
    level = int(request.form["level"])
    gpa = float(request.form["gpa"])
    selected_courses = request.form.getlist("courses")
    previous_courses = request.form.getlist("previous_courses")

    max_hours = 12 if gpa < 2 else 18
    valid_courses = []
    invalid_courses = []
    total_hours = 0


    for course in selected_courses:
        if course not in courses:
            invalid_courses.append(f"{course}: Course not found")
            continue

        course_data = courses[course]
        prerequisites = course_data["prerequisites"]

        if course_data["level"] == 2:
            if all(req in selected_courses or req in previous_courses for req in prerequisites):
                total_hours += course_data["hours"]
                if total_hours <= max_hours:
                    valid_courses.append(course_data["name"])
                else:
                    invalid_courses.append(
                        f"{course_data['name']}: Exceeds the maximum allowed hours ({max_hours} hours)")
                    total_hours -= course_data["hours"]
            else:
                missing_reqs = [req for req in prerequisites if
                                req not in selected_courses and req not in previous_courses]
                invalid_courses.append(f"{course_data['name']}: Missing prerequisites ({', '.join(missing_reqs)})")
        else:
            total_hours += course_data["hours"]
            if total_hours <= max_hours:
                valid_courses.append(course_data["name"])
            else:
                invalid_courses.append(f"{course_data['name']}: Exceeds the maximum allowed hours ({max_hours} hours)")
                total_hours -= course_data["hours"]

    recommendations = generate_recommendation( gpa, selected_courses)

    return render_template(
        "recommend.html",
        valid_courses=valid_courses,
        invalid_courses=invalid_courses,
        total_hours=total_hours,
        gpa=gpa,
        recommendations= recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
