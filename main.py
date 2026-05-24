"""
Entry point for the German Translation Practice Application.
"""

import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from src.logic.translation_manager import TranslationManager
from src.ui.terminal_ui import TerminalUI


def main():
    """Main entry point for the application."""
    # Path to the translations data file
    # Concat the path to ensure it works regardless of the current working directory, 
    # this approach is allowed  because of pathlib usage and is more robust than hardcoding a relative path.
    data_file_path = Path(__file__).parent / "data" / "translations.json"

    if not data_file_path.exists():
        print(f"Error: translations.json not found at {data_file_path}")
        sys.exit(1)

    try:
        # Initialize translation manager with stream reading
        manager = TranslationManager(str(data_file_path))

        # Validate the loaded data
        validation = manager.validate_data()
        if not validation['valid']:
            print("Warning: Validation issues found:")
            for error in validation['errors']:
                print(f"  - {error}")

        print(f"Loaded {validation['total_translations']} translations")
        print(f"Available languages: {', '.join(validation['languages'])}")

        # Initialize and run the UI
        ui = TerminalUI(manager)
        ui.run()

    except FileNotFoundError as e:
        print(f"Error: Could not find data file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
