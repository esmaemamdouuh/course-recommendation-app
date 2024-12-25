# Course Recommendation Web App

## **Overview**
This project is a web-based course recommendation system designed for second-year students. It evaluates the student’s GPA, selected courses, and prerequisites to provide tailored recommendations for additional courses.

---

## **Features**
- Displays available courses along with their prerequisites and credit hours.
- Validates course selections based on GPA, prerequisites, and maximum credit hours allowed.
- Generates personalized course recommendations using Google Generative AI.
- User-friendly interface with form-based input for course selection and GPA.

---

## **Technology Stack**
- **Backend**: Python, Flask
- **Frontend**: HTML (rendered using Flask's `render_template`)
- **AI Integration**: Google Generative AI (Gemini 1.5 Flash model)
- **Data**: Hardcoded course catalog in Python
- **Hosting**: Flask development server (debug mode)

---

## **Installation Instructions**

### **Prerequisites**
- Python 3.8 or higher
- `pip` package manager
- API key for Google Generative AI

### **Steps**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/esmaemamdouuh/course-recommendation-app.git
   cd course-recommendation-app
   ```

2. **Install Dependencies**:
   ```bash
   pip install flask google-generativeai
   ```

3. **Set Up the API Key**:
   - Replace the placeholder API key in the `app.py` file:
     ```python
     genai.configure(api_key="AIzaSyAKnWwc0R1eamUpSTTT_LKkB34E9K-Yl90")
     ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Web App**:
   Open your browser and go to `http://127.0.0.1:5000`.

---

## **Usage Instructions**
1. On the home page, view the list of available courses.
2. Enter your GPA, select courses you wish to take, and list your previously completed courses.
3. Submit the form to receive:
   - A list of valid courses.
   - Invalid courses with reasons (e.g., missing prerequisites, exceeding credit hour limits).
   - Personalized course recommendations.

---

## **File Structure**
- `app.py`: Main Flask application.
- `templates/index.html`: Form for user input (GPA, course selection, etc.).
- `templates/recommend.html`: Displays results of the course review and recommendations.
- `static/`: Directory for static assets (CSS, JS, images) if used.

---

## **API Configuration**
The project integrates with Google Generative AI:
- Model: Gemini 1.5 Flash
- Configuration: Adjust `generation_config` in `app.py` for custom behavior (e.g., response length, temperature).

---

## **Future Enhancements**
- Add a database to dynamically manage course data.
- Implement user authentication for personalized experiences.
- Extend AI-generated recommendations with detailed explanations.
- Deploy the application to a hosting platform (e.g., AWS, Heroku).

---


