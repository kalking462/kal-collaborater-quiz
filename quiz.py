
TICK = "✅"
CROSS = "❌"
questions = [
    # ========== MATH (17) ==========
    # ========THIS PART IS DONE BY KAL=====
    { "question": "[Math] What is 2 + 2?",
      "choices": ["3", "4", "5", "6"],
      "correct_index": 1 },

    { "question": "[Math] The derivative of x^2 with respect to x is:",
      "choices": ["x", "2x", "x^2", "1"],
      "correct_index": 1 },

    { "question": "[Math] ∫ x dx =",
      "choices": ["x^2 + C", "x^2/2 + C", "ln(x) + C", "2x + C"],
      "correct_index": 1 },

    { "question": "[Math] Solve 3x + 5 = 20. What is x?",
      "choices": ["3", "5", "7", "15"],
      "correct_index": 1 },

    { "question": "[Math] The slope of the line y = 3x − 1 is:",
      "choices": ["3", "-1", "1/3", "0"],
      "correct_index": 0 },

    { "question": "[Math] det([[1,2],[3,4]]) equals:",
      "choices": ["-2", "2", "5", "-5"],
      "correct_index": 0 },

    { "question": "[Math] lim (n→∞) (1 + 1/n)^n =",
      "choices": ["0", "1", "e (~2.718)", "Infinity"],
      "correct_index": 2 },

    { "question": "[Math] Roots of x^2 - 5x + 6 = 0 are:",
      "choices": ["1 and 6", "2 and 3", "-2 and -3", "3 and 4"],
      "correct_index": 1 },

    { "question": "[Math] The derivative of sin(x) is:",
      "choices": ["cos(x)", "-cos(x)", "sin(x)", "-sin(x)"],
      "correct_index": 0 },

    { "question": "[Math] Area of a circle of radius r is:",
      "choices": ["2πr", "πr^2", "πr^3", "4πr^2"],
      "correct_index": 1 },

    { "question": "[Math] log10(1000) equals:",
      "choices": ["2", "3", "4", "0.3"],
      "correct_index": 1 },

    { "question": "[Math] The arithmetic mean of 4 and 10 is:",
      "choices": ["6", "7", "8", "9"],
      "correct_index": 1 },

    { "question": "[Math] A right triangle with legs 6 and 8 has hypotenuse:",
      "choices": ["9", "10", "12", "14"],
      "correct_index": 1 },

    { "question": "[Math] Solve 2^x = 8. Then x =",
      "choices": ["2", "3", "4", "8"],
      "correct_index": 1 },

    { "question": "[Math] The median of [3, 7, 9, 11, 15] is:",

      "correct_index": 1 },

    { "question": "[Math] 5 choose 2 equals:",
      "choices": ["5", "10", "15", "20"],
      "correct_index": 1 },

    { "question": "[Math] The derivative of e^(2x) is:",
      "choices": ["e^(2x)", "2e^(2x)", "e^(x)", "2e^(x)"],
      "correct_index": 1 },
OBOBOB
    # ========== PHYSICS (17) ==========
    { "question": "[Physics] SI unit of force is:",
OBOBOB      "choices": ["Joule", "Pascal", "Newton", "Watt"],
      "correct_index": 2 },
OBOBOB
    { "question": "[Physics] Speed of light in vacuum is approximately:",
      "choices": ["3×10^6 m/s", "3×10^8 m/s", "3×10^10 m/s", "3×10^12 m/s"],
OBOBOB      "correct_index": 1 },
OBOBOB
    { "question": "[Physics] F = ma is:",
      "choices": ["Newton's First Law", "Newton's Second Law", "Newton's Third Law", "Hooke's Law"],
      "correct_index": 1 },
]

x = ["A", "B", "C", "D"]

score = 0
h = input("Enter your name: ")
OBOBOB
OBOBOBprint("\nHello", h, "WELCOME TO MULTIPLE CHOICE QUIZ - ENGLISH, MATH, CHEMISTRY, PHYSICS, BIOLOGY AND APTITUDE")
OBOBOBprint("============================================================\n")

for i, q in enumerate(questions, 1):
OBOBOB    print(f"Q{i}: {q['question']}")
    for idx, choice in enumerate(q["choices"]):
        print(f"   {x[idx]}. {choice}")

    z = input("Your answer (A, B, C, D): ").strip().upper()
    if z in x:
        user_index = x.index(z)
        if user_index == q["correct_index"]:
            print(f"{TICK} Correct!\n")
            score += 1
        else:
            g = x[q["correct_index"]]
            y = q["choices"][q["correct_index"]]
            print(f"{CROSS} Wrong! Correct answer is: {g}. {y}\n")
    else:
        print(f"{CROSS} Invalid choice. Skipped.\n")

print("======================")
OBOBOBprint(h, f"your score is: {score}", "out of", len(questions))
OBOBOBOBOBOBpercent = (score / len(questions)) * 100
print(f"Percentage: {percent:.1f}%")
OBOBOBprint("======================")

if score == len(questions):
    print(h, " Perfect! Excellent job!!! 🎉")
elif score >= len(questions) * 0.9:
    print(h, "🌟 Outstanding performance!")
elif score >= len(questions) * 0.75:
    print(h, "👏 Great job! Keep it up.")
elif score >= len(questions) / 2:
    print(h, "👍 Good job! Keep practicing.")
else:
    print(h, "Keep trying — you’ll get better!")

