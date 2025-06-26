# Netbian Wallpaper Crawler

This project is a Python crawler script for downloading anime wallpapers from "Netbian" (彼岸网). Users can specify the number of pages and page numbers to crawl. The script automatically downloads wallpapers to the `wallpapers` folder and saves wallpaper information to `wallpapers_ifmt.csv`.

## Features

- Customizable number of pages and page numbers to crawl
- Automatically downloads wallpapers as JPG files
- Saves wallpaper info (link and name) to a CSV file
- Automatically creates the image folder if it doesn't exist
- Uses anti-crawling headers (User-Agent and Cookie)
- **NEW**: Configuration file support for easy customization
- **NEW**: Proxy support for enhanced privacy
- **NEW**: Flexible category selection

## Requirements

- Python 3.x
- requests
- beautifulsoup4

### Install dependencies

```bash
pip install requests beautifulsoup4
```

## Quick Start

1. **Configure the script** (see Configuration section below)
2. **Run the script**:

   ```bash
   python wallpaper_get.py
   ```

3. **Follow the prompts** to enter the number of pages you want to crawl (e.g., 3), then enter each page number (e.g., 2, 3, 4), pressing Enter after each.

4. **Check results**: The script will download wallpapers to the `wallpapers` folder and generate `wallpapers_ifmt.csv` in the current directory.

## Configuration

The script uses `config.json` for all configuration settings. This makes it easy to customize without modifying the code.

### Configuration File Structure

```json
{
    "headers": {
        "User-Agent": "浏览器User-Agent字符串",
        "Cookie": "网站Cookie信息"
    },
    "settings": {
        "base_url": "网站基础URL",
        "category": "爬取分类",
        "download_delay": 下载延迟时间（秒）,
        "output_dir": "壁纸保存目录",
        "csv_file": "信息保存的CSV文件名"
    },
    "proxies": {
        "enabled": false,
        "http": "HTTP代理地址",
        "https": "HTTPS代理地址"
    }
}
```

### Configuration Options

#### 1. Headers Configuration
- **User-Agent**: Browser identifier to avoid being detected as a crawler
- **Cookie**: Website authentication information including login status

#### 2. Settings Configuration
- **base_url**: Base URL of the website (e.g., "http://www.netbian.com")
- **category**: Category to crawl (e.g., "dongman", "fengjing", "meinv", etc.)
- **download_delay**: Delay between downloads in seconds
- **output_dir**: Directory to save wallpaper images
- **csv_file**: CSV filename to save wallpaper information

#### 3. Proxies Configuration
- **enabled**: Whether to enable proxy (true/false)
- **http**: HTTP proxy server address and port
- **https**: HTTPS proxy server address and port

### How to Update Configuration

#### Update User-Agent
1. Open browser developer tools (F12)
2. Find any request in the Network tab
3. Copy the User-Agent value from the request headers
4. Update the User-Agent field in the configuration file

#### Update Cookie
1. Log in to the target website in your browser
2. Open developer tools (F12)
3. Find Cookies in the Application/Storage tab
4. Copy all Cookie values
5. Update the Cookie field in the configuration file

#### Enable Proxy
1. Set `proxies.enabled` to `true`
2. Update `proxies.http` and `proxies.https` with your proxy server addresses

#### Change Category
Modify the `category` field in the configuration file. Common categories include:
- `dongman` (动漫/Anime)
- `fengjing` (风景/Landscape)
- `meinv` (美女/Beauty)
- `youxi` (游戏/Games)
- `dongwu` (动物/Animals)
- `jianzhu` (建筑/Architecture)
- `meishi` (美食/Food)
- `zongjiao` (宗教/Religion)
- `beijing` (背景/Background)

## Files

- `wallpaper_get.py`: Main crawler script
- `config.json`: Configuration file
- `wallpapers/`: Folder for downloaded wallpapers
- `wallpapers_ifmt.csv`: CSV file with wallpaper links and names
- `start.bat`: Windows batch file for easy execution

## Important Notes

### Cookie Management
- Cookies have expiration times and need to be updated periodically
- If access is restricted, try updating the Cookie in the configuration file

### User-Agent
- Use real browser User-Agent strings to avoid being detected as a crawler
- Avoid using obvious crawler identifiers

### Download Speed
- Set appropriate delay times to avoid overwhelming the target website
- Increase `download_delay` for safer crawling, decrease for faster downloads

### Proxy Usage
- Ensure proxy servers are stable and reliable when using them
- Test proxy connectivity before running the crawler

## Troubleshooting

**Q: How to get the latest Cookie?**
A: Re-login to the website in your browser, then copy the latest Cookie value from developer tools.

**Q: How to change the crawling category?**
A: Modify the `category` field in the configuration file. See the category list above.

**Q: How to adjust download speed?**
A: Modify the `download_delay` value. Higher values = slower but safer, lower values = faster but riskier.

**Q: Configuration file not found error?**
A: Make sure `config.json` exists in the same directory as `wallpaper_get.py`.

**Q: After starting the script and entering the number of pages, the program closes with an error?**
A: Make sure the `config.json` is filled in correctly.

## Disclaimer

This project is for learning and technical exchange only. All images belong to their original website and authors. Do not use for commercial purposes.

---

# 彼岸壁纸爬虫

本项目是一个用于爬取「彼岸网」动漫壁纸的 Python 爬虫脚本。用户可自定义爬取的页数和页码，自动下载壁纸图片到 `wallpapers` 文件夹，并将壁纸信息保存到 `wallpapers_ifmt.csv` 文件中。

## 功能简介

- 支持自定义输入要爬取的页数和具体页码
- 自动下载壁纸图片为 JPG 文件
- 壁纸信息（链接和名称）保存为 CSV 文件
- 自动创建保存图片的文件夹
- 设置反爬虫 User-Agent 和 Cookie
- **新增**: 配置文件支持，便于自定义设置
- **新增**: 代理支持，增强隐私保护
- **新增**: 灵活的分类选择

## 环境依赖

- Python 3.x
- requests
- beautifulsoup4

### 安装依赖

```bash
pip install requests beautifulsoup4
```

## 快速开始

1. **配置脚本**（见下方配置说明）
2. **运行脚本**：

   ```bash
   python wallpaper_get.py
   ```

3. **按提示操作**：输入你想爬取的页数（如 3），然后依次输入每一页的页码（如 2、3、4），每输入一个页码按回车

4. **查看结果**：程序会自动爬取对应页码的壁纸，下载到 `wallpapers` 文件夹，并在当前目录生成 `wallpapers_ifmt.csv` 文件

## 配置说明

脚本使用 `config.json` 进行所有配置设置，无需修改代码即可轻松自定义

### 配置文件结构

```json
{
    "headers": {
        "User-Agent": "浏览器User-Agent字符串",
        "Cookie": "网站Cookie信息"
    },
    "settings": {
        "base_url": "网站基础URL",
        "category": "爬取分类",
        "download_delay": 下载延迟时间（秒）,
        "output_dir": "壁纸保存目录",
        "csv_file": "信息保存的CSV文件名"
    },
    "proxies": {
        "enabled": false,
        "http": "HTTP代理地址",
        "https": "HTTPS代理地址"
    }
}
```

### 配置选项说明

#### 1. headers 配置
- **User-Agent**: 模拟浏览器的标识，用于避免被网站识别为爬虫
- **Cookie**: 网站的认证信息，包含登录状态等

#### 2. settings 配置
- **base_url**: 网站的基础URL，如 "http://www.netbian.com"
- **category**: 要爬取的分类，如 "dongman"（动漫）、"fengjing"（风景）等
- **download_delay**: 每次下载之间的延迟时间，避免请求过于频繁
- **output_dir**: 壁纸图片保存的目录名
- **csv_file**: 保存壁纸信息的CSV文件名

#### 3. proxies 配置
- **enabled**: 是否启用代理，true为启用，false为禁用
- **http**: HTTP代理服务器地址和端口
- **https**: HTTPS代理服务器地址和端口

### 如何更新配置

#### 更新User-Agent
1. 打开浏览器开发者工具（F12）
2. 在Network标签页中找到任意请求
3. 复制请求头中的User-Agent值
4. 更新配置文件中的User-Agent字段

#### 更新Cookie
1. 在浏览器中登录目标网站
2. 打开开发者工具（F12）
3. 在Application/Storage标签页中找到Cookies
4. 复制所有Cookie值
5. 更新配置文件中的Cookie字段

#### 启用代理
1. 将 `proxies.enabled` 设置为 `true`
2. 更新 `proxies.http` 和 `proxies.https` 为你的代理服务器地址

#### 更换爬取分类
修改配置文件中的 `category` 字段，常见分类包括：
- dongman（动漫）
- fengjing（风景）
- meinv（美女）
- youxi（游戏）
- dongwu（动物）
- jianzhu（建筑）
- meishi（美食）
- zongjiao（宗教）
- beijing（背景）

## 文件说明

- `wallpaper_get.py`：主爬虫脚本
- `config.json`：配置文件
- `wallpapers/`：下载的壁纸图片存放目录
- `wallpapers_ifmt.csv`：保存壁纸链接和名称的 CSV 文件
- `start.bat`：Windows 批处理文件，便于执行

## 注意事项

### Cookie管理
- Cookie通常有时效性，过期后需要重新获取
- 如遇到访问受限，可尝试更新配置文件中的Cookie

### User-Agent
- 建议使用真实的浏览器User-Agent，避免使用明显的爬虫标识
- 避免使用明显的爬虫标识

### 下载速度
- 建议设置适当的延迟时间，避免对目标网站造成过大压力
- 增大 `download_delay` 值下载更慢但更安全，减小值下载更快但可能被限制

### 代理使用
- 使用代理时请确保代理服务器稳定可靠
- 运行爬虫前请测试代理连接性

## 常见问题

**Q: 如何获取最新的Cookie？**
A: 在浏览器中重新登录网站，然后从开发者工具中复制最新的Cookie值

**Q: 如何更换爬取分类？**
A: 修改配置文件中的 `category` 字段，常见分类见上方列表

**Q: 如何调整下载速度？**
A: 修改 `download_delay` 的值，数值越大下载越慢但越安全，数值越小下载越快但可能被限制

**Q: 配置文件不存在错误？**
A: 确保 `config.json` 文件存在于 `wallpaper_get.py` 同一目录下

**Q: 启动脚本输入页数后程序报错关闭？**
A: 确保 `config.json` 已正确填写

## 免责声明

本项目仅用于学习和技术交流，下载的图片版权归原网站及作者所有，请勿用于商业用途

