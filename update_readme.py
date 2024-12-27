import os
import re
from collections import defaultdict


def get_problem_data():
    """
    Parses problem data from the 'problems' directory.
    Returns a list of dictionaries, where each dictionary represents a problem.
    """
    problems = []
    problems_dir = "problems"

    for problem_folder in sorted(os.listdir(problems_dir)):
        match = re.match(r"(\d+)-([\w-]+)", problem_folder)
        if match:
            problem_number = match.group(1).lstrip("0")
            problem_name = match.group(2).replace("-", " ").title()
            readme_path = os.path.join(problems_dir, problem_folder, "README.md")
            solution_files = [
                f
                for f in os.listdir(os.path.join(problems_dir, problem_folder))
                if f.startswith("solution")
            ]

            try:
                with open(readme_path, "r") as f:
                    readme_content = f.read()
                    difficulty = re.search(
                        r"## Problem Description\n.*Difficulty: ([\w]+)", readme_content
                    ).group(1)
            except:
                difficulty = "Unknown"

            solutions = []
            for solution_file in solution_files:
                language = solution_file.split(".")[1]
                solutions.append(
                    {
                        "language": language,
                        "path": os.path.join(
                            problems_dir, problem_folder, solution_file
                        ),
                    }
                )

            problem_url = f"https://leetcode.com/problems/{match.group(2)}/"

            problems.append(
                {
                    "number": problem_number,
                    "name": problem_name,
                    "difficulty": difficulty,
                    "solutions": solutions,
                    "url": problem_url,
                }
            )

    return problems


def get_topic_data():
    """
    Parses topic data from the 'topics' directory.
    Returns a dictionary where keys are topics and values are lists of problem numbers.
    """
    topics = defaultdict(list)
    topics_dir = "topics"

    for topic_file in os.listdir(topics_dir):
        if topic_file.endswith(".md"):
            topic_name = topic_file[:-3].title()
            with open(os.path.join(topics_dir, topic_file), "r") as f:
                content = f.read()
                # Extract problem numbers using regex (assuming they are linked like [1. Two Sum](...))
                problem_numbers = re.findall(r"\[(\d+)\.", content)
                topics[topic_name].extend(problem_numbers)

    return topics


def generate_problems_by_number_table(problems):
    """Generates the Markdown table for 'Problems Solved' -> 'By Number'."""
    table = [
        "| Problem Number | Problem Name | Difficulty | Solution |",
        "| :------------- | :----------- | :--------- | :------- |",
    ]
    for problem in problems:
        solution_links = ", ".join(
            [f"[{sol['language']}]({sol['path']})" for sol in problem["solutions"]]
        )
        table.append(
            f"| {problem['number']} | [{problem['name']}]({problem['url']}) | {problem['difficulty']} | {solution_links} |"
        )
    return "\n".join(table)


def generate_problems_by_topic_table(problems, topics):
    """Generates the Markdown table for 'Problems Solved' -> 'By Topic'."""
    table = ["| Topic | Problems |", "| :---- | :------- |"]
    for topic, problem_numbers in topics.items():
        problem_links = []
        for problem in problems:
            if problem["number"] in problem_numbers:
                problem_links.append(
                    f"[{problem['number']}. {problem['name']}]({problem['url']})"
                )
        table.append(f"| {topic} | {', '.join(problem_links)} |")
    return "\n".join(table)


def generate_problems_by_difficulty_table(problems):
    """Generates the Markdown table for 'Problems Solved' -> 'By Difficulty'."""
    table = ["| Difficulty | Problems |", "| :--------- | :------- |"]

    problems_by_difficulty = defaultdict(list)
    for problem in problems:
        problems_by_difficulty[problem["difficulty"]].append(problem)

    for difficulty, problems in sorted(problems_by_difficulty.items()):
        problem_links = [
            f"[{problem['number']}. {problem['name']}]({problem['url']})"
            for problem in problems
        ]
        table.append(f"| {difficulty} | {', '.join(problem_links)} |")
    return "\n".join(table)


def generate_progress_tracker_table(problems):
    """Generates the Markdown table for the 'Progress Tracker'."""

    difficulty_counts = defaultdict(int)
    total_solved = 0

    for problem in problems:
        difficulty_counts[problem["difficulty"]] += 1
        total_solved += 1

    table = [
        "| Difficulty | Solved | Total | Percentage |",
        "| :--------- | :----- | :---- | :--------- |",
    ]

    for difficulty in ["Easy", "Medium", "Hard"]:
        solved = difficulty_counts[difficulty]
        # Assuming you know the total number of problems for each difficulty
        total = {
            "Easy": 100,  # Replace with actual counts
            "Medium": 150,
            "Hard": 50,
        }.get(difficulty, 0)
        percentage = (solved / total * 100) if total > 0 else 0
        table.append(f"| {difficulty} | {solved} | {total} | {percentage:.1f}% |")

    # Calculate overall totals
    total_problems = sum(
        {
            "Easy": 100,  # Replace with actual counts
            "Medium": 150,
            "Hard": 50,
        }.values()
    )  # Sum of total problems for all difficulties

    overall_percentage = (
        (total_solved / total_problems * 100) if total_problems > 0 else 0
    )
    table.append(
        f"| **Total** | **{total_solved}** | **{total_problems}** | **{overall_percentage:.1f}%** |"
    )

    return "\n".join(table)


def update_readme(problems, topics):
    """Updates the README.md file with the generated tables."""
    with open("README.md", "r") as f:
        readme_content = f.read()

    # Generate tables
    problems_by_number_table = generate_problems_by_number_table(problems)
    problems_by_topic_table = generate_problems_by_topic_table(problems, topics)
    problems_by_difficulty_table = generate_problems_by_difficulty_table(problems)
    progress_tracker_table = generate_progress_tracker_table(problems)

    # Update tables in README (using regex to find and replace)
    readme_content = re.sub(
        r"(## Problems Solved\n\n### By Number\n\n)[\s\S]*?(### By Topic)",
        r"\1" + problems_by_number_table + r"\n\n\2",
        readme_content,
    )

    readme_content = re.sub(
        r"(### By Topic\n\n)[\s\S]*?(### By Difficulty)",
        r"\1" + problems_by_topic_table + r"\n\n\2",
        readme_content,
    )

    readme_content = re.sub(
        r"(### By Difficulty\n\n)[\s\S]*?(## How to Use)",
        r"\1" + problems_by_difficulty_table + r"\n\n\2",
        readme_content,
    )

    readme_content = re.sub(
        r"(## Progress Tracker\n\n)[\s\S]*?(## Problems Solved)",
        r"\1"
        + progress_tracker_table
        + r"\n\n_Last updated: "
        + os.popen("date").read().strip()
        + r"_\n\n\2",
        readme_content,
    )

    with open("README.md", "w") as f:
        f.write(readme_content)


if __name__ == "__main__":
    problems = get_problem_data()
    topics = get_topic_data()
    update_readme(problems, topics)
