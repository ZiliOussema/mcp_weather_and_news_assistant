# MCP Weather & News Assistant

An AI assistant project built with the **Model Context Protocol (MCP)** that connects an LLM to real-world data sources via custom MCP tools.  
It provides **real-time weather information** and **latest news headlines** by allowing the model to call external APIs through an MCP server.

This repository is mainly designed as a **portfolio project** to demonstrate practical MCP skills such as:
- Building an MCP server with custom tools
- Exposing tools with JSON schemas for validation
- Integrating external APIs (OpenWeatherMap, NewsAPI)
- Returning structured outputs to LLM clients
- Deploying MCP servers across multiple platforms

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Finding Your Project Path](#finding-your-project-path)
- [Deployment](#deployment)
  - [Claude Desktop](#1-claude-desktop)
  - [Continue (VS Code)](#2-continue-vs-code)
  - [Cline](#3-cline)
  - [Other MCP Clients](#4-other-mcp-clients)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)

---

## Features

- **Real-time Weather Data**: Get current weather conditions (temperature, humidity, wind speed, description) for any city
- **Latest News Articles**: Fetch top 5 news articles by topic using NewsAPI
- **MCP Protocol**: Standards-based integration with any MCP-compatible client using FastMCP
- **Two Tools**: `weather(city)` and `news(topic)` tools exposed via MCP
- **Secure**: API keys stored in environment variables using python-dotenv

---

## Prerequisites

Before deploying this MCP server, ensure you have:

- **Python 3.8+** installed
- **API Keys** (free):
  - [OpenWeatherMap API Key](https://openweathermap.org/api)
  - [NewsAPI Key](https://newsapi.org/)
- An **MCP-compatible client** such as:
  - Claude Desktop
  - Continue (VS Code extension)
  - Cline
  - Or any other MCP client

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ZiliOussema/mcp_weather_and_news_assistant.git
cd mcp_weather_and_news_assistant
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# .env
OPENWEATHER_API_KEY=your_openweather_api_key_here
NEWS_API_KEY=your_newsapi_key_here
```

**IMPORTANT:** Never commit your `.env` file to version control!

---

## Finding Your Project Path

Before configuring any MCP client, you need to know your project's full path.

### Windows

Open Command Prompt in your project folder and run:

```cmd
cd
```

This will display your current directory path, for example:
```
C:\Users\YourName\Projects\mcp_weather_and_news_assistant
```

Or use PowerShell:
```powershell
pwd
```

### macOS/Linux

Open Terminal in your project folder and run:

```bash
pwd
```

This will display your current directory path, for example:
```
/Users/yourname/projects/mcp_weather_and_news_assistant
```

**Tip:** You can also drag and drop the project folder into Terminal/Command Prompt to see its full path.

---

## Deployment

### 1. Claude Desktop

#### Windows

**Step 1:** Locate the Claude Desktop configuration file

Path: `%APPDATA%\Claude\claude_desktop_config.json`

Or navigate to: `C:\Users\YOUR_USERNAME\AppData\Roaming\Claude\claude_desktop_config.json`

**Step 2:** Open `claude_desktop_config.json` and add your MCP server:

```json
{
  "mcpServers": {
    "weather-news": {
      "command": "C:\\path\\to\\your\\project\\mcp_weather_and_news_assistant\\venv\\Scripts\\python.exe",
      "args": [
        "C:\\path\\to\\your\\project\\mcp_weather_and_news_assistant\\server.py"
      ]
    }
  }
}
```

**Important Notes:**
- Replace `C:\\path\\to\\your\\project\\` with your actual project path
- Use double backslashes (`\\`) in Windows paths
- Paths must be absolute (full path from C:\)
- Make sure the paths are correct

**Step 3:** Verify the paths exist

Open Command Prompt and run:

```cmd
"C:\path\to\your\project\mcp_weather_and_news_assistant\venv\Scripts\python.exe" --version
```

Replace with your actual path. You should see the Python version number (e.g., `Python 3.11.0`).

**Step 4:** Restart Claude Desktop

- **Completely close** Claude Desktop (not just minimize)
- Check Task Manager to ensure no Claude processes are running
- Reopen Claude Desktop

**Step 5:** Verify the server is loaded

- Look for a plug icon or "MCP" section in Claude Desktop
- You should see `weather` and `news` tools available
- Try asking: "What's the weather in Paris?"

---

#### macOS

**Step 1:** Locate the configuration file

```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Step 2:** Edit the configuration using Terminal:

```bash
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Add:

```json
{
  "mcpServers": {
    "weather-news": {
      "command": "/Users/YOUR_USERNAME/mcp_weather_and_news_assistant/venv/bin/python",
      "args": [
        "/Users/YOUR_USERNAME/mcp_weather_and_news_assistant/server.py"
      ]
    }
  }
}
```

**Step 3:** Verify Python path

```bash
which python
# Or for virtual environment:
/Users/YOUR_USERNAME/mcp_weather_and_news_assistant/venv/bin/python --version
```

**Step 4:** Restart Claude Desktop

```bash
killall Claude
# Then reopen Claude Desktop from Applications
```

---

#### Linux

**Step 1:** Configuration location

```bash
~/.config/Claude/claude_desktop_config.json
```

**Step 2:** Edit configuration:

```bash
nano ~/.config/Claude/claude_desktop_config.json
```

Add:

```json
{
  "mcpServers": {
    "weather-news": {
      "command": "/home/YOUR_USERNAME/mcp_weather_and_news_assistant/venv/bin/python",
      "args": [
        "/home/YOUR_USERNAME/mcp_weather_and_news_assistant/server.py"
      ]
    }
  }
}
```

**Step 3:** Restart Claude Desktop

```bash
pkill claude
# Then restart from your application menu
```

---

### 2. Continue (VS Code)

[Continue](https://continue.dev/) is a popular VS Code extension that supports MCP servers.

**Step 1:** Install Continue extension

1. Open VS Code
2. Go to Extensions (`Ctrl+Shift+X`)
3. Search for "Continue"
4. Click Install

**Step 2:** Open Continue configuration

- Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
- Type: `Continue: Open config.json`
- Press Enter

**Step 3:** Add MCP server to Continue config

**For Windows:**

```json
{
  "models": [
    {
      "title": "Claude 3.5 Sonnet",
      "provider": "anthropic",
      "model": "claude-3-5-sonnet-20241022",
      "apiKey": "YOUR_ANTHROPIC_API_KEY"
    }
  ],
  "mcpServers": [
    {
      "name": "weather-news",
      "command": "C:\\path\\to\\your\\project\\mcp_weather_and_news_assistant\\venv\\Scripts\\python.exe",
      "args": [
        "C:\\path\\to\\your\\project\\mcp_weather_and_news_assistant\\server.py"
      ]
    }
  ]
}
```

Replace `C:\\path\\to\\your\\project\\` with your actual project location.

**For macOS/Linux:**

```json
{
  "models": [...],
  "mcpServers": [
    {
      "name": "weather-news",
      "command": "/Users/YOUR_USERNAME/mcp_weather_and_news_assistant/venv/bin/python",
      "args": [
        "/Users/YOUR_USERNAME/mcp_weather_and_news_assistant/server.py"
      ]
    }
  ]
}
```

**Step 4:** Reload VS Code

- Press `Ctrl+Shift+P` / `Cmd+Shift+P`
- Type: `Developer: Reload Window`
- Press Enter

**Step 5:** Test in Continue

Open Continue sidebar and ask:
```
What's the weather in New York?
```

You should see Continue using the `weather` tool.

---

### 3. Cline

[Cline](https://github.com/cline/cline) is an autonomous coding agent for VS Code with MCP support.

**Step 1:** Install Cline

1. Open VS Code
2. Go to Extensions (`Ctrl+Shift+X`)
3. Search for "Cline"
4. Click Install

**Step 2:** Configure Cline MCP settings

- Click the Cline icon in VS Code sidebar
- Go to Cline Settings (gear icon)
- Find "MCP Servers" section

**Step 3:** Add configuration

**Method A: Using Settings UI**

1. Click "Add MCP Server"
2. Fill in:
   - Name: `weather-news`
   - Command: Path to your Python executable (e.g., `C:\path\to\project\venv\Scripts\python.exe`)
   - Args: Path to your server.py (e.g., `C:\path\to\project\server.py`)

Replace the paths with your actual project location.

**Method B: Edit settings.json**

Open Command Palette and type: `Preferences: Open User Settings (JSON)`

Add:

```json
{
  "cline.mcpServers": [
    {
      "name": "weather-news",
      "command": "C:\\path\\to\\your\\project\\mcp_weather_and_news_assistant\\venv\\Scripts\\python.exe",
      "args": [
        "C:\\path\\to\\your\\project\\mcp_weather_and_news_assistant\\server.py"
      ]
    }
  ]
}
```

Replace with your actual project paths.

**Step 4:** Restart Cline

- Close and reopen Cline panel
- Or reload VS Code window

**Step 5:** Test with Cline

Ask Cline to:
```
Check the weather in London and get tech news
```

---

#### Cursor IDE

**Configuration location:** Settings → MCP Servers

Or edit `~/.cursor/config.json`:

```json
{
  "mcpServers": {
    "weather-news": {
      "command": "/path/to/python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

---

#### Generic MCP Client Configuration

For any MCP-compatible client, use this template:

```json
{
  "mcpServers": {
    "weather-news": {
      "command": "<PYTHON_EXECUTABLE_PATH>",
      "args": ["<SERVER_SCRIPT_PATH>"],
      "env": {
        "OPENWEATHER_API_KEY": "your_key",
        "NEWS_API_KEY": "your_key"
      }
    }
  }
}
```

**Finding your Python path:**

```bash
# Windows
where python

# macOS/Linux
which python
# Or for venv:
which python3
```

---

## Usage Examples

Once deployed, you can interact with the tools through natural language:

### Weather Queries

```
User: What's the weather like in Tokyo?
```

The AI will call the `weather` tool with `city="Tokyo"` and respond:

```
The current weather in Tokyo is 18°C with clear skies. 
Humidity is at 65% with a light breeze of 5 m/s.
```

---

### News Queries

```
User: Show me the latest technology news
```

The AI calls the `news` tool with `topic="technology"`:

```
Here are the top 5 tech headlines:
1. New AI breakthrough announced by researchers
   Source: TechCrunch | Published: 2026-02-03
2. Tech company releases innovative product
   Source: The Verge | Published: 2026-02-03
3. Cybersecurity concerns rise globally
   Source: Wired | Published: 2026-02-02
...
```

**Note:** The news tool searches for articles by topic, not by category or country.

---

### Combined Queries

```
User: What's the weather in London and any technology news?
```

The AI intelligently calls both tools:

```
Weather in London: 12°C, cloudy with light rain
Humidity: 80%, Wind: 4.2 m/s

Top Technology News:
1. [Tech Headline 1] - Source: TechCrunch
2. [Tech Headline 2] - Source: The Verge
...
```

---

## Troubleshooting

### Issue: Server Not Loading in Claude Desktop

**Symptoms:**
- MCP tools don't appear in Claude Desktop
- No plug icon visible

**Solutions:**

1. **Check configuration file location**
   ```bash
   # Windows
   echo %APPDATA%\Claude\claude_desktop_config.json
   
   # macOS
   echo ~/Library/Application\ Support/Claude/claude_desktop_config.json
   
   # Linux
   echo ~/.config/Claude/claude_desktop_config.json
   ```

2. **Verify JSON syntax**
   - Copy your config to [jsonlint.com](https://jsonlint.com/)
   - Fix any syntax errors (missing commas, quotes, etc.)

3. **Check Python path**
   ```bash
   # Test if Python executable exists (Windows example)
   "C:\path\to\your\project\mcp_weather_and_news_assistant\venv\Scripts\python.exe" --version
   
   # macOS/Linux
   /path/to/your/project/mcp_weather_and_news_assistant/venv/bin/python --version
   ```

4. **Check server.py path**
   ```bash
   # Windows - Verify file exists
   dir "C:\path\to\your\project\mcp_weather_and_news_assistant\server.py"
   
   # macOS/Linux
   ls -l /path/to/your/project/mcp_weather_and_news_assistant/server.py
   ```

5. **View Claude logs**
   - **Windows:** `%APPDATA%\Claude\logs\`
   - **macOS:** `~/Library/Logs/Claude/`
   - **Linux:** `~/.local/state/Claude/logs/`
   
   Look for error messages related to MCP servers.

---

### Issue: "Module not found" Error

**Symptoms:**
- Server starts but crashes immediately
- Logs show `ModuleNotFoundError`

**Solutions:**

1. **Activate virtual environment and reinstall**
   ```bash
   # Windows
   venv\Scripts\activate
   pip install -r requirements.txt
   
   # macOS/Linux
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Verify packages are installed**
   ```bash
   pip list
   # Should show: mcp, requests, python-dotenv
   ```

3. **Check you're using venv Python, not system Python**

---

### Issue: API Errors (401, 403, 404)

**Symptoms:**
- Tools execute but return error messages
- "Invalid API key" or "Unauthorized"

**Solutions:**

1. **Verify API keys in `.env` file**
   ```bash
   # Check .env exists
   cat .env
   
   # Or on Windows
   type .env
   ```

2. **Test API keys manually**
   ```bash
   # Test OpenWeatherMap
   curl "https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=YOUR_KEY&units=metric"
   
   # Test NewsAPI
   curl "https://newsapi.org/v2/everything?q=technology&apiKey=YOUR_KEY&pageSize=5"
   ```

3. **Check API key limits**
   - Free tier APIs have request limits
   - OpenWeatherMap: 60 calls/minute
   - NewsAPI: 100 requests/day (free tier)

---

### Issue: Tools Not Appearing in Continue/Cline

**Solutions:**

1. **Completely reload VS Code**
   - `Ctrl+Shift+P` → "Developer: Reload Window"

2. **Check Continue/Cline logs**
   - Open VS Code Output panel
   - Select "Continue" or "Cline" from dropdown
   - Look for MCP initialization errors

3. **Test server manually**
   ```bash
   python server.py
   # Should start without errors
   ```

4. **Verify MCP server section exists in config**
   - Continue: Look for `"mcpServers": [...]` array
   - Cline: Check settings have MCP configuration

---

### Issue: "Permission Denied" on macOS/Linux

**Solutions:**

1. **Make server.py executable**
   ```bash
   chmod +x server.py
   ```

2. **Check file ownership**
   ```bash
   ls -la server.py
   # Should be owned by your user
   ```

3. **Fix permissions**
   ```bash
   sudo chown $USER:$USER server.py
   ```

---

### General Debugging Tips

1. **Test server standalone**
   ```bash
   cd mcp_weather_and_news_assistant
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   python server.py
   ```
   
   Server should start and display: "Starting Weather and News Assistant MCP server..."

2. **Check server logs**
   
   The server already includes logging at INFO level. Check the console output when running the server for any error messages.

3. **Check network connectivity**
   ```bash
   # Test if you can reach APIs
   ping api.openweathermap.org
   ping newsapi.org
   ```

4. **Try minimal configuration**
   
   Start with just one MCP server to isolate issues.

---

## Project Structure

```
mcp_weather_and_news_assistant/
├── tools/
│   ├── __init__.py
│   ├── weather.py             # Weather tool implementation (get_weather function)
│   └── news.py                # News tool implementation (get_news function)
├── server.py                  # Main MCP server entry point using FastMCP
├── venv/                      # Virtual environment (not in repo)
│   ├── Scripts/               # Windows executables
│   └── bin/                   # Unix executables
├── .env                       # Environment variables (not in repo)
├── .gitignore                 # Git ignore file
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── LICENSE                    # Project license (optional)
```

---

## Testing the Server

### Manual Testing

```bash
# Activate environment
source venv/bin/activate  # or venv\Scripts\activate

# Run server
python server.py

# Server should display: "Starting Weather and News Assistant MCP server..."
```

### Using MCP Inspector (Optional)

```bash
npx @modelcontextprotocol/inspector python server.py
```

### Unit Tests (Optional)

Create `tests/test_tools.py`:

```python
import pytest
from tools.weather import get_weather
from tools.news import get_news

def test_weather():
    result = get_weather("Paris")
    assert "temperature" in result
    assert "humidity" in result
    assert "wind_speed" in result
    assert "description" in result

def test_news():
    result = get_news("technology")
    assert "topic" in result
    assert "results" in result
    assert len(result["results"]) > 0
```

Run tests:

```bash
pytest tests/
```

---

## Security Best Practices

1. **Never commit API keys**
   - Always use `.env` file
   - Add `.env` to `.gitignore`

2. **Use environment variables**
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   API_KEY = os.getenv("OPENWEATHER_API_KEY")
   ```

3. **Rotate keys regularly**
   - Generate new API keys periodically
   - Revoke old keys

4. **Limit API access**
   - Use read-only keys when possible
   - Set rate limits

---

## Advanced Configuration

### Environment Variables in MCP Config

Some clients support passing environment variables directly:

```json
{
  "mcpServers": {
    "weather-news": {
      "command": "/path/to/python",
      "args": ["/path/to/server.py"],
      "env": {
        "OPENWEATHER_API_KEY": "${OPENWEATHER_API_KEY}",
        "NEWS_API_KEY": "${NEWS_API_KEY}"
      }
    }
  }
}
```

This references system environment variables.

---

### Multiple MCP Servers

You can run multiple MCP servers simultaneously:

```json
{
  "mcpServers": {
    "weather-news": {
      "command": "/path/to/weather_news/venv/bin/python",
      "args": ["/path/to/weather_news/server.py"]
    },
    "database-tools": {
      "command": "/path/to/db_tools/venv/bin/python",
      "args": ["/path/to/db_tools/server.py"]
    },
    "file-manager": {
      "command": "/path/to/file_mgr/venv/bin/python",
      "args": ["/path/to/file_mgr/server.py"]
    }
  }
}
```

Replace each path with your actual project locations.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Changelog

### v0.0.1 (Initial Release)
- Weather tool implementation
- News tool implementation
- MCP server setup
- Documentation for multiple clients

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Resources

### MCP Documentation
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

### API Documentation
- [OpenWeatherMap API](https://openweathermap.org/api)
- [NewsAPI Documentation](https://newsapi.org/docs)

### MCP Clients
- [Claude Desktop](https://claude.ai/desktop)
- [Continue Extension](https://continue.dev/)
- [Cline](https://github.com/cline/cline)
- [Zed Editor](https://zed.dev/)
- [Cursor IDE](https://cursor.sh/)

### Related Projects
- [Awesome MCP Servers](https://github.com/modelcontextprotocol/awesome-mcp-servers)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

---

## Contact

For questions or support:
- Open an issue on [GitHub](https://github.com/ZiliOussema/mcp_weather_and_news_assistant)
- Check the [MCP Documentation](https://modelcontextprotocol.io/)

---


## Roadmap

Future enhancements:

- [ ] Implement news search functionality
- [ ] Add caching for API responses
- [ ] Create Docker container for easy deployment
- [ ] Add support for multiple languages
- [ ] Implement rate limiting
- [ ] Add unit tests
- [ ] Create web dashboard for monitoring

---

**MCP Weather & News Assistant** - A portfolio project demonstrating Model Context Protocol integration

