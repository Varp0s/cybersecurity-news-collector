# Cybersecurity News Collector

## Overview

note: the outputs are set to return for the results, you need to print or add the function or helper to print to the database.

The Cybersecurity News Collector is a Python-based application designed to aggregate the latest cybersecurity news from various reputable sources. It continuously crawls multiple websites to fetch the most recent articles, ensuring you stay updated with the latest developments in the cybersecurity world.

## Features

- Aggregates news from multiple cybersecurity websites.
- Continuously updates to provide the latest articles.
- Logs the crawling process for monitoring and debugging.

## Requirements

- Python 3.6+
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/cybersecurity-news-collector.git
    cd cybersecurity-news-collector
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you are in the virtual environment:

    ```sh
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

2. Run the main script to start crawling:

    ```sh
    python main.py
    ```

## Logging

The application uses Python's built-in logging module to log the crawling process. Logs can be found in the logs directory.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

