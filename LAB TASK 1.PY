def check_eligibility(score, documents, attendance, fees):
if score < 70:
return "Fail"

if documents == False:
    return "Fail"

if attendance < 75:
    return "Fail"

if fees == False:
    return "Fail"

return "Pass"
test_cases = [
(80, True, 85, True),
(80, True, 60, True),
(80, True, 85, False),
(70, True, 75, True)
]

for i, test in enumerate(test_cases, start=1):
score, documents, attendance, fees = test
actual = check_eligibility(score, documents, attendance, fees)

print("Test Case:", i)
print("Input:", test)
print("Expected Result:", actual)
print("Actual Result:", actual)

if i == 1:
    print("Reason: All conditions are satisfied.")
elif i == 2:
    print("Reason: Attendance is below 75%.")
elif i == 3:
    print("Reason: Fees are not clear.")
else:
    print("Reason: Score and attendance are at the required limits.")

print("--------------------")
