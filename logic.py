from PyQt6.QtWidgets import *
from creator import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.role = 'none'
        self.race = 'none'
        self.gender = 'none'
        self.skills = 'none'
        self.traits = 'none'
        self.name = 'none'

        self.options.setCurrentIndex(0)

        self.confirm.clicked.connect(lambda : self.message(self.role, self.race, self.gender, self.skills, self.traits, self.name))

    def role_choice(self) -> str:
        """
        Method to select the role of the character.
        :return: Role of character.
        """
        if self.paladin.isChecked():
            self.role = 'Paladin'
            return self.role
        elif self.mage.isChecked():
            self.role = 'Mage'
            return self.role
        elif self.ranger.isChecked():
            self.role = 'Ranger'
            return self.role
        elif self.healer.isChecked():
            self.role = 'Healer'
            return self.role
        else:
            self.role = 'none'
            return self.role

    def race_choice(self) -> str:
        """
        Method to select the race of the character.
        :return: Race of character
        """
        if self.human.isChecked():
            self.race = 'Human'
            return self.race
        elif self.elf.isChecked():
            self.race = 'Elf'
            return self.race
        elif self.dwarf.isChecked():
            self.race = 'Dwarf'
            return self.race
        elif self.lizard.isChecked():
            self.race = 'Dwarf'
            return self.race
        else:
            self.race = 'none'
            return self.race

    def gender_choice(self) -> str:
        """
        Method to select the gender of the character.
        :return: Gender of character.
        """
        if self.male.isChecked():
            self.gender = 'Male'
            return self.gender
        elif self.female.isChecked():
            self.gender = 'Female'
            return self.gender
        elif self.none.isChecked():
            self.gender = ''
            return self.gender
        else:
            self.gender = 'none'
            return self.gender

    def skills_choice(self) -> str:
        """
        Method to select the base skill of the character.
        :return: Skill of character.
        """
        if self.lock.isChecked():
            self.skills = 'Locksmith'
            return self.skills
        elif self.pickpocket.isChecked():
            self.skills = 'Pickpocket'
            return self.skills
        elif self.sneak.isChecked():
            self.skills = 'Sneak'
            return self.skills
        elif self.perception.isChecked():
            self.skills = 'Perception'
            return self.skills
        elif self.barter.isChecked():
            self.skills = 'Barter'
            return self.skills
        else:
            self.skills = 'none'
            return self.skills

    def traits_choice(self) -> str:
        """
        Method to select the base trait of the character.
        :return: Trait of character
        """
        if self.cruel.isChecked():
            self.traits = 'Cruel'
            return self.traits
        elif self.greedy.isChecked():
            self.traits = 'Greedy'
            return self.traits
        elif self.jealous.isChecked():
            self.traits = 'Jealous'
            return self.traits
        elif self.righteous.isChecked():
            self.traits = 'Righteous'
            return self.traits
        else:
            self.traits = 'none'
            return self.traits

    def name_choice(self) -> str:
        """
        Method to select the name of the character.
        :return: Name of character.
        """
        self.name = self.lineEdit.text()
        return self.name

    def message(self, role, race, gender, skills, traits, name):
        self.role_choice()
        self.race_choice()
        self.gender_choice()
        self.skills_choice()
        self.traits_choice()
        self.name_choice()
        if self.role == 'none':
            self.label.setText('Please select a Class')
        elif self.race == 'none':
            self.label.setText('Please select a Race')
        elif self.gender == 'none':
            self.label.setText('Please select a Gender')
        elif self.skills == 'none':
            self.label.setText('Please select a Skill')
        elif self.traits == 'none':
            self.label.setText('Please select a Trait')
        elif self.name == "":
            self.label.setText('Please choose a Name')
        else:
            self.label.setText(f'{self.name} is a {self.gender} {self.race} who lives life as a {self.role}.\n{self.name} is a {self.traits} creature who has oddly good {self.skills} abilities.')

