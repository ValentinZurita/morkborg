abilities_score = {
						    (1, 4): -3,
						    (5, 6): -2,
						    (7, 8): -1,
						    (9, 12): 0,
						    (13, 14): 1,
						    (15, 16): 2,
						    (17, 20): 3
				   }

initial_equipment = {
						"1st" : [
								    {"name": "Nothing", "description": ""},
								    {"name": "Nothing", "description": ""},
								    {"name": "Backpack", "description": "For 7 normal-sized items"},
								    {"name": "Sack", "description": "For 10 normal-sized items"},
								    {"name": "Small wagon", "description": ""},
								    {"name": "Donkey", "description": ""}
								],
						"2nd" : [
								    {"name": "Rope", "description": "30 feet"},
								    {"name": "Torches", "description": "Presence + 4 torches"},
								    {"name": "Lantern", "description": "With oil for Presence + 6 hours"},
								    {"name": "Magnesium strip", "description": ""},
								    {"name": "Unclean scroll", "description": ""},
								    {"name": "Sharp needle", "description": ""},
								    {"name": "Medicine chest", "description": "Presence + 4 uses (stops bleeding/infection and heals d6 HP)"},
								    {"name": "Metal file and lockpits", "description": ""},
								    {"name": "Bear trap", "description": ""},
								    {"name": "Bomb", "description": ""},
								    {"name": "Red poisson", "description": "d4 doses (Toughness DR12 or d10 damage)"},
								    {"name": "Silver crucifix", "description": ""}
								],
						"3rd":	[
									{"name": "Life elixir", "description": "d4 doses that heals d6 HP and removes infection"},
								    {"name": "Sacred scroll", "description": ""},
								    {"name": "Small but vicious dog", "description": "d6+2 HP, bite d4, only obeys you"},
								    {"name": "Monkeys", "description": "d4 Monkeys that ignore but love you (d4+2 HP, punch/bite d4)"},
								    {"name": "Exquisite perfume", "description": "Worth 25s"},
								    {"name": "Toolbox", "description": "10 nails, tongs, hammer, small saw and drill"},
								    {"name": "Heavy chain", "description": "15 feet"},
								    {"name": "Grappling hook", "description": ""},
								    {"name": "Shield", "description": "-1 HP damage or have the Shield break to ignore"},
								    {"name": "Crowbar", "description": "d4 damage"},
								    {"name": "Lard", "description": "May function as 5 meals in a pinch"},
								    {"name": "Tent", "description": ""}
								]
					}

scrolls = {
		    "Unclean Scrolls": {
		        1: {"Scroll": "Unclean Scroll: Palms Open the Southern Gate", "Description": "A ball of fire hits d2 creatures dealing d8 damage per creature."},
		        2: {"Scroll": "Unclean Scroll: Tongue of Eris", "Description": "A creature of your choice is confused for 10 minutes."},
		        3: {"Scroll": "Unclean Scroll: Te-le-kin-esis", "Description": "Move an object up 1d10×10 feet for d6 minutes."},
		        4: {"Scroll": "Unclean Scroll: Lucy-Fires Levitation", "Description": "Hover for Presence d10 rounds."},
		        5: {"Scroll": "Unclean Scroll: Daemon of Capillaries", "Description": "One creature suffocates for d6 rounds, losing d4 HP per round."},
		        6: {"Scroll": "Unclean Scroll: Nine Violet Signs Unknot the Storm", "Description": "Produce d2 lightning bolts dealing d6 damage each."},
		        7: {"Scroll": "Unclean Scroll: Metzhuotl Blind Your Eye", "Description": "A creature becomes invisible for d6 rounds or until it is damaged, attacking/defending with DR6."},
		        8: {"Scroll": "Unclean Scroll: Foul Psychopomp", "Description": "Summon (d6): 1–3 d4 skeletons, 4–6 d4 zombies."},
		        9: {"Scroll": "Unclean Scroll: Eyelid Blinds the Mind", "Description": "d4 creatures fall asleep for one hour unless they succeed a DR14 test."},
		        10: {"Scroll": "Unclean Scroll: Death", "Description": "All creatures within 30 feet lose a total of 4d10 HP."}
		    },
		    "Sacred Scroll": {
		        1: {"Scroll": "Sacred Scroll: Grace of a Dead Saint", "Description": "d2 creatures regain d10 HP each."},
		        2: {"Scroll": "Sacred Scroll: Grace for a Sinner", "Description": "A creature of your choice gets +d6 on one roll (damage, test etc.)."},
		        3: {"Scroll": "Sacred Scroll: Whispers pass the Gate", "Description": "Ask three questions to a deceased creature."},
		        4: {"Scroll": "Sacred Scroll: Aegis of Sorrow", "Description": "A creature of your choice gains 2d6 extra HP for 10 rounds."},
		        5: {"Scroll": "Sacred Scroll: Unmet Fate", "Description": "One creature, dead for no more than a week, is awakened with terrible memories."},
		        6: {"Scroll": "Sacred Scroll: Bestial Speech", "Description": "You may speak with animals for d20 minutes."},
		        7: {"Scroll": "Sacred Scroll: False Dawn / Night’s Chariot", "Description": "Light or pitch black for 3d10 minutes."},
		        8: {"Scroll": "Sacred Scroll: Hermetic Step", "Description": "You find all traps in your path for 2d10 minutes."},
		        9: {"Scroll": "Sacred Scroll: Roskoe’s Consuming Glare", "Description": "d4 creatures lose d8 HP each."},
		        10: {"Scroll": "Sacred Scroll: Enochian Syntax", "Description": "One creature blindly obeys a single command."}
		    }
		}

initial_weapons = {
				    1: {"name": "Femur", "description": "d4 damage"},
				    2: {"name": "Staff", "description": "d4 damage"},
				    3: {"name": "Shortsword", "description": "d4 damage"},
				    4: {"name": "Knife", "description": "d4 damage"},
				    5: {"name": "Warhammer", "description": "d6 damage"},
				    6: {"name": "Sword", "description": "d6 damage"},
				    7: {"name": "Bow", "description": "d6 damage with Presence + 10 arrows"},
				    8: {"name": "Flail", "description": "d8 damage"},
				    9: {"name": "Crossbow", "description": "d8 damage with Presence + 10 bolts"},
				    10: {"name": "Zweihander", "description": "d10 damage"}
}  

initial_armors = {
				    1: {"name": "No Armor", "description": "Tier 0"},
				    2: {"name": "Light armor", "description": "-d2 damage, tier 1"},
				    3: {"name": "Medium armor", "description": "-d4 damage, tier 2"},
				    4: {"name": "Heavy armor", "description": "-d6 damage, tier 3"}
				 }

names = [
		    {"d6": 1, "d8": 1, "Name": "Aerg-Tval"},
		    {"d6": 1, "d8": 2, "Name": "Agn"},
		    {"d6": 1, "d8": 3, "Name": "Arvant"},
		    {"d6": 1, "d8": 4, "Name": "Belsum"},
		    {"d6": 1, "d8": 5, "Name": "Belum"},
		    {"d6": 1, "d8": 6, "Name": "Brint"},
		    {"d6": 1, "d8": 7, "Name": "Börda"},
		    {"d6": 1, "d8": 8, "Name": "Daeru"},
		    {"d6": 2, "d8": 1, "Name": "Eldar"},
		    {"d6": 2, "d8": 2, "Name": "Felban"},
		    {"d6": 2, "d8": 3, "Name": "Gotven"},
		    {"d6": 2, "d8": 4, "Name": "Graft"},
		    {"d6": 2, "d8": 5, "Name": "Grin"},
		    {"d6": 2, "d8": 6, "Name": "Grittr"},
		    {"d6": 2, "d8": 7, "Name": "Haerü"},
		    {"d6": 2, "d8": 8, "Name": "Hargha"},
		    {"d6": 3, "d8": 1, "Name": "Harmug"},
		    {"d6": 3, "d8": 2, "Name": "Jotna"},
		    {"d6": 3, "d8": 3, "Name": "Karg"},
		    {"d6": 3, "d8": 4, "Name": "Karva"},
		    {"d6": 3, "d8": 5, "Name": "Katla"},
		    {"d6": 3, "d8": 6, "Name": "Keftar"},
		    {"d6": 3, "d8": 7, "Name": "Klort"},
		    {"d6": 3, "d8": 8, "Name": "Kratar"},
		    {"d6": 4, "d8": 1, "Name": "Kutz"},
		    {"d6": 4, "d8": 2, "Name": "Kvetin"},
		    {"d6": 4, "d8": 3, "Name": "Lygan"},
		    {"d6": 4, "d8": 4, "Name": "Margar"},
		    {"d6": 4, "d8": 5, "Name": "Merkari"},
		    {"d6": 4, "d8": 6, "Name": "Nagl"},
		    {"d6": 4, "d8": 7, "Name": "Niduk"},
		    {"d6": 4, "d8": 8, "Name": "Nifehl"},
		    {"d6": 5, "d8": 1, "Name": "Prügl"},
		    {"d6": 5, "d8": 2, "Name": "Qillnach"},
		    {"d6": 5, "d8": 3, "Name": "Risten"},
		    {"d6": 5, "d8": 4, "Name": "Svind"},
		    {"d6": 5, "d8": 5, "Name": "Theras"},
		    {"d6": 5, "d8": 6, "Name": "Therg"},
		    {"d6": 5, "d8": 7, "Name": "Torvul"},
		    {"d6": 5, "d8": 8, "Name": "Törn"},
		    {"d6": 6, "d8": 1, "Name": "Urm"},
		    {"d6": 6, "d8": 2, "Name": "Urvarg"},
		    {"d6": 6, "d8": 3, "Name": "Vagal"},
		    {"d6": 6, "d8": 4, "Name": "Vatan"},
		    {"d6": 6, "d8": 5, "Name": "Von"},
		    {"d6": 6, "d8": 6, "Name": "Vrakh"},
		    {"d6": 6, "d8": 7, "Name": "Vresi"},
		    {"d6": 6, "d8": 8, "Name": "Wemut"},
		]

print(type(names))