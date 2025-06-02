# ফসলের ডেটা (BARI-ভিত্তিক soil range সহ)
crop_data = [
    {"name": "ধান", "pH_min": 5.5, "pH_max": 7.0, "N_min": 80, "N_max": 100, "P_min": 30, "P_max": 50, "K_min": 50, "K_max": 70},
    {"name": "আলু", "pH_min": 5.0, "pH_max": 6.5, "N_min": 60, "N_max": 90, "P_min": 25, "P_max": 40, "K_min": 45, "K_max": 65},
    {"name": "গম", "pH_min": 6.0, "pH_max": 7.5, "N_min": 85, "N_max": 100, "P_min": 35, "P_max": 60, "K_min": 55, "K_max": 75},
    {"name": "ভুট্টা", "pH_min": 5.8, "pH_max": 7.2, "N_min": 80, "N_max": 110, "P_min": 40, "P_max": 60, "K_min": 50, "K_max": 70},
    {"name": "সরিষা", "pH_min": 6.0, "pH_max": 7.5, "N_min": 60, "N_max": 85, "P_min": 25, "P_max": 45, "K_min": 45, "K_max": 65},
    {"name": "পাট", "pH_min": 5.5, "pH_max": 7.5, "N_min": 70, "N_max": 90, "P_min": 30, "P_max": 50, "K_min": 50, "K_max": 70},
    {"name": "আখ", "pH_min": 6.0, "pH_max": 7.0, "N_min": 100, "N_max": 140, "P_min": 45, "P_max": 60, "K_min": 60, "K_max": 80},
    {"name": "শাক", "pH_min": 6.2, "pH_max": 7.5, "N_min": 60, "N_max": 85, "P_min": 30, "P_max": 50, "K_min": 50, "K_max": 65},
    {"name": "লালশাক", "pH_min": 5.5, "pH_max": 6.8, "N_min": 50, "N_max": 75, "P_min": 20, "P_max": 40, "K_min": 40, "K_max": 60},
    {"name": "টমেটো", "pH_min": 5.5, "pH_max": 6.8, "N_min": 70, "N_max": 95, "P_min": 30, "P_max": 50, "K_min": 50, "K_max": 70},
    {"name": "বার্লি", "pH_min": 6.0, "pH_max": 7.5, "N_min": 60, "N_max": 80, "P_min": 15, "P_max": 25, "K_min": 30, "K_max": 50},
    {"name": "কাউন", "pH_min": 5.5, "pH_max": 7.0, "N_min": 60, "N_max": 80, "P_min": 20, "P_max": 30, "K_min": 30, "K_max": 50},
    {"name": "চীনা", "pH_min": 5.5, "pH_max": 6.5, "N_min": 60, "N_max": 80, "P_min": 15, "P_max": 25, "K_min": 30, "K_max": 50},
    {"name": "ব্রোকলি", "pH_min": 6.0, "pH_max": 7.0, "N_min": 100, "N_max": 140, "P_min": 25, "P_max": 35, "K_min": 60, "K_max": 80},
    {"name": "চাইনিজ বাঁধাকপি", "pH_min": 6.0, "pH_max": 7.0, "N_min": 160, "N_max": 210, "P_min": 35, "P_max": 50, "K_min": 100, "K_max": 150}
]

def suggestion(pH, N, P, K):
    suitable_crop = []
    for x in crop_data:
        if (x["pH_min"] <= pH <= x["pH_max"] and
            x["N_min"] <= N <= x["N_max"] and
            x["P_min"] <= P <= x["P_max"] and
            x["K_min"] <= K <= x["K_max"]):
            suitable_crop.append(x["name"])
    if suitable_crop:
        print("\n✅ Soil-based Suitable Crops:")
        print(", ".join(suitable_crop))
    else:
        print("\n❌ No suitable crops found based on soil parameters.")

def month_suggest(month1):
    season_list = {}
    try:
        with open("E:\\month.txt") as file:
            for line in file:
                line = line.strip()
                key1 = line.split(",")[0]
                list1 = line.split(",")[1:]
                season_list[key1] = list1
    except FileNotFoundError:
        print("❌ E:\\month.txt not found.")
        return None
    for key, month2 in season_list.items():
        if month1 in [m for m in month2]:
            return key
    return None

def season(x):
    file_path = "E:\\Season_text.txt"  # ✅ Your exact file path

    season_list2 = {}
    current_season = None

    # Read and parse the file
    try:
        with open(file_path, encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                # Skip blank lines
                if not line:
                    continue

                parts = [p.strip() for p in line.split(",")]

                if len(parts) == 1:
                    # It's a season name
                    current_season = parts[0]
                    season_list2[current_season] = {}
                elif current_season:
                    # It's a category and crops
                    category = parts[0]
                    crops = parts[1:]
                    season_list2[current_season][category] = crops

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return

    # Show data if season is found
    if x in season_list2:
        print(f"\n📅 Season: {x}")
        for category, crops in season_list2[x].items():
            print(f"📂 Category: {category}")
            print(f"🌱 Crops: {', '.join(crops)}")
    else:
        print(f"\n⚠️ Season not found: {x}")
def suggestion_crop_based_on_month():
    while True:
        print("\n🔄 New Crop Suggestion")
        try:
            a = float(input("Enter soil pH: "))
            b = float(input("Enter Nitrogen (N): "))
            c = float(input("Enter Phosphorus (P): "))
            d = float(input("Enter Potassium (K): "))
            month = input("Enter month name (e.g., january): ").strip().capitalize()
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
            continue


        season_suggest= month_suggest(month)
        season(season_suggest)

        suggestion(a, b, c, d)

# 🔰 Start the program
suggestion_crop_based_on_month()
