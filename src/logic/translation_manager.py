"""Translation practice logic and management."""

import random
from typing import List, Dict, Any, Optional
from src.utils.json_stream import JSONStreamReader


class TranslationManager:
    """
    Manages translation data and handles random selection for practice.
    Uses stream reading to avoid loading all data into memory.
    """

    def __init__(self, data_file_path: str):
        """
        Initialize the Translation Manager.

        Args:
            data_file_path: Path to the translations.json file
        """
        self.data_file_path = data_file_path
        self.translations: List[Dict[str, Any]] = []
        self._load_translations()

    def _load_translations(self) -> None:
        """Load translations from file using stream reader."""
        reader = JSONStreamReader(self.data_file_path)
        for translation in reader.stream():
            self.translations.append(translation)
        print(f"Loaded {len(self.translations)} translations from {self.data_file_path}")

    def get_random_translation(self) -> Optional[Dict[str, Any]]:
        """
        Get a random translation from the loaded data.

        Returns:
            A random translation dictionary or None if no translations exist
        """
        if not self.translations:
            return None
        return random.choice(self.translations)

    def get_translation_by_id(self, translation_id: int) -> Optional[Dict[str, Any]]:
        """
        Get a translation by its ID.

        Args:
            translation_id: The ID of the translation to retrieve

        Returns:
            The translation dictionary or None if not found
        """
        for translation in self.translations:
            if translation.get('id') == translation_id:
                return translation
        return None

    def get_available_languages(self) -> List[str]:
        """
        Get list of available language codes from the translations.

        Returns:
            List of language codes (e.g., ['en', 'de', 'sk'])
        """
        if not self.translations:
            return []

        languages = set()
        for translation in self.translations:
            languages.update(k for k in translation.keys() if k != 'id')

        return sorted(list(languages))

    def get_total_translations(self) -> int:
        """
        Get the total number of translations loaded.

        Returns:
            Count of translations
        """
        return len(self.translations)

    def validate_data(self) -> Dict[str, Any]:
        """
        Validate the loaded translation data structure.

        Returns:
            Dictionary with validation results
        """
        validation = {
            'valid': True,
            'total_translations': len(self.translations),
            'languages': self.get_available_languages(),
            'errors': []
        }

        for idx, translation in enumerate(self.translations):
            if 'id' not in translation:
                validation['errors'].append(f"Translation {idx}: Missing 'id' field")
                validation['valid'] = False

            if len(translation) < 2:
                validation['errors'].append(f"Translation {idx}: Missing language data")
                validation['valid'] = False

        return validation
