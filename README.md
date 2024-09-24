## Overview
This repository contains the solutions for the Python and Django technical assessment test. It demonstrates proficiency in Python web scraping, CSV processing, Django ORM queries, rate-limiting, and efficient algorithms.

## Setup

### Prerequisites
- Python 3.x
- Django 4.x
- `pip` to manage Python dependencies

### Installation

1. Clone the repository:

    ```bash
    git clone <repo here..> 
    cd vd-tech-assessment
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Django Setup (for q3_vd_project)

1. Navigate to the project directory (if applicable).
2. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

3. Create a superuser to access the Django admin panel (optional):

    ```bash
    python manage.py createsuperuser
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

### Running the Scripts

- **Q1 (Web Scraper)**: Executes the script to scrape articles from a news website (India Today[https://www.indiatoday.in/], in this case):

    ```bash
    cd q1_news_scraping
    python news_scraping.py
    ```

- **Q2 (CSV Cleaning)**: Run the script to clean the CSV file:

    ```bash
    cd q2_data_cleaning
    python data_cleaning.py
    ```


- **Q3 (Django view - top 5 customers)**: Run the script to check the view for the top 5 customers who have spent the most in the last 6 months:

    ```bash
    cd q3_vd_project
    python manage.py migrate 
    python manage.py loaddata users.json <!--to add dummy data as users in the database--!>
    python manage.py createsuperuser <!--for admin purpose and to add data which is optional--!>
    python manage.py runserver
    ```

- **Q4 (Rate Limiter)**: Test the request rate-limiting functionality:

    ```bash
    cd q4_request_rate_limiting
    python rate_limiter.py
    ```
- **Q5 (Aggregation)**: Test the aggregation of values in dictionaries:

    ```bash
    cd q5_aggregation
    python aggregator.py
    ```
- **Q6 (Removing Array Duplicates in O(1) Space)**: Outputs the duplicate of the list without using any extra space:

    ```bash
    cd q6_array_duplicate
    python rm_array_duplicate.py
    ```
### Usage

The project includes Django models and views for querying top customers based on order history. You can extend the view for front-end integration.

### Testing

To test the solutions:
1. For the Django model, use the Django shell or create a view.
2. For scripts like CSV processing, and rate limiting, simply run the Python files.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
