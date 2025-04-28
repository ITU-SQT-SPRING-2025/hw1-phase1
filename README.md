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
| 1502XXXXX  | Fatih Baskın     |
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
|21| HumanEval/XX  |                         |                       |
|22| HumanEval/XX  |                         |                       |
|23| HumanEval/XX  |                         |                       |
|24| HumanEval/XX  |                         |                       |
|25| HumanEval/XX  |                         |                       |
|26| HumanEval/XX  |                         |                       |
|27| HumanEval/XX  |                         |                       |
|28| HumanEval/XX  |                         |                       |
|29| HumanEval/XX  |                         |                       |
|30| HumanEval/XX  |                         |                       |

