# Telegram Bot

This is a simple Telegram bot built using the `python-telegram-bot` library. The bot can respond to commands such as `/start`, `/help`, and `/caps`.

## Features

- `/start`: Sends a welcome message.
- `/help`: Provides help information.
- `/caps <text>`: Converts the provided text to uppercase.

## Setup

### Prerequisites

- Python 3.11
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Telegram bot token and bot name:
    ```env
    TG_BOT_TOKEN=your-telegram-bot-token
    TG_BOT_NAME=your-bot-name
    ```

### Running the Bot

To run the bot, execute the following command:
```sh
python src/main.py
```

### Using Docker

1. Build the Docker image:
    ```sh
    docker build -t telegram-bot --build-arg TOKEN=your-telegram-bot-token .
    ```

2. Run the Docker container:
    ```sh
    docker run -d --name telegram-bot telegram-bot
    ```

## Usage

- Start a chat with your bot on Telegram.
- Use the `/start` command to receive a welcome message.
- Use the `/help` command to get help information.
- Use the `/caps <text>` command to convert text to uppercase.

## License

This project is licensed under the [MIT License](LICENSE).
