
**Action Plan:**

1. **Refine and Finalize the Algorithm and Checklist**:
   - Develop a comprehensive algorithm and checklist for solving coding tasks both at home and during interviews.

2. **Practice Asking Clarifying Questions**:
   - Focus on identifying and formulating clarifying questions during task-solving.
   - Make it a habit to think about relevant clarifying questions for each step of the process.

3. **Create an Interview Process Checklist**:
   - Draft a structured checklist for approaching tasks in interviews to ensure a clear and consistent problem-solving methodology.

4. **Simulate Clarifying Question Scenarios**:
   - Take a few sample interview questions and generate potential clarifying questions for each. This will help you prepare for real-world scenarios and improve your ability to think critically under pressure.

prepare list of tricks/tips to find more optimal solution. Like, you can use an auxiliary data structure..

There are also some interesting insights available here:
<https://www.techinterviewhandbook.org/coding-interview-prep/>
<https://www.techinterviewhandbook.org/coding-interview-cheatsheet/>
<https://www.techinterviewhandbook.org/coding-interview-techniques/>

# Persons

You can learn a bunch of cool tricks from these persons

site:<https://leetcode.com/> "StefanPochmann"
site:<https://leetcode.com/> "lee215"
site:<https://leetcode.com/> "Awice"
site:<https://leetcode.com/> "zhijun_liao"
site:<https://leetcode.com/> "fun4LeetCode"
site:<https://leetcode.com/> "DBabichev"
site:<https://leetcode.com/> "agave"
site:<https://leetcode.com/> "yegao"

# Before solving

Coding questions tend to be vague and underspecified on purpose to allow the interviewer to gauge the candidate's attention to detail and carefulness.

- Do not jump straight into coding, take a few minutes to understand the problem and ask any clarifying questions (but not too long!).
- Make a plan. Be wary of jumping into code without thinking about your program's high-level structure. You don't have to work out every last detail (this can be difficult for more meaty problems), but you should give the matter sufficient thought. Without proper planning, you may be forced to waste your limited time reworking significant parts of your program.
- Describe your solution to your interviewer and get their thoughts on your solution.

# Learn to Ask Clarifying Questions

Clarify any assumptions you made subconsciously. **Many questions are under-specified on purpose.** Some interviewers deliberately omit important details to see if you ask the right questions. E.g. a tree-like diagram could very well be a graph that allows for cycles and a naive recursive solution would not work.

Always seek clarification about the question upon hearing it even if it you think it is clear to you. You might discover something that you have missed out and it also sends a signal to the interviewer that you are a careful person who pays attention to details. Some interviewers deliberately omit important details to see if you ask the right questions.

Before jumping into writing code, a good candidate will always ask clarifying questions. This serves three main purposes:

- It bounds the problem space. For example, perhaps you ask the interviewer, "Is it guaranteed that all integers in this array are positive?". If the answer is yes, then you don't have to account for the entire negative integer space, which could potentially make the problem much easier to solve.
- It shows the interviewer that you're proactively thinking about edge cases. Interviews are as much about showing that you're capable of thinking critically and thoroughly as it is about raw coding ability.
- It allows you and the interviewer to agree on an understanding of the problem. Occasionally, I've given a problem to a candidate and they solved a slightly different problem. Making sure that you and your interviewer are on the same page about what your task is before you begin.

For data structures, I've divided the questions into two broad categories:

- Questions about the input/output of the function (the function signature)
- Questions about allowable/preferred solving methods (used in the body of the function)

*Make sure to clarify the following things:*

- *Ask for an example* of input and output
- Clarify the data type
- Clarify any kinds of restrictions in range (e.g will there be numbers bigger than the largest int?)
- Ask about whether you need to deal with certain edge cases or not.
- *Make sure you can or cannot use certain libraries* and features of the language you are programming in.
- If you have 2 solutions in mind ask whether it is more important to prioritize time or space complexity

For example:

- How big is the size of the input?
- How big is the range of values?
- What kind of values are there? Are there negative numbers? Floating points? Will there be empty inputs?
- Are there duplicates within the input?
- What are some extreme cases of the input?
- Can I destroy or mutate the original array/graph/data structure?
- How is the input stored? If you are given a dictionary of words, is it a list of strings or a Trie?
- Should the list be sorted in ascending or descending order?
- What data does the list contain?
- Is the data given to me as static input or is it a stream of input?
- Can you give me an example of what the input and output of my solution should look like?

**In the end work through a small example to ensure you understood the question.**

# Planning the solution and solving the problem

## Work out and optimize your approach with the interviewer

The worst thing you can do next is jump straight to coding - interviewers expect there to be some time for a 2-way discussion on the correct approach to take for the question, including analysis of the time and space complexity.

This discussion can range from a few minutes to up to 5-10 minutes depending on the complexity of the question. This also gives interviewers a chance to provide you with hints to guide you towards an acceptable solution.

> Explain a few approaches that you could take at a high level (don't go too much into implementation details). Discuss the tradeoffs of each approach with your interviewer as if the interviewer was your coworker and you all are collaborating on a problem.

Solving techique. An **example** can dramatically improve your ability to solve an interview question, and yet so many candidates just try to solve the question in their heads. Example should be sufficiently large, specific and not a special case.

State a brute-force. Start with a brute force approach, communicate it to the interviewer, explain the time and space complexity and why it is bad. It is unlikely that the brute force approach will be one that you will be coding. Despite being possibly slow, a brute force algorithm is valuable to discuss. *It's a starting point for optimizations, and it helps you wrap your head around the problem.*

At this point, the interviewer will usually pop the dreaded "Can we do better?" question, meaning that they are looking for a more optimal approach. In my opinion, this is usually the hardest part of the interview. In general, look for repeated work and try to optimize them by potentially caching the calculated result somewhere and reference it later, rather than having to compute it all over again. There are some tips on tackling topic-specific questions that I dive into details below.

After you have sufficiently clarified the scope and intention of the problem, explain your high level approach to the interviewer even if it is a naive solution. If you are stuck, consider various approaches and explain out loud why it will/will not work. Sometimes your interviewer might drop hints and lead you towards the right path.

You can sort an input array or make some another changes to an input data if you stuck with a solution. After it you can reason more clearly about combinatorics of problem and use heuristics to solve the problem. #coding/tip #tip #heuristics

Appraisal criteria when comparing solutions:
Time and space complexity
Almost every interviewer will ask for the time and space complexity of the algorithm. Proactively providing this information, instead of waiting for them to ask, shows the interviewer that you're familiar with these concepts and can calculate them easily.

Some things to keep in mind:

- When initially thinking about the problem, try to think what the absolute best and worst case complexity would be. For example, to find a certain element in an unsorted list, we know that we will have to look at every element in the list at least once, so we're lower bounded by O(n).
- Try to "stress test" your complexity, especially if it depends on two or more variables. For example, if your algorithm was O(n * k): What happens if k is extremely small? What happens when k approaches n? Occasionally, you'll find that one algorithm is optimal for certain values of n and k, and another algorithm is optimal for different values of n and k.
- For memory constraints, try to reason about if you really need to keep track of all the values in your data structures. Also, be cognizant of the fact that certain functions in different coding languages may use additional memory. A good example of this is list slicing in Python, which creates a new list (potentially another O(n) memory usage).
- Think out loud. Explain your thought process to your interviewer as you code. This helps you more fully communicate your solution, and gives your interviewer an opportunity to correct misconceptions or otherwise provide high-level guidance.
- Break the problem down and define abstractions. One crucial skill the recruiters look for is the ability to handle complexity by breaking problems into manageable sub-problems. For anything non-trivial, you'll want to avoid writing one giant, monolithic function. Feel free to define helper functions, helper classes, and other abstractions to reach a working solution. You can leverage design patterns or other programming idioms as well. Ideally, your solution will be well-factored and as a result easy to read, understand, and prove correct.
- Optimize. Proactively suggest ways to optimize to the interviewer and get their feedback to ensure what you're trying to do is not overly complex and is correct then code it up.
- Consider edge cases (extreme test cases), test your code, restate complexity

## While solving (tricks)

-

## While coding

**Only start coding after you and your interviewer have agreed on an approach and they have given you the green light.**

Write your code with good coding style. Reading code written by others is usually not an enjoyable task. Reading horribly-formatted code by others makes it worse. Your goal is to make your interviewer understand the code you have written so that they can quickly evaluate if your code does what you say it does and whether it solves the given problem. Use clear variable names, avoid single letter names unless they are for iteration. However, if you are coding on a whiteboard, you might not want to use extremely verbose variable names for the sake of reducing the amount you have to write. Abbreviations are usually fine if you explain what it means beforehand.
*Always be explaining what you are currently writing/typing to the interviewer.* Explain what you are coding/typing to the interviewer, what you are trying to achieve. This is not about literally reading out what you are typing to the interviewer. Talk about the section of the code you are currently implementing at a higher level, explain why it is written as such and what it is trying to achieve.
While coding, if you find yourself copying and pasting code, consider whether it is necessary. If you find yourself copying and pasting one large chunk of code spanning multiple lines, it is usually an indicator that you can refactor by extracting those lines into a function and defining parameters for the differences in them. If it is just a single line you copied, usually it is fine. Do remember to change the respective variables in your copied line of code where relevant. Copy-paste errors are a common source of bugs even in day-to-day coding!

- Ask for permission to use trivial functions without having to implement them.
- Write in a modular fashion, going from higher-level functions and breaking them down into smaller helper functions.
- If you are cutting corners in your code, state that out loud to your interviewer and say what you would do in a non-interview setting (no time constraints). E.g., "Under non-interview settings, I would write a regex to parse this string rather than using split() which may not cover certain edge cases."

# After coding

- Scan through your code for mistakes - such as off-by-one errors.
- Brainstorm edge cases with the interviewer and add additional test cases.
- Step through your code with those test cases.
- Look out for places where you can refactor.
- Reiterate the time and space complexity of your code. This allows you to remind yourself to spot issues within your code that could deviate from the original time and space complexity.
- Explain trade-offs and how the code / approach can be improved if given more time.

After you have finished coding, do not immediately announce to the interviewer that you are done. In most cases, your code is usually not perfect and contains some bugs or syntax errors. What you need to do now is to review your code.

- Review and refactor. Firstly, look through your code from start to finish as if it is the first time you are seeing it, as if it was written by someone else and you are trying to spot bugs in it. That's exactly what your interviewer will be doing. Look through and fix any minor issues you may find.
- Step through your code and test it. One of the best ways to check your work is to simulate how your code executes against a sample input. Take one of your earlier examples and make sure your code produces the right result. Huge caveat here: when mentally simulating how your code behaves, your brain will be tempted to project what it wants to happen rather than what actually says happen. Fight this tendency by being as literal as possible.
- Next, come up with small test cases and step through the code (not your algorithm!) with those sample input. What interviewers usually do after you have finished coding would be to get you to write tests. It is a huge plus if you write tests for your code even before they prompt you to do so. You should be emulating a debugger when stepping through and jot down or say out the values of the important variables as you step through the lines of code.
- Refactoring. If there are huge duplicated chunks of code in your solution, it would be a good chance to refactor it and demonstrate to the interviewer that you are one who values code quality. Also look out for places where you can do short-circuit evaluation.
- Think about edge cases. Naturally, you should strive for a solution that's correct in all observable aspects. Sometimes there will be a flaw in the core logic of your solution, but more often your only bugs will be in how you handle edge cases. (This is true of real-world engineering as well.) Make sure your solution works on all edge cases you can think of.
- Restate the complexity. Is it the same, or different to your initial thinking based on what you have actually coded up? Make sure you're thinking about both space and time. Lastly, give the time/space complexity of your code and explain why it is such. You can even annotate certain chunks of your code with the various time/space complexities to demonstrate your understanding of your code and the APIs of your chosen programming language. Explain any trade-offs in your current approach vs alternative approaches, possibly in terms of time/space.
- Explain the shortcuts you took. If you skipped things for reasons of expediency that you would otherwise do in a "real world" scenario, please let us know what you did and why. For example, "If I were writing this for production use, I would check an invariant here." Since an interview is an artificial environment, this gives him/her a sense for how you'll treat code once you're actually on the job.

If your interviewer is happy with the solution, the interview usually ends here. It is also not uncommon that the interviewer asks you extension questions, such as how you would handle the problem if the whole input is too large to fit into memory, or if the input arrives as a stream. This is a common follow-up question at Google where they care a lot about scale. The answer is usually a divide-and-conquer approach — perform distributed processing of the data and only read certain chunks of the input from disk into memory, write the output back to disk, and combine them later on.

# Remember

- Interviewer can only evaluate you on the code you write.
- Talk about what you are doing throughout the interview. If you need to be quiet to think, that's great — just let the interviewer know.
- Think out loud if you are working through a solution you are presented with as the Engineer will want to know how you approach and troubleshoot problems.
- If the interviewer gives you hints to improve your code, take them and run with them. It is good to adjust and work through the problems with the interviewer to show your thought process and problem solving ability.
- Discuss initial ideas and solutions with your interviewer, which will help you to clarify any ambiguity.
- Take hints from your interviewer to showcase your thought pnrocess and problem-solving ability.
- Generally avoid solutions with lots of edge cases or huge if/else if/else blocks. Deciding between iteration and recursion is always an important step.
- Think about different algorithms and algorithmic techniques (sorting, divide-and-conquer, dynamic programming/memorization, recursion)
- Think about data structures, particularly the ones used most often (Array, Stack/Queue, Hashset/Hashmap/Hashtable/Dictionary, Tree/Binary Tree, Heap, Graph, Bloom Filter, etc.)
- Don't worry about rote memorization such as runtimes or API/native calls. It's good to know how to figure out approximate runtimes on the fly but the code you write is more important.
- You will be asked about O(Memory) constraints, the complexity of the algorithm you are writing and its runtime — O(N²), O(N) etc
- Important — think about testing your code throughout the interview
- Make sure you review recursion.
- Make sure you know what your base case is. Bonus points available for talking about or implementing the dynamic programming solution.
- Practice coding on a whiteboard.

Advices:
You need to learn to communicate your thoughts. It can be hard, awkward and unnatural — so it requires a lot of practice.
You neet be active at interview

# Coding Signals

The point of interviews is for interviewers to extract signals from certain candidate behaviors. In coding interviews, the signals can be broadly classified into the following categories: Problem Solving, Technical Competency, Testing, and Communication.
When interviewers take down interview feedback, these are likely what is on their feedback sheet.

Problem solving
Understanding the problem

- 👍 Understood the key aspects of the problem quickly
- 👎 Had difficulty in understanding the key aspects of the problem
Solution/approach
- 👍 Approached the problem in a systematic and logical manner
- 👎 Did not demonstrate a logical thought process for approaching the problem
Improving the solution
- 👍 Suggested a more efficient solution when prompted, or proactively coming up with a better solution
- 👎 Had difficulty in coming up with a more efficient solution even after being prompted
Trade-offs analysis
- 👍 Explained the trade-offs of different approaches clearly and correctly
- 👎 Failed to describe trade-offs of different approaches
Hinting
- 👍 Did not require any major hints
- 👎 Needed plenty of hints

Technical competency
Speed

- 👍 Quickly implemented a working solution
- 👎 Was not able to complete the solution
Correctness/Accuracy
- 👍 Implemented the solution correctly (e.g., working solution, minimal bugs)
- 👎 Unable to correctly implement a solution (e.g., non-working solution, incorrect logic, and/or serious bugs)
Complexity analysis
- 👍 Able to determine the algorithmic time and space complexity
- 👎 Was not able to determine the algorithmic time and space complexity (explain why TC came up with such an answer)
Mastery of chosen programming language
- 👍 Demonstrated mastery of the chosen programming language
- 👎 Does not seem to be familiar with the chosen programming language Implementation
- 👍 Implementation was clean and straightforward
- 👎 Implementation was unnecessarily complex and/or messy
Coding style
- 👍 Coding style was neat (proper indentation, spacing and no bad practices)
- 👎 Coding style was messy (inconsistent indentation, weird spacings, etc)

Testing
Common cases

- 👍 Tested their code against various typical cases
- 👎 Failed to test the code against typical cases
Corner cases
- 👍 Found and handled corner/edge cases
- 👎 Failed to consider corner/edge cases
Self-correction
- 👍 Identified and corrected bugs in the code (where applicable)
- 👎 Was not able to discover and fix bugs even after being prompted

Communication
Clarify problem

- 👍 Appropriately asked good, clarifying questions about the problem
- 👎 Failed to confirm understanding/ask appropriate questions
Communicating approach
- 👍 Able to explain overall approach, technical terms and acronyms (where applicable)
- 👎 Failed to effectively explain overall approach, technical terms and acronyms (where applicable)

# Applications

## Notes from LT guy

Other things like, candidate should be able to finish leetcode medium problem in ==20 minutes==. Leaked problem will be banned, but only if it is identical and marked as "asked in Google interview".
They are really picky with the code. You must not take too many hints. You must not make careless mistakes. You must check corner case. And your solution cannot involve any inefficiency.

Leetcode problems usually don't need customized data structure. You are just given an array or a tree, and you start to code. Google interview will require you to build your own data structure, for example, to build a segment tree.

Leetcode problems come with boundary conditions and no bad inputs. Google interview will require you to check boundary conditions in the code. So, try to implement the checkings against boundary condition when practicing.

Leetcode problems come with test cases, especially the corner cases. Google interview will require you to make up the test cases. So, try to make up cases before you press submit. Try to get a higher AC rate.

Don't jump into coding but code fast. You need additional time to explain and dry-run your code. So practice is important. Practice more with trees. Especially, practice until you don't make off-by-1 error. Like, back to when you wrote a for-loop for the first time, you probably took some time to figure out it is `i < n` or `i <= n`, but now you just type the whole for-loop header without thinking.

Don't debate with the interviewer. You are not showing how convincing you are. You just take the hint and start over.

## What to do when stuck

Getting stuck during coding interviews is extremely common. But do not worry, that is part of the process and is a test of your problem solving abilities. Here are some tips to try out when you are stuck:

- Talk through what you initially thought might work and explain why it doesn't
o This can help guide you on the right track by avoiding the pitfalls

- Come up with more test cases and write them down
o A pattern may emerge

- Think about how you would solve it without a program
o You may spot a pattern and come up with a general algorithm for it

- Recall past questions related to the topic, what similar questions in the past have you encountered and what techniques did you use?

- Enumerate through the common data structures and whether they can be applied to the question
o Dictionaries/maps are extremely common in making algorithms more efficient

- Look out for repeated work and determine if you can cache those computations
o Trade off memory for speed

You have a solution. Now what?

# time-complexity

phrases:
The outer loop is invoked `n - 1` times, and the `i-th` iteration processes `n - 1`- i elements.

processing an element entails computing a difference, performing a compare, and possibliy updating a variable, all of which take constant time.
