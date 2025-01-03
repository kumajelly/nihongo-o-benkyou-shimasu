# Nihongo o Benkyou Shimasu

This repository automates the process of improving Japanese language skills through the power of structured, daily learning and spaced repetition. It was created as a way to make learning relevant and engaging while helping to tackle the challenges of language acquisition.

---

## **Why This Project Exists**

The project was born out of my desire to improve my Japanese, especially to better communicate with my wife's family. Recognizing my struggle with the language, I realized I needed a method that was both structured and practical. Writing daily summaries provided a way to make the process of learning Japanese relevant, interesting, and personal. By turning everyday events into material for study, it accomplished multiple goals:

1. **Increased Relevance**: The daily summaries are directly related to my life, ensuring that the vocabulary and grammar I learn are practical and immediately useful.
2. **Enhanced Motivation**: Writing these summaries keeps the learning process interesting and prevents it from feeling like a chore.
3. **Encouraging Consistency**: The automation ensures I stay disciplined and accountable to a daily practice routine.

This system combines automation and personalization to streamline the study process and make the journey more effective.

---

## **How It Works**

1. **Daily Summaries**:
   - Each day, a summary of daily activities is written in English and stored in the `daily-summaries` directory.
   - A scheduled GitHub Action processes the summary, translating it into Japanese (JLPT N5 level) with detailed annotations, including:
     - Translation in Japanese (with kanji, hiragana, and grammar).
     - Romanized pronunciation (romaji).
     - Sentence breakdown (particles, verbs, adjectives, and grammar explanations).
     - Vocabulary list with meanings, parts of speech, and example sentences.
     - The original English text for reference.

2. **Monthly Summaries**:
   - At the end of each month, a workflow aggregates all processed daily summaries into a single file stored in the `monthly-summaries` directory.
   - The monthly summary includes:
     - A vocabulary frequency analysis at the top, which highlights the words encountered, their meanings, and their usage frequency.
     - All daily summaries in reverse chronological order.

3. **Email Notifications**:
   - Both daily and monthly summaries can be emailed directly, with the content of the summary included in the body of the email for easy reference and review.

4. **OpenAI Integration**:
   - Leveraging the OpenAI API, the project generates translations and detailed annotations. This ensures high-quality language outputs while saving time on manual translations.

---

## **A Seamless Workflow**

To make the system as accessible and efficient as possible, it integrates seamlessly into my daily routines:

1. **Writing Summaries**:
   - I use **Drafts for iOS** with an action that quickly saves my English daily summaries into the correct `daily-summaries` directory in the repository.

2. **Pushing Summaries**:
   - Using **Working Copy for iOS**, I push the updates to GitHub.

3. **Receiving Study Sheets**:
   - Once the study sheet is created by the OpenAI API, I can read it in:
     - **iA Writer** (Markdown editor available on all devices).
     - My email inbox for quick and convenient access across work and home computers, or on the go.

### **Why Email?**
The email-based system ensures:
- **Accessibility**: I can view the study sheet anywhere, whether on my phone, work PC, or home laptop.
- **Convenience**: Email is an always-available platform, removing the need to open additional apps or tools.
- **Cross-Device Sync**: Study sheets are accessible and consistent across all my devices.

---

## **Goals Achieved**

- **Practical Learning**: By writing about daily life, the project ensures that language learning is tied to real-world scenarios, making it more practical and engaging.
- **Accountability**: Automation ensures consistency and discipline in daily practice.
- **Communication with Family**: The ultimate goal of the project is to improve communication with my wife’s family by becoming more proficient in Japanese.

---

## **How to Use**

1. **Daily Summary**:
   - Write your daily summary in English and save it in the `daily-summaries` directory (e.g., `2025-01-01.txt`).
   - The workflow will process the file automatically and create a translated summary in the `processed` directory.

2. **Monthly Summary**:
   - Run the monthly summary workflow (scheduled to run automatically on the 1st of each month).
   - The aggregated summary will appear in the `monthly-summaries` directory, complete with vocabulary analysis.

3. **Email Delivery**:
   - The workflows can send both daily and monthly summaries via email for easy access and review.

---

## **Future Enhancements**

- Expanding vocabulary insights with advanced grammar analysis.
- Adding support for higher JLPT levels as proficiency improves.
- Incorporating writing feedback into the summaries to refine grammar and style.

---

This project represents the perfect marriage of technology and personal development, making language learning accessible, structured, and tailored to real life. If you’re looking to learn Japanese—or any language—this could be a great starting point!
