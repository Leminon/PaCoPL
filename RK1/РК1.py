from operator import itemgetter


class ProgrammingLanguage:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class Library:
    def __init__(self, id: int, name: str, function_count: int,
                 language_id: int):
        self.id = id
        self.name = name
        self.function_count = function_count
        self.language_id = language_id

class LibraryLanguage:
    def __init__(self, library_id: int, language_id: int):
        self.library_id = library_id
        self.language_id = language_id

languages = [
    ProgrammingLanguage(id=1, name="Python"),
    ProgrammingLanguage(id=2, name="Java"),
    ProgrammingLanguage(id=3, name="Язык JavaScript"),
    ProgrammingLanguage(id=4, name="Язык C#"),]

libraries = [
    Library(id=1, name="Алгоритмы", function_count=121, language_id=1),
    Library(id=2, name="Асинхронные задачи", function_count=80, language_id=1),
    Library(id=3, name="Spring", function_count=200, language_id=2),
    Library(id=4, name="Адаптер", function_count=100, language_id=4),
    Library(id=5, name="React", function_count=50, language_id=3),]

library_language_links = [
    LibraryLanguage(library_id=1, language_id=1),
    LibraryLanguage(library_id=1, language_id=4),
    LibraryLanguage(library_id=2, language_id=1),
    LibraryLanguage(library_id=3, language_id=2),
    LibraryLanguage(library_id=4, language_id=4),
    LibraryLanguage(library_id=5, language_id=3),]



one_to_many = [
    (language.name, library.name, library.function_count)
    for language in languages for library in libraries
    if library.language_id == language.id]


many_to_many_temp = [
    (library.name, link.language_id)
    for library in libraries for link in library_language_links
    if library.id == link.library_id]
many_to_many = [
    (library_name, language.name)
    for library_name, language_id in many_to_many_temp
    for language in languages if language.id == language_id]


print("\nЯзыки со словом 'язык' в названии и их библиотеки")
res_1 = {}
for language_name, library_name, _ in one_to_many:
    if "язык" in language_name.lower():
        res_1.setdefault(language_name, []).append(library_name)
print(res_1)


print("\nСреднее число функций библиотек по языкам")
res_2_unsorted = []
for language in languages:
    counts = [count for language_name, _, count in one_to_many
              if language_name == language.name]
    if counts:
        res_2_unsorted.append(
            (language.name, round(sum(counts) / len(counts), 2))
        )
res_2 = sorted(res_2_unsorted, key=itemgetter(1))
print(res_2)


print("\nЗапрос 3: Библиотеки на букву 'А' и их языки")
res_3 = {}
for library_name, language_name in many_to_many:
    if library_name.startswith("А"):
        res_3.setdefault(library_name, []).append(language_name)
print(res_3)
