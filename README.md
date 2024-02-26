# cli-lingo
**CLI tool** to quickly translate languages into English.


### Quick Install:
- `git clone https://github.com/critnull/cli-lingo@latest`
- `cd cli-lingo`
- `pip install -r requirements.txt`
> Note: If you're having issues, it's the **googletrans** module you need from **requirements.txt**

### Usage Examples:
- `python3 cli-lingo.py "我是一个机器人，我需要上油"`
- `python3 cli-lingo.py "Ich bin ein Roboter und muss geölt werden."`
> Fun tip: You can use this command to quickly rename files into English, eg:
> `mv "电视遥控器手册.pdf" "$(python cli-lingo.py "电视遥控器手册").pdf"`
