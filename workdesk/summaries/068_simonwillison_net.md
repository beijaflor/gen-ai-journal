This article, titled **"Cooking with Claude,"** is a blog post by Simon Willison (dated December 2025) exploring how Large Language Models (LLMs) can be used to coordinate complex culinary tasks through "vibe-coding" and vision capabilities.

Here is a summary of the key points:

### 1. The "Two-Recipe" Challenge
Willison frequently cooks meal kits (Green Chef) for four people, which requires preparing two different two-portion recipes simultaneously. This usually results in a chaotic "mad flurry" of trying to synchronize different timers and cooking steps.

### 2. The Experiment: Building a Custom App
To solve this, Willison used **Claude (specifically "Opus 4.5")** to automate the planning:
*   **Vision Task:** He took a single photo of two different recipe cards. Claude successfully extracted the detailed instructions from the image, despite the small text.
*   **Vibe-Coding:** He prompted Claude to build a custom, mobile-friendly, interactive web application (an "Artifact") to manage the workflow.
*   **App Features:** The app included a persistent start timer (using `localStorage`), countdowns for upcoming steps, and a combined timeline showing exactly when to start each task so both meals would finish at the same time.
*   **The Result:** Willison hosted the code himself and followed it to the minute. Both meals were served perfectly in 44 minutes.

### 3. General Cooking with LLMs
Beyond complex timing, the author uses LLMs for:
*   **Ingredient Identification:** Taking photos of unknown ingredients (like dried beans at a market) and asking for recipe ideas.
*   **"Hype-man" Mode:** Using prompts like "Get me excited about cooking with these!" to generate creative inspiration.
*   **The "Mean" Recipe Theory:** Willison suggests that LLMs are excellent at providing the "average" version of a dish—essentially a reliable baseline synthesized from thousands of internet recipes.
*   **Iterative Refinement:** He uses the models to handle substitutions (e.g., "make it vegan") or to improve flavors (e.g., repeatedly asking the model to "make it tastier").

### 4. Key Takeaways
*   **Pushing Boundaries:** The author argues that the best way to learn LLM capabilities is to give them tasks that seem slightly beyond their abilities.
*   **The "Vibe-Coding" Success:** He was impressed that a "chaotic" approach—relying on the LLM to extract data and write code without heavy manual oversight—resulted in a functional, error-free utility.
*   **Future Benchmarking:** He proposes a "cooking benchmark" for LLMs, where different models are judged on the actual taste and success of the recipes they generate.