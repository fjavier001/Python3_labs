


wee_names = []

wee_names = list(filter(filter_names,pets))
print(f"3.Short names = {wee_names}")

wee_names = [ pet_name.title() for pet_name in pets if len(pet_name) <= 5]
print(f"5.1 Short names = {wee_names}@)

wee_names = [ (pet_name.title(), len(pet_name)) for pet_name in pets if len(pet_name) <=5 ]
print(f"5.Short names = {wee_names}")

wee_names = { pet_name.title(): len(pet_name) for pet_name in pets if len(pet_name) <= 5 }
print(f"5.2 Short names = {wee_names}")

wee_names = { pet_name.title() for pet_name in pets if len(pet_name) <= 5 }
print(f"5.3 Short names = {wee_names}")