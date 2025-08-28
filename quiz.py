
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
    #========THIS PART IS DONE BY SELAM========

    { "question": "[English] 'Once in a blue moon' means:",
      "choices": ["very often", "very rarely", "at night", "twice monthly"],
      "correct_index": 1 },

    { "question": "[English] Comparative of 'good' is:",
      "choices": ["gooder", "best", "better", "more good"],
      "correct_index": 2 },

    { "question": "[English] Author of 'Romeo and Juliet':",
      "choices": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
      "correct_index": 1 },

    { "question": "[English] Antonym of 'expand' is:",
      "choices": ["extend", "enlarge", "contract", "inflate"],
      "correct_index": 2 },

    # ========== APTITUDE / REASONING (16) ==========
    { "question": "[Aptitude] Next number in the series 2, 4, 8, 16, ?",
      "choices": ["18", "24", "32", "64"],
      "correct_index": 2 },

    { "question": "[Aptitude] Odd one out: Square, Triangle, Circle, Rectangle",
      "choices": ["Square", "Triangle", "Circle", "Rectangle"],
      "correct_index": 2 },

    { "question": "[Aptitude] Simple interest on $1000 at 5% p.a. for 2 years:",
      "choices": ["$50", "$100", "$150", "$200"],
      "correct_index": 1 },

    { "question": "[Aptitude] Simplify the ratio 15:45",
      "choices": ["1:2", "1:3", "3:1", "2:3"],
      "correct_index": 1 },

    { "question": "[Aptitude] Probability of heads on a fair coin toss:",
      "choices": ["0", "1/2", "1/3", "1"],
      "correct_index": 1 },

    { "question": "[Aptitude] Average of 5, 7, 9 is:",
      "choices": ["6", "7", "8", "9"],
      "correct_index": 1 },

    { "question": "[Aptitude] A does a job in 10 days, B in 20 days. Together, time needed:",
      "choices": ["5 days", "6 days", "6.67 days", "7.5 days"],
      "correct_index": 2 },

    { "question": "[Aptitude] Distance at 60 km/h for 2 hours is:",
      "choices": ["60 km", "90 km", "100 km", "120 km"],
      "correct_index": 3 },

    { "question": "[Aptitude] Angle between clock hands at 3:00:",

      "correct_index": 2 },

    { "question": "[Aptitude] Distinct permutations of 'LEVEL':",
      "choices": ["12", "24", "30", "60"],
      "correct_index": 2 },

    { "question": "[Aptitude] All mammals are animals; all dogs are mammals. Therefore, dogs are animals.",
      "choices": ["Valid", "Invalid", "Unsure", "Paradox"],
      "correct_index": 0 },

    { "question": "[Aptitude] 20% of 250 equals:",
      "choices": ["25", "40", "50", "60"],
      "correct_index": 2 },

    { "question": "[Aptitude] Bought for $200, sold for $240. Profit percentage:",
      "choices": ["10%", "15%", "20%", "25%"],
      "correct_index": 2 },

    { "question": "[Aptitude] If x:y = 2:3 and y:z = 4:5, then x:z =",
      "choices": ["6:5", "8:15", "3:5", "2:5"],
      "correct_index": 1 },

    { "question": "[Aptitude] LCM of 12 and 18 is:",
      "choices": ["24", "30", "36", "48"],
      "correct_index": 2 },

    { "question": "[Aptitude] John is 5 years older than Mary. Their ages sum to 45. John's age is:",
      "choices": ["20", "22", "23", "25"],
      "correct_index": 3 },

      #========THIS PART IS DONE BY KALID $=====

    { "question": "[Physics] SI unit of energy is:",
      "choices": ["Watt", "Joule", "Newton", "Volt"],
      "correct_index": 1 },

    { "question": "[Physics] Work done by a 10 N force over 2 m (parallel) is:",
      "choices": ["5 J", "10 J", "20 J", "40 J"],
      "correct_index": 2 },

    { "question": "[Physics] Approximate acceleration due to gravity on Earth:",
      "choices": ["8.9 m/s^2", "9.8 m/s^2", "10.8 m/s^2", "1 g/s^2"],
      "correct_index": 1 },

    { "question": "[Physics] If V=12 V and R=4 Ω, current I is:",
      "choices": ["1 A", "2 A", "3 A", "4 A"],
      "correct_index": 2 },

    { "question": "[Physics] Momentum (p) is defined as:",
      "choices": ["m/a", "mv", "ma", "m/v"],
      "correct_index": 1 },

    { "question": "[Physics] Which is a scalar quantity?",
      "choices": ["Velocity", "Displacement", "Temperature", "Force"],
      "correct_index": 2 },

    { "question": "[Physics] Which particle has no electric charge?",
      "choices": ["Proton", "Electron", "Neutron", "Alpha particle"],
      "correct_index": 2 },
    { "question": "[Physics] A lens that converges light is:",
      "choices": ["Concave", "Convex", "Cylindrical", "Planar"],
      "correct_index": 1 },


      "choices": ["Circular", "Elliptical", "Parabolic", "Hyperbolic"],
      "correct_index": 1 },

    { "question": "[Physics] Unit of frequency is:",
      "choices": ["Newton", "Hertz", "Joule", "Tesla"],
      "correct_index": 1 },

    { "question": "[Physics] Pressure is defined as:",
      "choices": ["Force × area", "Force / area", "Area / force", "Work / time"],
      "correct_index": 1 },

    { "question": "[Physics] The First Law of Thermodynamics is about:",
      "choices": ["Entropy decrease", "Energy conservation", "Action-reaction", "Inertia"],
      "correct_index": 1 },

    { "question": "[Physics] Amplitude of a wave is:",
      "choices": ["Time period", "Number of cycles", "Max displacement", "Wavelength"],
      "correct_index": 2 },

    { "question": "[Physics] Highest energy EM radiation:",
      "choices": ["Radio waves", "Infrared", "X-rays", "Gamma rays"],
      "correct_index": 3 },

    # ========== CHEMISTRY (17) ==========
    { "question": "[Chemistry] Avogadro’s number is:",
      "choices": ["6.022×10^22", "6.022×10^23", "6.022×10^24", "6.022×10^25"],
      "correct_index": 1 },

    { "question": "[Chemistry] pH of a neutral solution at 25°C is:",
      "choices": ["0", "7", "14", "1"],
      "correct_index": 1 },

    { "question": "[Chemistry] Oxidation number of oxygen in H2O is:",
      "choices": ["-2", "-1", "0", "+2"],
      "correct_index": 0 },

    { "question": "[Chemistry] Bond type in NaCl is primarily:",
      "choices": ["Covalent", "Ionic", "Metallic", "Hydrogen"],
      "correct_index": 1 },

    { "question": "[Chemistry] PV = nRT is the:",
      "choices": ["Boyle’s Law", "Charles’s Law", "Ideal Gas Law", "Dalton’s Law"],
      "correct_index": 2 },

    { "question": "[Chemistry] Electron geometry of CH4 (carbon):",
      "choices": ["Linear", "Trigonal planar", "Tetrahedral", "Octahedral"],
      "correct_index": 2 },
]
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

