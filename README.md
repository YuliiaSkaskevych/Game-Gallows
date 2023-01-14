Implement a word guessing game according to the developed project.



Terms:
1. There are topics in each list of words for guessing.
    At the start, the user receives a list of topics, enters the name of the desired one;
2. The program randomly selects a word from those available in the subject, announces its length and number of attempts (number of letters + 5);
3. The program prompts the user to enter a letter;
4. It is necessary to check the input for "adequacy". We exclude numbers, symbols, an empty line and a space.
    In case of incorrect input, the number of attempts is not reduced;
5. Letters cannot be re-entered. When re-entering, the number of attempts is not reduced;
6. If the letter is not in the word, reduce the number of attempts by one;
7. If the letter is in the word, we print the word, replacing the unguessed letters with an underscore;
8. If a letter occurs in a word 2 or more times, it is enough to guess it 1 time;
9. The game stops in 2 cases: the attempts are over or the word is guessed.
