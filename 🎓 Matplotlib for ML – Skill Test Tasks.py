import matplotlib.pyplot as plt

data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "study_hours": [2, 3, 4, 1, 5],
    "sleep_hours": [7, 6, 5, 8, 6],
    "test_score": [70, 75, 80, 65, 90],
    "mood": ["Happy", "Tired", "Focused", "Sleepy", "Happy"]
}

days = data["day"]
study_hours = data["study_hours"]
sleep_hours = data["sleep_hours"]
test_score = data["test_score"]
mood = data["mood"]

plt.figure()
plt.plot(days,study_hours, linestyle="--", marker="o", color="pink")
plt.figure()
plt.scatter(days, study_hours, marker="o", color="plum")
plt.figure()
plt.bar(days,study_hours)
plt.figure()
plt.hist(study_hours, bins=3, color="skyblue", edgecolor="black")
plt.figure()
plt.subplot(2,2,1)
plt.plot(days,sleep_hours, label="sleep_hours")
plt.subplot(2,2,2)
plt.plot(days,study_hours, label="study_hours")
plt.subplot(2,2,3)
plt.plot(days,mood, label="mood")
plt.subplot(2,2,4)
plt.plot(days,test_score, label="test_scores")
plt.xlabel("days")
plt.ylabel("study_hours")
plt.title("study hours on diffenent days")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
