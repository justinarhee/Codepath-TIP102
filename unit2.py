from collections import Counter
import math

# session 1 standard problem set ver 1

# problem 1
def lineup(artists, set_times):
    dict = {}
    for i in range(len(artists)):
        dict[artists[i]] = set_times[i]
    return dict

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]
# artists2 = []
# set_times2 = []
# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# problem 2
def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return {'message': 'Artist not found'}
    
# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }
# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  

# problem 3
def total_sales(ticket_sales):
    return sum(ticket_sales.values())

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
# print(total_sales(ticket_sales))

# problem 4
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}
    for artist in venue1_schedule:
        if artist in venue2_schedule:
            if venue1_schedule[artist] == venue2_schedule[artist]:
                conflicts[artist] = venue1_schedule[artist]
    return conflicts

# venue1_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "8:00 PM",
#     "HARDY": "7:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }
# venue2_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "10:30 PM",
#     "HARDY": "7:00 PM",
#     "Wizkid": "6:00 PM"
# }
# print(identify_conflicts(venue1_schedule, venue2_schedule))

# problem 5
def best_set(votes):
    freq = Counter(votes.values())
    print(freq)
    maxVote = max(freq.values())
    for artist, count in freq.items():
        if count == maxVote:
            return artist

# votes1 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA",
#     1239: "SZA"
# }
# votes2 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA"
# }
# print(best_set(votes1))
# print(best_set(votes2))

# problem 6
def max_audience_performances(audiences):
    max_val = max(audiences)
    return sum(a for a in audiences if a == max_val)

# problem 8
def num_popular_pairs(popularity_scores):
    sum = 0
    freq = Counter(popularity_scores)
    for score, count in freq.items():
        if count > 1:
            sum += math.comb(count, 2)
    return sum

# popularity_scores1 = [1, 2, 3, 1, 1, 3]
# popularity_scores2 = [1, 1, 1, 1]
# popularity_scores3 = [1, 2, 3]
# print(num_popular_pairs(popularity_scores1))
# print(num_popular_pairs(popularity_scores2))
# print(num_popular_pairs(popularity_scores3))

# problem 9
def find_stage_arrangement_difference(s,t):
    sum = 0
    for i in range(len(s)):
        sum += abs(i - t.index(s[i]))
    return sum

# s1 = ["Alice", "Bob", "Charlie"]
# t1 = ["Bob", "Alice", "Charlie"]
# s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
# t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]
# print(find_stage_arrangement_difference(s1, t1))
# print(find_stage_arrangement_difference(s2, t2))

# problem 10
def num_VIP_guests(vip_passes, guests):
    vip_set = set()
    for c in vip_passes:
        vip_set.add(c)
    count = 0
    for g in guests:
        if g in vip_set:
            count += 1
    return count

# vip_passes1 = "aA"
# guests1 = "aAAbbbb"
# vip_passes2 = "z"
# guests2 = "ZZ"
# print(num_VIP_guests(vip_passes1, guests1))
# print(num_VIP_guests(vip_passes2, guests2))

# problem 11
def schedule_pattern(pattern, schedule):
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

    return True

# pattern1 = "abba"
# schedule1 = "rock jazz jazz rock"
# pattern2 = "abba"
# schedule2 = "rock jazz jazz blues"
# pattern3 = "aaaa"
# schedule3 = "rock jazz jazz rock"
# print(schedule_pattern(pattern1, schedule1))
# print(schedule_pattern(pattern2, schedule2))
# print(schedule_pattern(pattern3, schedule3))

# session 1 advanced problem set ver 1
# problem 1
def total_treasures(treasure_map):
    return sum(treasure_map.values())

# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }
# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }
# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2))

# problem 2
def can_trust_message(message):
    message = "".join(message.split())
    mes = set(message)
    if (len(mes) == 26):
        return True
    return False

# message1 = "sphinx of black quartz judge my vow"
# message2 = "trust me"
# print(can_trust_message(message1))
# print(can_trust_message(message2))

# problem 3
def find_duplicate_chests(chests):
    freq = Counter(chests)
    duplicates = []
    for chest in freq:
        if freq[chest] > 1:
            duplicates.append(chest)
    return duplicates

# chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# chests2 = [1, 1, 2]
# chests3 = [1]
# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))

# problem 4
def is_balanced(code):
    freq = Counter(code)
    freqFreq = Counter(freq.values())

    if len(freqFreq) != 2:
        return False
    check = list(freqFreq)
    if abs(check[0] - check[1]) != 1:
        return False
    return True

# code1 = "arghh"
# code2 = "haha"
# print(is_balanced(code1)) 
# print(is_balanced(code2)) 

# problem 5
def find_treasure_indices(gold_amounts, target):
    