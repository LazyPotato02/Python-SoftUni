from mammal.project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def test_mammal_init_should_create_proper_obj(self):
        name = 'Test'
        mammal_type = 'Dog'
        sound = 'bark'
        mammal = Mammal(name, mammal_type, sound)
        self.assertEqual(name, mammal.name)
        self.assertEqual(mammal_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_mammal_make_sound_returns_proper_result(self):
        name = 'Test'
        mammal_type = 'Dog'
        sound = 'bark'
        mammal = Mammal(name, mammal_type, sound)

        actual_result = mammal.make_sound()
        expected_result = f"{name} makes {sound}"

        self.assertEqual(actual_result, expected_result)

    def test_mammal_get_kingdom_returns_animals(self):
        name = 'Test'
        mammal_type = 'Dog'
        sound = 'bark'
        mammal = Mammal(name, mammal_type, sound)

        actual_result = mammal.get_kingdom()
        expected_result = f"animals"

        self.assertEqual(actual_result, expected_result)

    def test_info_returns_proper_type_of_animal(self):
        name = 'Test'
        mammal_type = 'Dog'
        sound = 'bark'
        mammal = Mammal(name, mammal_type, sound)

        actual_result = mammal.info()
        expected_result = f"{name} is of type {mammal_type}"

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    main()
