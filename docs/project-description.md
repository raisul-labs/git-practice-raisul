# Git Practice Project — Project Description

## 1. Project Overview

The Git Practice Project is a simple Python-based calculator application developed as part of a Git & GitHub practical assignment.

The main purpose of this project is to demonstrate the practical use of Git for source code management, including repository initialization, file tracking, meaningful commits, feature branches, branch merging, and GitHub integration.

## 2. Project Objectives

The project was developed with the following objectives:

- Understand the basic Git workflow
- Initialize and manage a Git repository
- Create and organize project files
- Track changes using Git
- Write meaningful commit messages
- Create and work with feature branches
- Merge completed features into the main branch
- Connect a local repository with GitHub
- Push the project to a public GitHub repository
- Maintain a clean and professional project structure
- Implement basic error handling in Python

## 3. Application Description

The application is a command-line calculator written in Python.

When the program runs, it displays:

- Student name
- Current date
- Addition result
- Subtraction result
- Multiplication result
- Division result
- Division-by-zero error handling

The calculator functionality is organized into reusable functions, making the code easier to understand and maintain.

## 4. Application Features

### 4.1 Student Information

The application displays the student's name and the current date when the program starts.

### 4.2 Addition

The `add()` function returns the sum of two numbers.

Example:

10 + 5 = 15

### 4.3 Subtraction

The `subtract()` function returns the difference between two numbers.

Example:

10 - 5 = 5

### 4.4 Multiplication

The `multiply()` function returns the product of two numbers.

Example:

10 × 5 = 50

### 4.5 Division

The `divide()` function returns the division result.

Example:

10 ÷ 2 = 5.0

### 4.6 Error Handling

The application handles division by zero using exception handling.

Instead of allowing the program to crash, it displays:

Error: Cannot divide by zero

## 5. Project Structure

The project follows the required assignment structure:

    git-practice-raisul/
    │
    ├── README.md
    ├── .gitignore
    │
    ├── src/
    │   ├── main.py
    │   └── utils.py
    │
    └── docs/
        └── project-description.md

### File Responsibilities

| File | Purpose |
|---|---|
| `README.md` | Project overview and usage instructions |
| `.gitignore` | Prevents unnecessary files from being tracked |
| `src/main.py` | Main application entry point |
| `src/utils.py` | Calculator functions |
| `docs/project-description.md` | Detailed project documentation |

## 6. Git Branches

### feature/calculator

This branch was created to develop the initial calculator functionality.

Features implemented:

- Addition
- Subtraction
- Multiplication

After completing the feature, the branch was merged into `main`.

### feature/error-handling

This branch was created to improve the calculator functionality.

Features implemented:

- Division
- Division-by-zero error handling

After completing the feature, the branch was merged into `main`.

## 7. Git Workflow

The project follows a structured Git workflow:

    Initialize Repository
            ↓
    Create Project Structure
            ↓
    Create Initial Commit
            ↓
    Create Feature Branch
            ↓
    Develop Feature
            ↓
    Commit Changes
            ↓
    Merge Feature Branch
            ↓
    Improve Documentation
            ↓
    Add Additional Features
            ↓
    Connect GitHub Remote
            ↓
    Push to Public Repository

This workflow demonstrates how Git can be used to manage changes throughout the development lifecycle.

## 8. Commit Strategy

Meaningful commit messages were used to clearly describe each development step.

Examples of commits used in the project include:

- Initial commit: project structure and basic program
- Add gitignore file
- Add basic calculator functions
- Improve README formatting
- Add multiplication calculator function
- Update project description documentation
- Add calculator division error handling
- Add project usage instructions

Each commit represents a specific development or documentation change.

## 9. Technologies Used

The following technologies and tools were used:

- Python 3
- Git
- GitHub
- Visual Studio Code

## 10. Requirements

To run this project locally, the following software is required:

- Python 3.x
- Git
- A GitHub account for repository access

## 11. How to Run the Application

Clone the repository:

    git clone https://github.com/raisul-labs/git-practice-raisul

Navigate to the project directory:

    cd git-practice-raisul

Run the Python application:

    python src/main.py

## 12. Expected Output

    Name: Md Raisul Islam
    Today's Date: 2026-10-09

    Calculator
    Addition: 15
    Subtraction: 5
    Multiplication: 50
    Division: 5.0
    Error: Cannot divide by zero

## 13. GitHub Integration

The local Git repository is connected to a public GitHub repository.

The project demonstrates:

- Local repository management
- Remote repository configuration
- Pushing commits to GitHub
- Maintaining project history on GitHub
- Public repository access

## 14. Learning Outcomes

Through this project, the following practical skills were developed:

- Creating a Git repository
- Understanding Git staging
- Creating commits
- Writing meaningful commit messages
- Creating feature branches
- Switching between branches
- Merging branches
- Resolving basic workflow issues
- Connecting Git with GitHub
- Pushing code to a remote repository
- Maintaining project documentation

## 15. Conclusion

The Git Practice Project demonstrates a complete basic Git and GitHub workflow using a simple Python calculator application.

Although the application is intentionally simple, the project focuses on demonstrating important software development practices such as version control, structured development, meaningful commits, feature branching, documentation, and GitHub collaboration.

This project provides a practical foundation for using Git and GitHub in larger software development projects.

## 16. Author

**Md Raisul Islam**

GitHub Username: `raisul-labs`

Repository: `git-practice-raisul`