# Project Specification: OOHLIFE - A Flask Web Application

## 1. Project Overview
**OOHLIFE** is a simple, web-based Python application built with Flask. It acts as a personalized life guide. The app features a web UI built with HTML and CSS that prompts the user for their name and date of birth. The backend extracts a specific digit from the day of the birth date, maps it to a curated list of 10 distinct life insights (outputs 0 through 9), and displays a personalized message on the web page.

## 2. Technical Stack & Requirements
- **Backend Framework:** Python 3.8+ with Flask (`flask`, `request`, `render_template`)
- **Frontend UI:** HTML5 and CSS3 (simple, responsive design)
- **Built-in Modules:** `datetime` (for parsing and validating date inputs)
- **Architecture:** Standard Flask MVC pattern (`app.py` for logic and routing, `templates/` folder for HTML views).

## 3. Core Logic & Algorithm Specification
1. **User Input Collection (via Web UI):**
   - Accept user inputs through an HTML form using the `POST` method.
   - Inputs required: `name` (text field) and `dob` (HTML date picker field, format `YYYY-MM-DD`).
2. **Date Parsing & Validation (Backend):**
   - Parse the incoming `dob` from `request.form` using `datetime.strptime(dob, "%Y-%m-%d")`.
   - Handle `ValueError` gracefully, returning an error message to the UI if parsing fails.
3. **Digit Extraction & Indexing Rule:**
   - Extract the day of the month: `day_number = dob.day`.
   - Format the day as a two-digit string with leading zeros: `day_str = f"{day_number:02d}"`.
   - Extract the **second digit** of the day string: `second_digit = int(day_str[1])`.
     - *Edge Case Handled:* If the day is `10`, `day_str` is `"10"`, so `day_str[1]` is `'0'`, resulting in `0`.
     - This guarantees a numeric range of `0` through `9`.
4. **Message Retrieval:**
   - Maintain a list of exactly 10 output strings (indices `0` through `9`).
   - Retrieve `outputs[second_digit]` and pass it back to the template via `render_template`.

## 4. Phased Implementation Plan for LLM Execution

### Phase 1: Flask Application Setup & Routing
- **Objective:** Establish the main entry point and basic web server structure.
- **Tasks:**
  - Create `app.py`.
  - Initialize the Flask app `app = Flask(__name__)`.
  - Define a single route `/` that handles both `GET` and `POST` methods.
  - On `GET`, return `render_template('index.html')`.

### Phase 2: Frontend UI Construction (HTML & CSS)
- **Objective:** Build a clean, user-friendly web interface to collect data and display results.
- **Tasks:**
  - Create a `templates` directory and add `index.html`.
  - Write an HTML form with inputs for Name (`type="text"`) and Date of Birth (`type="date"`, which automatically forces valid `YYYY-MM-DD` formatting in modern browsers).
  - Add basic, modern CSS (either via a `<style>` block in the head or a `static/style.css` file) to center the form, style the submit button, and make it visually appealing.
  - Implement Jinja2 templating variables (`{{ message }}`, `{{ error }}`) to conditionally display results or errors below the form.

### Phase 3: Algorithm, Logic Layer & Output Data
- **Objective:** Implement the digit-extraction logic and the life output messages in `app.py`.
- **Tasks:**
  - Define the `LIFE_OUTPUTS` list containing 10 distinct, motivational strings.
  - Inside the `/` route's `POST` block, retrieve `request.form.get('name')` and `request.form.get('dob')`.
  - Implement the date parsing and second-digit extraction algorithm.
  - Map the extracted digit (0-9) to `LIFE_OUTPUTS`.

### Phase 4: Integration, Testing & Error Handling
- **Objective:** Connect the frontend and backend smoothly, ensuring robust error handling.
- **Tasks:**
  - Pass the user's name, the extracted day, and the corresponding life message back into `render_template('index.html', name=name, message=message)`.
  - Wrap the backend parsing in a `try...except ValueError` block, passing an `error="Invalid Date"` context back to the template if it fails.
  - Test edge cases: Date endings with 0 (e.g., the 10th or 20th), single-digit days (e.g., the 5th), and the 31st to ensure the 0-9 index always falls safely within the 10-item list constraint.
