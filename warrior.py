class Warrior:
    ranks = ["Pushover","Novice","Fighter","Warrior","Veteran","Sage",
             "Elite","Conqueror","Champion","Master","Greatest"]
    
    def __init__(self):
        self.experience = 100
        self.level = 1
        self.rank = "Pushover"
        self.achievements = []
        
    def _update_stats(self):
        self.experience = min(10000, self.experience)
        self.level = min(100, self.experience // 100)
        idx = 10 if self.level == 100 else self.level // 10
        self.rank = self.ranks[idx]
        
    def battle(self, enemy_level):
        if enemy_level > 100 or enemy_level < 1:
            return "Invalid level"
        
        my_lvl = self.level
        my_rank_idx = 10 if my_lvl == 100 else my_lvl // 10
        enemy_rank_idx = 10 if enemy_level == 100 else enemy_level // 10
        
        if enemy_rank_idx > my_rank_idx and enemy_level - my_lvl >= 5:
            return "You've been defeated"
        
        if enemy_level <= my_lvl - 2:
            gain = 0
        elif enemy_level == my_lvl - 1:
            gain = 5
        elif enemy_level == my_lvl:
            gain = 10
        else:
            diff = enemy_level - my_lvl
            gain = 20 * diff * diff
        
        self.experience += gain
        self._update_stats()
        
        if my_lvl >= enemy_level + 2:
            return "Easy fight"
        elif my_lvl == enemy_level or my_lvl == enemy_level + 1:
            return "A good fight"
        else:
            return "An intense fight"

    def training(self, training_data):
        desc, xp_gain, min_lvl = training_data
        if self.level < min_lvl:
            return "Not strong enough"
        self.experience += xp_gain
        self._update_stats()
        self.achievements.append(desc)
        return desc
