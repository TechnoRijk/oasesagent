# oasesagent

Automated LinkedIn Post Generator
Overview

The Automated LinkedIn Post Generator streamlines the process of creating, scheduling, and managing LinkedIn posts using advanced AI models and intelligent agents. It provides users with an intuitive interface to generate engaging content, manage their posting schedule, and monitor the performance of their posts. This system is beneficial for professionals, influencers, and companies looking to maintain an active and effective presence on LinkedIn with minimal manual effort.
Features

    User Authentication and Management: Create accounts and manage user profiles.
    Post Creation and Editing: Interface for creating and editing LinkedIn posts, including text and images.
    Automated Post Generation: Use AI models to generate text and images for LinkedIn posts.
    Post Scheduling: Schedule posts for future dates and times.
    Database Management: Store user data, posts, schedules, and settings securely.
    Task Scheduling: Manage tasks for scheduling posts using Celery and Redis.
    Content Management Integration: Integrate with Notion to fetch and update content.
    Interactive UI: Streamlit interface for content management and real-time updates.
    Deployment: Deploy the application using Docker and Heroku for scalability and consistency.
    Agent Integration: Implement hierarchical agents using CrewAI and Retrieval-Augmented Generation (RAG).

Architecture

The application consists of the following components:

    Frontend: Built with React.js for user interface.
    Backend: Developed with Flask to handle API requests, process data, and manage scheduling.
    Database: PostgreSQL to store user data, posts, schedules, and settings.
    AI Services: Uses models like Llama3, OpenGPT-4o for text generation, and Stable Diffusion XL for image generation.
    Task Queue: Uses Celery and Redis for managing tasks.
    External API Integrations: Integrates with Notion API for content management.
    Agents: Manages various tasks using CrewAI and RAG.

Setup Instructions
Prerequisites

    Node.js and npm (for frontend)
    Python 3.9+ (for backend)
    PostgreSQL (for database)
    Redis (for task queue)
    Docker and Docker Compose (for deployment)
    Heroku CLI (for deployment to Heroku)

Frontend Setup (React.js)

    Clone the repository and navigate to the frontend directory:

    sh

git clone <repository-url>
cd linkedin-post-generator

Install the required packages:

sh

npm install

Start the React development server:

sh

    npm start

Backend Setup (Flask)

    Create a virtual environment and activate it:

    sh

python3 -m venv venv
source venv/bin/activate

Install the required packages:

sh

pip install -r requirements.txt

Configure the database URI and other environment variables in app.py.

Initialize the database:

sh

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Start the Flask development server:

sh

    flask run

Task Queue Setup (Celery and Redis)

    Start the Redis server:

    sh

redis-server

Start the Celery worker:

sh

    celery -A worker.celery worker --loglevel=info

Streamlit Setup

    Install Streamlit:

    sh

pip install streamlit

Run the Streamlit app:

sh

    streamlit run streamlit_app.py

Deployment (Docker and Heroku)

    Build and run Docker containers:

    sh

docker-compose up --build

Deploy to Heroku:

sh

    heroku create linkedin-post-generator
    heroku addons:create heroku-postgresql:hobby-dev
    heroku addons:create heroku-redis:hobby-dev
    heroku stack:set container
    git push heroku main

Using the Application

    Dashboard: View recent posts and manage your content.
    Post Creation/Editing: Create new posts or edit existing ones, and schedule them for future publication.
    Settings: Manage your brand guidelines and RSS feeds.
    Streamlit Interface: Interact with AI models for content generation and scheduling.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
