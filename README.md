# MCP Weather & News Assistant

An AI assistant project built with the **Model Context Protocol (MCP)** that connects an LLM to real-world data sources via custom MCP tools.  
It provides **real-time weather information** and **latest news headlines** by allowing the model to call external APIs through an MCP server.

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

Or use PowerShell:
```powershell
pwd
```

### macOS/Linux

Open Terminal in your project folder and run:

```bash
pwd
```

---

## Deployment

### 1. Claude Desktop

#### Windows

**Step 1:** Locate the Claude Desktop configuration file

Path: `%APPDATA%\Claude\claude_desktop_config.json`

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

**Step 3:** Verify the paths exist

```cmd
"C:\path\to\your\project\mcp_weather_and_news_assistant\venv\Scripts\python.exe" --version
```

**Step 4:** Restart Claude Desktop

- Completely close Claude Desktop
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

**Step 2:** Edit the configuration:

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

**Step 3:** Restart Claude Desktop

```bash
killall Claude
```

Then reopen Claude Desktop from Applications.

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
```

---

### 2. Continue (VS Code)

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

```yaml
mcpServers:
  weather-news:
    command: C:\path\to\your\project\mcp_weather_and_news_assistant\venv\Scripts\python.exe
    args:
      - C:\path\to\your\project\mcp_weather_and_news_assistant\server.py
```

**For macOS/Linux:**

```yaml
mcpServers:
  weather-news:
    command: /Users/YOUR_USERNAME/mcp_weather_and_news_assistant/venv/bin/python
    args:
      - /Users/YOUR_USERNAME/mcp_weather_and_news_assistant/server.py
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

---

### 3. Cline

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

Click "Add MCP Server" and fill in:
- Name: `weather-news`
- Command: Path to your Python executable
- Args: Path to your server.py

Or edit settings.json:

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

**Step 4:** Restart Cline or reload VS Code

---

## Usage Examples

### Weather Queries

```
User: What's the weather like in Tokyo?
```

Response:
```
The current weather in Tokyo is 18°C with clear skies. 
Humidity is at 65% with a light breeze of 5 m/s.
```

### News Queries

```
User: Show me the latest technology news
```

Response:
```
Here are the top 5 tech headlines:
1. New AI breakthrough announced by researchers
   Source: TechCrunch | Published: 2026-02-03
2. Tech company releases innovative product
   Source: The Verge | Published: 2026-02-03
...
```

### Combined Queries

```
User: What's the weather in London and any technology news?
```

---

## Troubleshooting

### Server Not Loading in Claude Desktop

1. **Check configuration file location**
   ```bash
   # Windows
   echo %APPDATA%\Claude\claude_desktop_config.json
   
   # macOS
   echo ~/Library/Application\ Support/Claude/claude_desktop_config.json
   
   # Linux
   echo ~/.config/Claude/claude_desktop_config.json
   ```

2. **Verify JSON syntax** at [jsonlint.com](https://jsonlint.com/)

3. **Check Python path**
   ```bash
   # Windows
   "C:\path\to\your\project\mcp_weather_and_news_assistant\venv\Scripts\python.exe" --version
   
   # macOS/Linux
   /path/to/your/project/mcp_weather_and_news_assistant/venv/bin/python --version
   ```

4. **View Claude logs**
   - **Windows:** `%APPDATA%\Claude\logs\`
   - **macOS:** `~/Library/Logs/Claude/`
   - **Linux:** `~/.local/state/Claude/logs/`

---

### "Module not found" Error

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
   ```

---

### API Errors (401, 403, 404)

1. **Verify API keys in `.env` file**
   ```bash
   cat .env
   ```

2. **Test API keys manually**
   ```bash
   # Test OpenWeatherMap
   curl "https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=YOUR_KEY&units=metric"
   
   # Test NewsAPI
   curl "https://newsapi.org/v2/everything?q=technology&apiKey=YOUR_KEY&pageSize=5"
   ```

3. **Check API key limits**
   - OpenWeatherMap: 60 calls/minute
   - NewsAPI: 100 requests/day (free tier)

---

### Tools Not Appearing in Continue/Cline

1. **Reload VS Code**: `Ctrl+Shift+P` → "Developer: Reload Window"

2. **Check logs** in VS Code Output panel

3. **Test server manually**
   ```bash
   python server.py
   ```

---

### "Permission Denied" on macOS/Linux

```bash
chmod +x server.py
```

---

## Project Structure

```
mcp_weather_and_news_assistant/
├── tools/
│   ├── __init__.py
│   ├── weather.py             # Weather tool implementation
│   └── news.py                # News tool implementation
├── server.py                  # Main MCP server entry point
├── venv/                      # Virtual environment 
├── .env                       # Environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Testing the Server

```bash
# Activate environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run server
python server.py
```

---

## Security Best Practices

1. **Never commit API keys** - Always use `.env` file
2. **Add `.env` to `.gitignore`**
3. **Rotate keys regularly**
4. **Use read-only keys when possible**

---

**MCP Weather & News Assistant** - A portfolio project demonstrating Model Context Protocol integration