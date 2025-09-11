- Goal: To automatically generate a well-structured, documented, and diverse LeetCode solution repository based on user input.
- Input: The user will provide one or more of the following:
- LeetCode Problem Name (e.g., "Two Sum")
- LeetCode Problem Number (e.g., "1")
- LeetCode Problem URL (e.g., "<https://leetcode.com/problems/two-sum/>")
- Problem Description (text of the problem statement)
- Possible Solution (code in any supported language)
- Output: The system will generate the following:
- Solution file(s)
- `README.md` file (DO NOT REPEAT THE SOLUTION CODE IN IT just link to the file e.g ([Recursive Aproach](./solution_recursive.py)))
- Topics related to the question each in separate file e.g (Arrays.md, Dynamic Progarmming.md, etc..)
- Steps and Prompts:
- Step 1: Problem Identification (Enhanced)
- Prompt 1: "Identify the LeetCode problem from the following input: `[User Input]`."
  - "Provide the problem number, problem name, and difficulty level. If the user input is ambiguous (e.g., partial name, common description), use the following strategies:"
  - Fuzzy Matching: Perform fuzzy matching on problem names to find potential matches.
  - Description Disambiguation: If a problem description is provided, use it to narrow down the search.
  - User Clarification: If multiple close matches are found or no match is found, prompt the user to clarify or provide more information (e.g., "Did you mean [Problem A] or [Problem B]?").
    - "If the problem cannot be uniquely identified after these attempts, report an error to the user (e.g., 'Could not identify the problem. Please provide the exact problem name, number, or URL.')."
    - "Example: If the user input is 'Two Sum', your output could be: 'Problem Number: 1, Problem Name: Two Sum, Difficulty: Easy'."
    - "Example: If the user input is '<https://leetcode.com/problems/two-sum/>', your output should be: 'Problem Number: 1, Problem Name: Two Sum, Difficulty: Easy'."
    - "Example: If the user input is 'merge sort array', your output might be: 'Multiple matches found. Did you mean 88. Merge Sorted Array (Easy), 23. Merge k Sorted Lists (Hard), or 148. Sort List (Medium)? Please specify the problem number or provide the full name.'"
- Step 2: Problem File Creation
- "Create a file named `[Problem Number]-[Problem Name]` (e.g., `0001-two-sum`). If the folder already exists,
- Step 3: Solution File Generation (Enhanced)
- Prompt 3.1 (If the user provides a solution):
  - "Analyze the following code: `[User-provided code]`. Determine the programming language used. Create a file named `solution.[language extension]` (e.g., `solution.py`, `solution.java`) inside the problem file (`[Problem Number]-[Problem Name]`). Place the provided code into this file."
  - "Add a descriptive comment at the beginning of the code file, indicating the problem number, problem name, and the approach used in the solution (e.g., 'Two Sum - Hash Map Approach')."
  - Prompt 3.1.1: "Generate alternative solution. If you know of multiple common approaches to solve the problem, generate separate solution files for each approach (e.g., `solution_bruteforce.cpp`, `solution_hashmap.java`)."
- Prompt 3.2 (If the user does not provide a solution):
  - "Generate solutions in Python for the LeetCode problem: `[Problem Name]` (Number: `[Problem Number]`). The solutions should be well-commented. Create files named `solution.py`,"
  - "Add a descriptive comment at the beginning of each code file, indicating the problem number, problem name, and the approach used in the solution (e.g., 'Two Sum - Hash Map Approach')."
  - "If you know of multiple common approaches to solve the problem, generate separate solution files for each approach (e.g., `solution_bruteforce.py`, `solution_hashmap.py`)."
  - Create for each related topic to the question a file with well structured explanation for this topic at the end list the problem with a link (markdown)
- Step 4: Problem README Generation (Enhanced)
- Prompt 4: "Generate a `README.md` file for the problem: `[Problem Name]` (Number: `[Problem Number]`, Difficulty: `[Difficulty]`).
- "The `README.md` file should follow this template:"

- # [Problem Number]. [Problem Name], Difficulty: [Difficulty]

- ## Problem Description

      [Paste the problem description here. If the user provided the description, use that. Otherwise, fetch it from LeetCode. If fetching from LeetCode is not possible, leave a placeholder: "[TODO: Fetch problem description from LeetCode]" and inform the user.]

      [Include examples from the problem description.]

      Constraints:

      [List the constraints from the problem description. If fetching from LeetCode is not possible, leave a placeholder: "[TODO: Fetch constraints from LeetCode]".]

- ## Approach(es)

      [Provide a detailed explanation of each solution approach implemented. Analyze time and space complexity. Include diagrams or illustrations if helpful. Structure this section with subsections for each approach.]

- ### [Approach 1 Name] (e.g., Hash Map Approach)

  - Algorithm:
  - [Provide a step-by-step explanation of the algorithm. Be thorough and clear.]
  - [Explain the underlying design principles and the rationale for choosing this approach.]
    - Data Structures:
  - [Describe the data structures used and why they are suitable for this approach.]
    - Time Complexity:
  - [Analyze the time complexity of the algorithm.]
    - Space Complexity:
  - [Analyze the space complexity of the algorithm.]
    - Trade-offs:
  - [Discuss any trade-offs associated with this approach, such as performance vs. memory usage or implementation complexity.]

       [Repeat subsections for other approaches, if available.]

    - ## Code

      [Provide a brief overview of each solution implemented.]

      Approach then /LINKTO_SOLUTION_FILE like [Recursive Approach](./solution_recursive.py)

    - ## Notes (Optional)

      [Include any alternative approaches considered but not implemented, potential optimizations, common pitfalls, lessons learned, or links to relevant resources. If no notes are needed, this section can be omitted.]
  - Topic Extraction :  Ideally, the system should be able to extract relevant topics for each problem (e.g., "Array," "Hash Table," "Dynamic Programming") and include them in the problem list with explanation in separate file each.
