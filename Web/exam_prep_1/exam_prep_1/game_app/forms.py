from django import forms

from exam_prep_1.game_app.models import Person, Game


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('email', 'age', 'password')


class CreatePersonForm(ProfileBaseForm):
    pass


class EditPersonForm(ProfileBaseForm):
    class Meta:
        model = Person
        fields = '__all__'


class DeletePersonForm(ProfileBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Game.objects \
                .all() \
                .delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class CreateGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
