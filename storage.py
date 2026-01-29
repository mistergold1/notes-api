import json
import os


class Storage:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self.notes, f, indent=2)

    def get_all(self):
        return self.notes

    def add(self, text):
        note = {
            "id": len(self.notes) + 1,
            "text": text
        }
        self.notes.append(note)
        self._save()
        return note

    def delete(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                self.notes.remove(note)
                self._save()
                return True
        return False
