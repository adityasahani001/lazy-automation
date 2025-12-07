# Lazy Photo Sorter – AI for Bharat Fellowship (Kiro Week 2: Lazy Automation)

This project is created as part of the **AI for Bharat Fellowship – Week 2 Challenge: Lazy Automation**.  
The objective of the weekly challenge is to identify a repetitive or boring digital task and automate it using a script.  
For this submission, I chose a common real-world problem:

> **“I hate manually renaming and organizing hundreds of photos, so I built a script that automates the entire process.”**

This repository contains the complete implementation, documentation, `.kiro` directory, testing steps, and usage instructions required for the Week-2 submission.

---

## 📘 Project Overview

Managing large numbers of photos is time-consuming and error-prone. Many devices generate filenames like:

- `IMG_20230415_145533.jpg`  
- `PXL_20221110_093311.jpg`  
- `DSC00123.JPG`

These filenames are inconsistent and do not help with chronological sorting or archival.

This automation script solves that problem by:

- Extracting **EXIF timestamps** (when available)  
- Falling back to **file modification time**  
- Renaming files into a clean, time-based pattern  
- Organizing them into structured folders  
- Supporting preview mode (`--dry-run`) to ensure safety  

This ensures that all photos follow a consistent naming format and are neatly organized by year and month.
## 📢 Official Blog Submission (AI for Bharat – Week 2)

As part of the Kiro Week 2: Lazy Automation challenge, I documented the entire problem, approach, solution, and development process in a detailed blog published on AWS Builder Center.

You can read the full blog here:

🔗 **AWS Builder Center Blog:**  
https://builder.aws.com/content/36WpDNZIRY5dGoJTTAAsF459YoX/automating-my-photo-organization-workflow-using-python-kiro-week-2-lazy-automation


---

## 🎯 Challenge Alignment (Why This Project?)

As part of the **Kiro Week 2: Lazy Automation Challenge**, the goal is to:

1. Identify a repetitive task  
2. Automate it with a script  
3. Document the process formally  
4. Showcase how Kiro accelerated development  
5. Publish both the repository and a technical blog post

This project has been designed to meet all these goals in a structured and professional manner.

---

## 🧠 Key Features

- **EXIF-based renaming:** Uses `DateTimeOriginal` when available  
- **Fallback timestamps:** Uses file modification time where EXIF is missing  
- **Consistent filename format:**  
  `YYYYMMDD_NNNN.ext`  
- **Automated folder structuring:**  
  Files organized into:  
  `DEST/YYYY/MM/`
- **Dry-run support:** Preview actions without modifying files  
- **Recursive mode:** Process all nested folders  
- **Extension filtering:** Limit processing to specific file types  
- **Collision-safe renaming:** Automatically appends suffixes to avoid overwrites  
- **Clean and modular code structure**

---

## 📁 Repository Structure

lazy-photo-sorter/
├─ .kiro/
│ └─ config.yaml
├─ src/
│ └─ rename_photos.py
├─ tests/
│ └─ test_rename_dryrun.md
├─ requirements.txt
├─ .gitignore
├─ README.md
└─ LICENSE


Each directory serves a clear purpose:

- `.kiro/` contains project metadata required for this challenge  
- `src/` includes the main automation script  
- `tests/` contains a simple reproducible dry-run test plan  
- `requirements.txt` lists dependencies  
- `.gitignore` ensures a clean repository  
- `README.md` provides complete documentation  
- `LICENSE` specifies usage permissions  

---

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/lazy-photo-sorter.git
cd lazy-photo-sorter

2. Create a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

🚀 Usage Instructions
Dry-run mode (recommended first)

Preview changes without modifying any files:

python3 src/rename_photos.py --source ./incoming --dest ./sorted --dry-run

Real execution
python3 src/rename_photos.py --source ./incoming --dest ./sorted

Recursive processing
python3 src/rename_photos.py -s ./incoming -d ./sorted -r

Extension filtering
python3 src/rename_photos.py -s ./incoming -d ./sorted -e .jpg .png

Verbose log output
python3 src/rename_photos.py -s ./incoming -d ./sorted --verbose

🧪 Testing

A simple manual testing plan is included in:

tests/test_rename_dryrun.md


It guides you through:

Preparing sample files

Running the script in dry-run mode

Verifying the rename and folder structure

Executing the final run

📦 The .kiro Directory (Challenge Requirement)

This repository includes a proper .kiro/config.yaml file at the root, as required for the fellowship challenge.

It describes the project, commands used, and notes about how Kiro assisted development.

Example:

project: lazy-photo-sorter
description: "Kiro Week 2 automation project"


The .kiro directory is intentionally not ignored in .gitignore.

⚡ How Kiro Helped in Development

Kiro accelerated the development workflow by:

Generating boilerplate code and argument parsing structure

Helping refine logic for EXIF extraction and fallback timestamps

Producing documentation, README drafts, and test plans

Assisting in validating command structure

Speeding up iteration during debugging

Providing structured prompts and scaffolding for the automation task

Screenshots and recordings of Kiro usage will be included in the accompanying AWS Builder Center blog post.

🛣️ Future Enhancements (Roadmap)

Potential improvements to extend functionality:

Duplicate detection using file hashing (MD5/SHA-1)

Support for video metadata (e.g., .mp4, .mov)

Undo/restore functionality through a log file

Thumbnail / contact sheet generator

Web-based or desktop GUI

Integration with cloud storage (AWS S3, Google Drive)

📄 License

This project is released under the MIT License.
You are free to modify, distribute, and build upon the work.

See the LICENSE file for full details.

📝 AI for Bharat – Week 2 Submission Checklist

This repository satisfies all requirements:

 Public GitHub repository

 .kiro directory at project root

 Complete automation script

 Requirements file included

 Test plan added

 Full README documentation

 AWS Builder Center blog post (to be published)

 Submit blog + repo link on dashboard

🙌 Acknowledgments

This project was developed as part of the AI for Bharat Fellowship Program,
under the Kiro Week-2: Lazy Automation module.
Thanks to the organizers and mentors for enabling hands-on learning through practical projects.

📬 Contact

Feel free to reach out via GitHub Issues or connect through the AI for Bharat community channels for any queries, suggestions, or improvements.

Happy Automating! 🚀


---
