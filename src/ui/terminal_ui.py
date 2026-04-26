"""Terminal-based user interface for the translation practice application."""

from typing import Optional, Dict, Any
from src.logic.translation_manager import TranslationManager


class TerminalUI:
    """
    Terminal UI for the translation practice application.
    Handles user interaction and displays translation practice sessions.
    """

    def __init__(self, translation_manager: TranslationManager):
        """
        Initialize the Terminal UI.

        Args:
            translation_manager: Instance of TranslationManager
        """
        self.manager = translation_manager
        self.source_language = 'en'
        self.target_language = 'de'
        self.score = 0
        self.total_questions = 0

    def clear_screen(self) -> None:
        """Clear the terminal screen."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self) -> None:
        """Display application header."""
        print("\n" + "=" * 60)
        print("  German Translation Practice Application".center(60))
        print("=" * 60 + "\n")

    def display_menu(self) -> None:
        """Display main menu options."""
        print("\nMain Menu:")
        print("1. Start Practice Session")
        print("2. View Statistics")
        print("3. Settings")
        print("4. Exit")
        print("-" * 40)

    def display_settings_menu(self) -> None:
        """Display settings menu."""
        languages = self.manager.get_available_languages()
        print("\nSettings:")
        print(f"Available languages: {', '.join(languages)}")
        print(f"Source language: {self.source_language}")
        print(f"Target language: {self.target_language}")
        print("\n1. Set source language")
        print("2. Set target language")
        print("3. Back to main menu")
        print("-" * 40)

    def display_statistics(self) -> None:
        """Display current session statistics."""
        print("\nSession Statistics:")
        print(f"Total Questions: {self.total_questions}")
        print(f"Correct Answers: {self.score}")
        if self.total_questions > 0:
            accuracy = (self.score / self.total_questions) * 100
            print(f"Accuracy: {accuracy:.1f}%")
        print("-" * 40)

    def get_user_input(self, prompt: str) -> str:
        """
        Get user input with validation.

        Args:
            prompt: The prompt to display

        Returns:
            User input as a string
        """
        return input(prompt).strip()

    def display_translation_question(self, translation: Dict[str, Any]) -> None:
        """
        Display a translation question.

        Args:
            translation: Translation dictionary containing language pairs
        """
        source_word = translation.get(self.source_language, 'N/A')
        target_word = translation.get(self.target_language, 'N/A')

        print("\n" + "-" * 40)
        print(f"Translate the following {self.source_language.upper()} word to {self.target_language.upper()}:")
        print(f"\n  >>> {source_word} <<<\n")

    def check_answer(self, user_answer: str, correct_answer: str) -> bool:
        """
        Check if the user's answer is correct.

        Args:
            user_answer: The user's provided answer
            correct_answer: The correct translation

        Returns:
            True if correct, False otherwise
        """
        is_correct = user_answer.lower().strip() == correct_answer.lower().strip()
        
        if is_correct:
            print("✓ Correct!")
            self.score += 1
        else:
            print(f"✗ Incorrect. The correct answer is: {correct_answer}")

        self.total_questions += 1
        return is_correct

    def run_practice_session(self, num_questions: int = 5) -> None:
        """
        Run a practice session with the specified number of questions.

        Args:
            num_questions: Number of questions in the session
        """
        self.clear_screen()
        self.display_header()
        print(f"Starting practice session ({num_questions} questions)")
        print(f"Source: {self.source_language.upper()} → Target: {self.target_language.upper()}\n")

        for i in range(num_questions):
            translation = self.manager.get_random_translation()

            if translation is None:
                print("No translations available!")
                return

            self.display_translation_question(translation)
            user_answer = self.get_user_input("Your answer: ")
            correct_answer = translation.get(self.target_language, '')

            self.check_answer(user_answer, correct_answer)
            print()

        print("\n" + "=" * 40)
        print("Session Complete!")
        self.display_statistics()
        print("=" * 40)

    def run(self) -> None:
        """Main application loop."""
        while True:
            self.clear_screen()
            self.display_header()

            # Display app info
            print(f"Loaded {self.manager.get_total_translations()} translations")
            print(f"Available languages: {', '.join(self.manager.get_available_languages())}\n")

            self.display_menu()
            choice = self.get_user_input("Enter your choice (1-4): ")

            if choice == '1':
                try:
                    num_q = self.get_user_input("How many questions? (default 5): ")
                    num_questions = int(num_q) if num_q else 5
                    self.run_practice_session(num_questions)
                except ValueError:
                    print("Invalid input. Using default of 5 questions.")
                    self.run_practice_session(5)
                self.get_user_input("\nPress Enter to continue...")

            elif choice == '2':
                self.clear_screen()
                self.display_header()
                self.display_statistics()
                self.get_user_input("\nPress Enter to continue...")

            elif choice == '3':
                self._handle_settings_menu()

            elif choice == '4':
                print("\nThank you for practicing! Auf Wiedersehen!")
                break

            else:
                print("Invalid choice. Please try again.")
                self.get_user_input("Press Enter to continue...")

    def _handle_settings_menu(self) -> None:
        """Handle the settings menu."""
        while True:
            self.clear_screen()
            self.display_header()
            self.display_settings_menu()
            choice = self.get_user_input("Enter your choice (1-3): ")

            if choice == '1':
                self._set_source_language()
            elif choice == '2':
                self._set_target_language()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
                self.get_user_input("Press Enter to continue...")

    def _set_source_language(self) -> None:
        """Allow user to set the source language."""
        languages = self.manager.get_available_languages()
        print(f"\nAvailable languages: {', '.join(languages)}")
        lang = self.get_user_input("Enter source language code: ").lower()
        if lang in languages:
            self.source_language = lang
            print(f"Source language set to: {lang}")
        else:
            print(f"Invalid language. Please use one of: {', '.join(languages)}")
        self.get_user_input("Press Enter to continue...")

    def _set_target_language(self) -> None:
        """Allow user to set the target language."""
        languages = self.manager.get_available_languages()
        print(f"\nAvailable languages: {', '.join(languages)}")
        lang = self.get_user_input("Enter target language code: ").lower()
        if lang in languages:
            self.target_language = lang
            print(f"Target language set to: {lang}")
        else:
            print(f"Invalid language. Please use one of: {', '.join(languages)}")
        self.get_user_input("Press Enter to continue...")
