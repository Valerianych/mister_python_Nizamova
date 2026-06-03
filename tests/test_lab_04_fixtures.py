import shutil
import tempfile
import unittest
from pathlib import Path

from labtools.notes import NotesStorage


class TestNotesStorage(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir)
        self.file_path = Path(self.temp_dir) / "notes.txt"
        self.storage = NotesStorage(self.file_path)

    def test_empty_storage_returns_empty_list(self):
        self.assertEqual(self.storage.read_notes(), [])

    def test_add_one_note(self):
        self.storage.add_note("first note")
        self.assertEqual(self.storage.read_notes(), ["first note"])

    def test_add_several_notes(self):
        self.storage.add_note("one")
        self.storage.add_note("two")
        self.assertEqual(self.storage.read_notes(), ["one", "two"])


if __name__ == "__main__":
    unittest.main()
