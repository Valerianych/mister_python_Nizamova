from pathlib import Path


class NotesStorage:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def add_note(self, text):
        with self.file_path.open("a", encoding="utf-8") as file:
            file.write(text + "\n")

    def read_notes(self):
        if not self.file_path.exists():
            return []
        with self.file_path.open("r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
