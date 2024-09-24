# Technical Assessment Test: Python and Django

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
    git clone https://github.com/AbhinavMangalore16/vd-tech-assessment.git
    cd assessment-test
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

### Django Setup

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

- **Q1 (Web Scraper)**: Execute the script to scrape articles:

    ```bash
    python scrape_articles.py
    ```

- **Q2 (CSV Cleaning)**: Run the script to clean the CSV file:

    ```bash
    python clean_csv.py
    ```

- **Q4 (Rate Limiter)**: Test the rate-limiting functionality:

    ```bash
    python rate_limiter.py
    ```

### Usage

The project includes Django models and views for querying top customers based on order history. You can extend the view for front-end integration.

### Testing

To test the solutions:
1. For the Django model, use the Django shell or create a view.
2. For scripts like CSV processing, and rate limiting, simply run the Python files.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
