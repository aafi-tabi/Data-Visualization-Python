import matplotlib.pyplot as plt

# 💼 LEVEL 1 — Daily Life Data Drill
# data = [6.5, 7, 6, 5.5, 8, 9, 7.5]
# plt.hist(data, bins=3, color="plum", edgecolor="black")
# plt.grid(True)
# plt.title("Daily Life Data Drill")
# plt.xlabel("value range")
# plt.ylabel("frequency")
# plt.show()

# 📊 LEVEL 2 — Mood Tracker Bar Chart

# days = ["mon","tue","wed","thu","fri","sat","sun"]
# mood = [2, 3, 4, 3, 5, 4, 2]
# plt.bar(days, mood)
# plt.show()

# 📈 LEVEL 3 — Caffeine vs Study Hours Plot

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# study_hours = [2, 4, 3, 5, 6]
# # snack_level = [1, 2, 2, 3, 4]

# plt.plot(days, study_hours, marker="o", color="pink", linestyle="--")
# plt.grid(True)
# plt.xlabel("days")
# plt.ylabel("study_hours")
# plt.title("Caffeine vs Study Hours Plot")
# plt.show()

# sleep = [5, 6, 7, 8, 6.5, 7.5, 9]
# energy = [3, 4, 6, 9, 5, 7, 10]

# plt.boxplot(sleep)
# plt.xlabel("hours slept")
# plt.ylabel("how energetic you felt (1–10)")
# plt.title("sleep vs energy levels")
# plt.grid()
# plt.show()

# import matplotlib.pyplot as plt

# Create a 2x2 grid
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])  # Top-left

plt.subplot(2, 2, 2)
plt.plot([1, 2, 3], [1, 2, 3])  # Top-right

plt.subplot(2, 2, 3)
plt.plot([1, 2, 3], [9, 4, 1])  # Bottom-left

plt.subplot(2, 2, 4)
plt.plot([1, 2, 3], [3, 2, 1])  # Bottom-right

plt.tight_layout()  # so they don't overlap
plt.show()
