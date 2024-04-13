class HubPlayer:
    
    def __init__(self, name,email,username, player_id):
        self.name = name
        self.email = email
        self.username = username
        self.player_id = player_id
        
    def update_account(self, name=None, email=None, username=None):
        if name:
            self.name = name
        if email: 
            self.email = email
        if username:
            self.username = username
        
class ActivePlayer(HubPlayer):
    
    def __init__(self, name,email,username, player_id, points, character_ids, selected_charachter_id):
        super().__init__(name, email, username, player_id)
        self.points = points
        self.character_id = character_ids
        self.selected_character_id = selected_charachter_id

class Character:
        
    def __init__(self, name, attribute, skill_level, abilities):
        self.name = name
        self.attribute = attribute
        self.skill_level = skill_level

class Troll(Character):
    def __init__(self, name, type, skill_level, abilities, weapon):
        super().__init__(name, type, skill_level, abilities)
        self.weapon = weapon

    def update_char(self, type=None, skill_level=None, abilities=None, weapon=None):
        if type:
            self.type = type
        if skill_level:
            self.skill_level = skill_level
        if abilities:
            self.abilities = abilities
        if weapon:
            self.weapon = weapon
            
