# MCP English Text Improver

A Python-based MCP service that improves and corrects English text using OpenAI's GPT-4 model.

## Features

- GUI interface with input and output text areas
- AI-powered English language improvement
- Native English speaker-like text revision
- Simple and efficient workflow
- Real-time status updates

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd mcp-english-improver
```

2. Set up the virtual environment and install dependencies:

```bash
./setup.sh
```

Alternatively, you can set up the virtual environment manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows

# Install requirements
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your API keys:

```
OPENAI_API_KEY=your_openai_api_key
```

## Usage

1. Activate the virtual environment (if not already activated):

```bash
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

2. Run the application:

```bash
python src/main.py
```

3. In the GUI window:
   - Enter your text in the left text area
   - Click the "Improve Text" button
   - The improved text will appear in the right text area
   - Status updates will be shown below the button

## Project Structure

```
mcp-english-improver/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── gui.py
│   └── services/
│       ├── __init__.py
│       ├── clipboard_service.py
│       └── text_improvement_service.py
├── tests/
│   └── __init__.py
├── venv/              # Virtual environment directory
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── setup.sh
```

## License

MIT License
