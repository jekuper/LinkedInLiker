# LinkedIn Automation Tool

This is a LinkedIn automation tool built using **Python** and **Selenium**. It automates the process of engaging with posts on LinkedIn by:

- Liking posts with an appropriate reaction based on the post's text.

## Features

### Implemented Features
- **Login Automation**: Automatically logs into your LinkedIn account.
- **Post Engagement**: 
  - Selects posts from your feed.
  - If a post has fewer than 50 likes, it selects a random reaction and likes the post.
  - If a post has more than 50 likes, it has a 1% chance of liking the post; otherwise, the post is ignored.

### Planned Features
- **Commenting on Posts**: Automatically writes comments based on the post's text.
- **Local LLM Integration**: The tool will use a local Language Model (LLM) server that you can set up yourself.
- **Smart Post Selection**: Skips controversial posts based on LLM evaluation of the post's content.

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Install required libraries using the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Tool
To run the tool, execute the following command:
```bash
python3 main.py
```

### Configuration
Before running the tool, set up the configuration file:
1. Navigate to the `config` folder.
2. Use the provided `config.json.example` as a template.
3. Rename the file to `config.json` and populate it with your settings.

#### Configuration Parameters
| Parameter      | Type    | Description                                                                 |
|----------------|---------|-----------------------------------------------------------------------------|
| `llm_path`     | string  | Path to the LLM folder (future feature, not used currently).                |
| `username`     | string  | Your LinkedIn username.                                                     |
| `password`     | string  | Your LinkedIn password.                                                     |
| `manual`       | boolean | If `true`, the program will stop and wait for user input before each step.  |
| `post_count`   | integer | Number of posts to analyze in your feed.                                    |
| `pause_time`   | integer | Base time (in seconds) to pause after navigating to a post before liking it. A random number (0-20 seconds) will be added to this value for the final pause time. |

## Contribution
This tool is open source and welcomes contributions! Feel free to submit issues, suggest features, or create pull requests to help improve the tool.

---

Happy automating! 🚀
