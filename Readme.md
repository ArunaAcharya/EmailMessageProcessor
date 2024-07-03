## Email Complaint Processing System

### Overview

This system automatically processes emails using IMAP, identifies if the email is a complaint using NLP, and stores all relevant details in a database.

### Features

- **IMAP Email Processing**: Connects to an email server to retrieve emails.
- **NLP Complaint Identification**: Utilizes Natural Language Processing (NLP) to analyze the email content and determine if it is a complaint.
- **Database Storage**: Stores email details and complaint status in a database.

### Requirements

- Python 3.8+
- IMAP Client Library
- NLP Library (spaCy, NLTK, etc.)
- Database (MySQL, PostgreSQL, etc.)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-repo/email-complaint-processing.git
    cd email-complaint-processing
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
