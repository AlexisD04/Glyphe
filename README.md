# PEN-TESTING FRAMEWORK

## QUICK START

To launch the framework, run the following command in your terminal:

```bash
chmod +x glyphe.sh
./glyphe.sh
```

A Python environment with all required modules is automatically created and loaded when the framework starts.

### AUTHENTIFICATION

- **Username:** *guest*
- **Password:** *guest*

### NAVIGATION

- Select a tool by entering its corresponding number.
- Use the *leave* option to exit the current menu or close the framework.

##  CONFIGURATION

To use the **shodan** tool, add your API key to the *config.py* file:

```python
SHODAN_API_KEY = "your_api_key_here"
```

**Note**: Through the API, free Shodan accounts have limited access to data.

## FEATURES

### AVAILABLE TOOLS

| Tool        | Description                                                                                     | Status                     |
|-------------|-------------------------------------------------------------------------------------------------|----------------------------|
| **Whois**   | Retrieves public registration details for a domain or IP address.                               | To improve                 |
| **Shodan**  | Search engine for internet-connected devices. Identifies exposed systems and vulnerabilities.   | Requires API key           |
| **HTTrack** | Website copier tool for offline browsing.                                                       | Next implementation        |

### PLANNED FEATURES

- Additional pen-testing tools
- Rework of the input command style
- More options on the tools
- Output saving to files
- Secure/non-secure profiles for project isolation
- Customizable dashboards for each profile
- Improved UI and customization options

## ADDING A NEW TOOL

To add a custome tool (e.g. in the *access* category):

1. **Create a Python file** in the appropriate subdirectory:

```bash
touch core/tools/access/my_tool.py
```

2. **Register the tool** in *tools/_init_.py*:

```python
my_tool = TOOLS["main_my_tool"]
toolSetAccess = [
    ...
    ("my_tool", my_tool),
    ("Leave", lambda: None)
]
```

3. **Add dependencies** (if any) in the *requirements.txt*:

## DEPENDENCIES & EXTERNAL CODE

- [python-whois](https://github.com/relip/python-whois)
- [shodan-python](https://github.com/achillean/shodan-python)
- [pyhttrack (modified)](https://github.com/riodevnet/pyhttrack/tree/v1.1.3)