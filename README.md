# Personalized Letter Generator

- The Personalized Letter Generator is a Python program that takes a list of names from a file and a letter template from another file. It then generates personalized letters for each name by replacing the placeholder [name] in the template with the actual name from the list. The generated letters are saved in separate files for each name.

---

### Features:

- Personalized Letters: The program replaces the placeholder [name] in the template with each name from the list.
- Automated File Creation: It automatically creates a new file for each name, saving the personalized letter in the "Output" folder.
- Simple Text Manipulation: Uses basic string replacement to generate the customized letters.
- Batch Processing: Handles multiple names and creates personalized letters in bulk.

---

### How It Works:

- Name List: The program reads names from a file (name list.txt).
- Template Letter: It reads the letter template from letter template.txt, where [name] is a placeholder for the actual name.
- Customization: For each name in the list, it strips any extra spaces, replaces [name] with the current name, and creates a new letter.
- Output: For each name, a new file is created in the Output folder, containing the personalized letter.
