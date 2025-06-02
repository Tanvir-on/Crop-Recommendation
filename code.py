# Crop data with soil suitability
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
    {"name": "কাউন", "pH_min": 5.5, "pH_max": 7.0, "N_min": 60, "N_max": 80, "P_min": 20, "P_max": 30, "K_min": 30, "K_max": 50},
    {"name": "চীনা", "pH_min": 5.5, "pH_max": 6.5, "N_min": 60, "N_max": 80, "P_min": 15, "P_max": 25, "K_min": 30, "K_max": 50},
    {"name": "ব্রোকলি", "pH_min": 6.0, "pH_max": 7.0, "N_min": 100, "N_max": 140, "P_min": 25, "P_max": 35, "K_min": 60, "K_max": 80},
    {"name": "চাইনিজ বাঁধাকপি", "pH_min": 6.0, "pH_max": 7.0, "N_min": 160, "N_max": 210, "P_min": 35, "P_max": 50, "K_min": 100, "K_max": 150}
]

# Suggest crops based on soil
def suggestion(pH, N, P, K):
    suitable_crop = []
    for x in crop_data:
        if (x["pH_min"] <= pH <= x["pH_max"] and
            x["N_min"] <= N <= x["N_max"] and
            x["P_min"] <= P <= x["P_max"] and
            x["K_min"] <= K <= x["K_max"]):
            suitable_crop.append(x["name"])

    if suitable_crop:
        print("\n✅ Suitable crops based on soil parameters:")
        print(", ".join(suitable_crop))
    else:
        print("\n❌ No suitable crops found based on soil parameters.")

# Map month to season
def month_suggest(month1):
    season_list = {}
    with open("seasons_by_month.txt", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            key1 = line.split(",")[0]
            list1 = line.split(",")[1:]
            season_list[key1] = list1

    for key, month2 in season_list.items():
        if month1 in month2:
            return key
    return None

# Get crop list for a season
def season_suggest(season_key):
    season_list2 = {}
    current_season = None
    with open("", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) == 1:
                current_season = parts[0].strip()
                season_list2[current_season] = {}
            else:
                category = parts[0]
                crops = parts[1:]
                if current_season:
                    season_list2[current_season][category] = crops

    return season_list2.get(season_key)

# Optional: Filter crops based on both season and soil
def filtered_crop_suggestions(pH, N, P, K, seasonal_crops):
    suitable_crop = []
    for crop in crop_data:
        if crop["name"] in seasonal_crops:
            if (crop["pH_min"] <= pH <= crop["pH_max"] and
                crop["N_min"] <= N <= crop["N_max"] and
                crop["P_min"] <= P <= crop["P_max"] and
                crop["K_min"] <= K <= crop["K_max"]):
                suitable_crop.append(crop["name"])
    return suitable_crop

# Main function
def suggestiion_crop_based_on_month():
    while True:
        print("\n=== Crop Recommendation System ===")
        try:
            a = float(input("Enter pH value: "))
            b = float(input("Enter N value: "))
            c = float(input("Enter P value: "))
            d = float(input("Enter K value: "))
        except ValueError:
            print("Please enter valid numeric values.")
            continue

        month = input("Enter month name (e.g., november): ").lower()

        season_key = month_suggest(month)
        if season_key:
            print(f"\n🌾 Season detected: {season_key.capitalize()}")
            crops_data = season_suggest(season_key)
            if crops_data:
                print("\n📋 Seasonal crop list:")
                all_crops = []
                for category, crops in crops_data.items():
                    print(f"  ▶ {category.capitalize()}: {', '.join(crops)}")
                    all_crops.extend(crops)

                # Soil + Season-based filter
                filtered = filtered_crop_suggestions(a, b, c, d, all_crops)
                if filtered:
                    print("\n✅ Crops suitable for both soil and season:")
                    print(", ".join(filtered))
                else:
                    print("\n⚠️ No crop matches both soil and seasonal conditions.")
            else:
                print("No crop data found for this season.")
        else:
            print("❌ No season found for the given month.")

        # Optionally, show all soil-suitable crops
        suggestion(a, b, c, d)

        again = input("\nDo you want to try again? (yes/no): ").lower()
        if again != "yes":
            break

# Run the program
suggestiion_crop_based_on_month()
