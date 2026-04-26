"""JSON stream reader for efficient file handling."""

import json
from typing import Iterator, Dict, Any


class JSONStreamReader:
    """
    Reads JSON array files and yields objects one at a time.
    Efficiently handles JSON files containing arrays of objects.
    """

    def __init__(self, file_path: str):
        """
        Initialize the JSON stream reader.

        Args:
            file_path: Path to the JSON file containing an array of objects
        """
        self.file_path = file_path

    def stream(self) -> Iterator[Dict[str, Any]]:
        """
        Stream JSON objects from the file one at a time without loading entire file.
        Reads incrementally and yields complete objects as they're parsed.

        Yields:
            Dict containing a single JSON object from the array

        Raises:
            json.JSONDecodeError: If the file is not valid JSON
            FileNotFoundError: If the file does not exist
        """
        with open(self.file_path, 'r', encoding='utf-8') as f:
            decoder = json.JSONDecoder()
            buffer = ""
            
            for line in f:
                buffer += line
                
                # Try to extract complete JSON objects from buffer
                while buffer:
                    buffer = buffer.lstrip()
                    
                    # Skip array brackets and commas
                    if buffer and buffer[0] in '[,':
                        buffer = buffer[1:]
                        continue
                    
                    # Check for end of array
                    if buffer and buffer[0] == ']':
                        return
                    
                    # Skip whitespace
                    if buffer and buffer[0] in ' \n\t\r':
                        buffer = buffer[1:]
                        continue
                    
                    # Try to decode a JSON object
                    if buffer and buffer[0] == '{':
                        try:
                            obj, idx = decoder.raw_decode(buffer)
                            yield obj
                            buffer = buffer[idx:]
                        except json.JSONDecodeError:
                            # Incomplete object, read more
                            break
                    else:
                        break
