import json
import os
from typing import List


class Entry:
    """
    Класс Entry (запись), который имеет атрибуты:
    title (наименование)
    entries (опциональный) - записи (по умолчанию пустой лист) - будет хранить дочерние записи
    parent (опциональный) - родительская запись (по умолчанию None) - указывает на родительскую запись
    """

    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        """
        Вывод названия записи
        """
        return self.title

    def add_entry(self, entry):
        """Добавление новой записи в лист текущей записи"""
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(str(self), indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def json(self):
        res = {
            'title': self.title,
            'entries': [entry.json() for entry in self.entries]
        }
        return res

    def save(self, path):
        filename = f'{self.title}.json'
        full_path = os.path.join(path, filename)
        os.makedirs(path, exist_ok=True)
        data = self.json()
        with open(full_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_data):
        entry = Entry(json_data["title"])
        for sub_entry_json in json_data.get("entries", []):
            sub_entry = cls.from_json(sub_entry_json) if isinstance(sub_entry_json, dict) else sub_entry_json
            entry.add_entry(sub_entry)
        return entry

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls.from_json(data)


def print_with_indent(value, indent=0):
    print('\t' * indent + value)


# from resources import Entry
# import os

class EntryManager:
    def __init__(self, path):

        self.data_path: str = path
        self.entries: List[Entry] = []

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)

    def load(self):
        for filename in os.listdir(self.data_path):
            if filename.endswith('.json'):
                full_path = os.path.join(self.data_path, filename)
                entry = Entry.load(full_path)
                self.entries.append(entry)

    def add_entry(self, title: str):
        entry = Entry(title, "")
        self.entries.append(entry)
