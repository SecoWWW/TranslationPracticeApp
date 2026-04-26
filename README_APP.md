# German Translation Practice Application

A Python 3 application to help practice German language through translation exercises.

## Features

- **Stream-based JSON reading**: Efficient file handling without loading entire file into memory
- **Random word selection**: Practice with randomized translation pairs
- **Layered architecture**: Clean separation between UI and business logic
- **Terminal UI**: Interactive terminal-based interface
- **Multi-language support**: Easily configure source and target languages
- **Session tracking**: Track score and accuracy during practice sessions

## Project Structure

```
src/
├── logic/
│   ├── __init__.py
│   └── translation_manager.py    # Core translation logic and random selection
├── ui/
│   ├── __init__.py
│   └── terminal_ui.py            # Terminal-based user interface
├── utils/
│   ├── __init__.py
│   └── json_stream.py            # Stream-based JSON reader
└── __init__.py

main.py                             # Application entry point
requirements.txt                    # Python dependencies (none required)
```

## Running the Application

```bash
# Navigate to the project directory
cd TranslationPracticeApp

# Run the application
python main.py
```

## How to Use

1. **Start Practice Session**: Select option 1 to begin a practice session. Choose the number of questions.
2. **View Statistics**: Select option 2 to see your current session score and accuracy.
3. **Settings**: Select option 3 to configure source and target languages.
4. **Exit**: Select option 4 to quit the application.

## JSON Data Format

The `translations.json` file should follow this format:

```json
[
    {
        "id": 1,
        "en": "Hello",
        "de": "Hallo",
        "sk": "Ahoj"
    },
    {
        "id": 2,
        "en": "Goodbye",
        "de": "Auf Wiedersehen",
        "sk": "Zbohom"
    }
]
```

## Architecture

### Logic Layer (`logic/translation_manager.py`)
- `TranslationManager`: Manages translation data and provides random selection
- Uses stream reading to load translations efficiently
- Provides methods to:
  - Get random translations
  - Retrieve translations by ID
  - Get available languages
  - Validate data structure

### UI Layer (`ui/terminal_ui.py`)
- `TerminalUI`: Handles all user interaction
- Independent of data source (can be easily replaced with web UI, GUI, etc.)
- Features:
  - Main menu navigation
  - Practice session management
  - Statistics display
  - Settings configuration

### Utils (`utils/json_stream.py`)
- `JSONStreamReader`: Efficiently reads JSON arrays from files
- Yields one object at a time (streaming approach)
- Prevents memory issues with large translation files

## Future Enhancements

- Add persistence for user statistics/progress
- Implement spaced repetition algorithm
- Add word categories/difficulty levels
- Support for audio pronunciation
- Web-based UI using Flask/FastAPI
- Database backend for larger datasets
- Leaderboard functionality

## Requirements

- Python 3.7+
- No external dependencies (uses only Python standard library)

## License

See LICENSE file in the project root.
