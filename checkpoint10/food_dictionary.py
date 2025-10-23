def main():
    word_list = [
  "banana", "milk", "soda", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "soda", "sourmilk", "sourmilk", "butter", "soda", "chocolate"
    ]
    count(word_list)
def count(word_list):
    repetitions = {}
    for word in word_list:
        if word not in repetitions:
            repetitions[word] = 0
        
        repetitions[word] += 1
    print(repetitions)

main()