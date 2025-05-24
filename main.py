questions =[
  ["Who is the current Prime Minister of India (as of 2024)?", "Narendra Modi", "Rahul Gandhi", "Amit Shah", "Manmohan Singh", 1],
  ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
  ["Which festival is known as the Festival of Lights?", "Holi", "Raksha Bandhan", "Diwali", "Eid", 3],
  ["What is the capital of Maharashtra?", "Delhi", "Nagpur", "Mumbai", "Pune", 3],
  ["Which animal is known as the 'Ship of the Desert'?", "Elephant", "Camel", "Horse", "Donkey", 2],
  ["What is the currency of Japan?", "Yuan", "Won", "Dollar", "Yen", 4],
  ["Who wrote the Indian National Anthem?", "Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarojini Naidu", "Jawaharlal Nehru", 2],
  ["Which of these is a programming language?", "Python", "Anaconda", "Cobra", "Viper", 1],
  ["Where is the Taj Mahal located?", "Delhi", "Agra", "Jaipur", "Lucknow", 2],
  ["Which sport is associated with Wimbledon?", "Cricket", "Football", "Tennis", "Hockey", 3]
]

print("Welcome To Kaun Banega Crorepati.")
money = 0

for question in questions:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"5. {question[1]}")
    print(f"Current Money : Rs.{money}")

    #check whether the answer is corrent or not

    a = int(input("Enter the Answer (1/2/3/4) : "))
    if(question[5] == a):
        print("Correct Answer")
        money =money + 100
        print(f"Your Current Money  : Rs.{money}")
    else:
        print(f"Incorrect Answer. The correct answer is option : {question[5]}")
        print(f"You are taking Home Rs.{money}")
        break