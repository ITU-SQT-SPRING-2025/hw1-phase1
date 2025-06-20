# BLG 475E Software Quality and Testing 2024-2025 Spring Term Project

The aim of the project is to use publicly available LLMs to generate codes, unit tests, and integration tests and compare the results using the [HumanEval](https://github.com/openai/human-eval) dataset.

The LLM selection was based on the availability of the LLMs on web. Moreover, the selected LLMs are the models that are free and considered state-of-the-art currently.

## The LLMs used in the project:

- GPT-4o (ChatGPT's free tier)
- DeepSeek-V3 (DeepSeek's free tier)

### Group members are:

| Student ID |   Student Name   |
| ---------- | ---------------- |
| 150220760  | Onur Yavri       |
| 150210710  | Fatih Baskın     |
| 150200917  | Erblina Nivokazi |


## Chosen test set from the HumanEval dataset.

| Order | Prompt ID | Reason for being chosen | Difficulty |
| ----: | --------- | ----------------------- | :--------: |
| 1| HumanEval/21  | The implementation requires arithmetic knowledge. | Easy |
| 2| HumanEval/26  | To see the behavior of the LLM, whether it uses a data structure or solves procedurally. | Easy |
| 3| HumanEval/57  | The implementation requires what monotonocally increasing/decreasing means. | Easy |
| 4| HumanEval/72  | The implementation requires a popular problem, which is deciding whether a sequence is palindrom or not. | Easy |
| 5| HumanEval/79  | A common introductory problem to programming. | Easy |
| 6| HumanEval/89  | Encryption algorithms can be hard to grasp fully for LLMs (or for non-experts). | Hard |
| 7| HumanEval/93  | Encoding is one of the core of communication | Hard |
| 8| HumanEval/94  | The function name is not self-describing, might mislead the LLMs' results. | Moderate |
| 9| HumanEval/116 | The requested implementation has an example that contradicts with the problem specification. Because of that, LLMs might struggle which requirement to satisfy. | Hard |
|10| HumanEval/126 | Checking if a list is sorted can be done in multiple ways, the choice of LLMs might differ. Thus, it is included in the test set. | Moderate |
|11| HumanEval/163 | Tests understanding of integer generation and sequence control, fundamental to program flow. | Easy |
|12| HumanEval/27 | Involves working with pairs and sorting, a basic but important data structure operation. | Moderate |
|13| HumanEval/6 | Requires parsing and nested list manipulation, assessing LLMs' capacity for handling recursive data. | Moderate |
|14| HumanEval/22 | Focuses on filtering and boolean operations over arrays, important for array-processing skills. | Easy |
|15| HumanEval/108 | Challenges involve mapping multiple rules to elements, good for testing conditional structures. | Moderate |
|16| HumanEval/129 | Requires constructing palindromic sequences, which is slightly tricky and tests string manipulation. | Moderate |
|17| HumanEval/143 | Involves mathematical operations and prime number logic, known to be difficult for language models. | Hard |
|18| HumanEval/50 | Involves basic string operations and pattern matching, fundamental for LLMs. | Easy |
|19| HumanEval/155 | Requires precise handling of list operations and slicing, prone to boundary errors. | Easy |
|20| HumanEval/107 | Demands implementing customized arithmetic logic, harder than typical operations. | Hard |
|21| HumanEval/161  | A basic string manipulation function, however the function name is not self-describing, might mislead the LLMs' results. | Moderate |
|22| HumanEval/160  | Requires knowledge of operator precedence and data structures (such as trees) to evaluate algebraic expressions. | Hard |
|23| HumanEval/158  | Function that finds a string in a given rule from an array. Requires knowledge of sets/maps and sorting | Moderate |
|24| HumanEval/154  | This function checks cyclic patters given in two strings. A function that tests LLM's capacity to form nested loops. | Easy |
|25| HumanEval/151  | This function requires basic array handling and arithmetic knowledge. | Easy |
|26| HumanEval/150  | For this function, prime numbers should be evaluated. It could be done using Sieve of Eratosthenes. | Easy |
|27| HumanEval/110  | A basic function that requires array handling and counting | Easy | 
|28| HumanEval/109  | Some simple logic is involved to solve this function. Requires array handling | Easy |
|29| HumanEval/106  | A basic mathematical function, however the function name is not self-describing, might mislead the LLMs' results. | Moderate |
|30| HumanEval/59  | A complex mathematical problem that involves prime numbers and divisors. | Hard |

## Prompt for the integration test's implementation and the scenario for the integration

### Prompt: 
```You will implement a Python class named Secret that has methods of encoding a given string by shifting forward 5, wrapping around z to a in the alphabet, and decoding in the reverse manner. The class will also have a method that takes a string representing a sentence. The sentence contains some words separated by a space, and it will find a new string that contains the words from the original sentence whose lengths are prime numbers. The order of words in the original sentence will be preserved in the new sentence. Another method for this class is going to find if length of words of a sentence is monotonically increasing, or monotonically decreasing or neither of them. \nExamples: \nSecret.encode("fun code") => "kzs htij" \nSecret.encode("quick fox") => "vznhp ktc" \nSecret.decode("vznhp ktc") => "quick fox" \nSecret.isMonotonic("fun code") => True \nSecret.isMonotonic("coding is fun") => False \nSecret.processSentence("fun code") => "fun code" \nSecret.processSentence("this is a test") => "is"```

### Follow-up prompt for test scenario: 
```Using PyUnit, implement an integration test that does the process over given string sentence and encode if the processed string is monotonic, else decode the processed string.```
