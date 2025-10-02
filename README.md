# PUCE Manabí Discord Bot

A helpful Discord bot for the Pontificia Universidad Católica del Ecuador Sede Manabí (PUCEM), designed to provide students and prospective applicants with easy access to important university information.

## 📖 Overview

This bot serves as a virtual assistant for the PUCE Manabí community on Discord. It offers a user-friendly interface with buttons and dropdown menus to navigate through various information categories, from academic programs to contact details. The main goal is to provide instant, organized, and accessible information to anyone interested in the university.

## ✨ Features

- **Interactive Menus**: Utilizes Discord UI components like buttons and select menus for an intuitive and modern user experience.
- **Contact Information**: Quickly retrieve contact details, including WhatsApp, email, and phone numbers.
- **Academic Programs**:
  - Browse a comprehensive list of undergraduate careers with links to the official university page and relevant Instagram accounts.
  - Explore postgraduate specializations and master's degrees with direct links for more information.
- **Admissions**: Get direct links to the enrollment process for undergraduate, postgraduate, and PUCE Tec programs.
- **Scholarships**: Find information and links regarding available scholarships.
- **Campus Information**: Easily find addresses and Google Maps links for the Portoviejo and Manta campuses.
- **Author Credits**: A special section to acknowledge the creators of the bot.

## 🚀 How to Use

1.  Invite the bot to your Discord server.
2.  In a channel where the bot has read and write permissions, type `hello` or `hola`.
3.  The bot will respond with a welcome message and a main menu of options.
4.  Use the buttons and dropdown menus to navigate and find the information you need. All interactions are ephemeral to keep the channel clean.

## 🛠️ Setup for Development

To run this bot locally for development or testing, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/castro-bot/Discord-Bot.git
    cd Discord-Bot
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**

    - Create a file named `.env` in the root directory of the project.
    - Add your Discord bot token to the `.env` file:
      ```
      TOKEN=YOUR_DISCORD_BOT_TOKEN
      ```

5.  **Run the bot:**
    ```bash
    python Discord_Bot.py
    ```

## 📦 Dependencies

- [discord.py](https://github.com/Rapptz/discord.py) - A modern, easy-to-use, feature-rich, and async-ready API wrapper for Discord.
- [python-dotenv](https://github.com/theskumar/python-dotenv) - To manage environment variables for sensitive information like API tokens.

## ✍️ Authors

This bot was created with ❤️ by:

- Adolfo Castro 🎷
- Axel Hernández 🥋
- Paula Márquez ❤️
- Leonela Sornoza 🎹
