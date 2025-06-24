# Netbian Wallpaper Crawler

This project is a Python crawler script for downloading anime wallpapers from "Netbian" (彼岸网). Users can specify the number of pages and page numbers to crawl. The script automatically downloads wallpapers to the `wallpapers` folder and saves wallpaper information to `wallpapers_ifmt.csv`.

## Features

- Customizable number of pages and page numbers to crawl
- Automatically downloads wallpapers as JPG files
- Saves wallpaper info (link and name) to a CSV file
- Automatically creates the image folder if it doesn't exist
- Uses anti-crawling headers (User-Agent and Cookie)

## Requirements

- Python 3.x
- requests
- beautifulsoup4

### Install dependencies

```bash
pip install requests beautifulsoup4
```

## Usage

1. Run the script:

   ```bash
   python wallpaper_get.py
   ```

2. Follow the prompts to enter the number of pages you want to crawl (e.g., 3), then enter each page number (e.g., 2, 3, 4), pressing Enter after each.

3. The script will download wallpapers to the `wallpapers` folder and generate `wallpapers_ifmt.csv` in the current directory.

## Files

- `wallpaper_get.py`: Main crawler script
- `wallpapers/`: Folder for downloaded wallpapers
- `wallpapers_ifmt.csv`: CSV file with wallpaper links and names

## Notes

- For learning and communication purposes only. Do not use for commercial purposes.
- Netbian has anti-crawling mechanisms. The script sets User-Agent and Cookie. If access is restricted, try updating the Cookie.
- To avoid overloading the website, you can increase the `time.sleep()` interval.
- Ensure you have network access and write permissions in the current directory.

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

## 环境依赖

- Python 3.x
- requests
- beautifulsoup4

### 安装依赖

```bash
pip install requests beautifulsoup4
```

## 使用方法

1. 运行脚本：

   ```bash
   python wallpaper_get.py
   ```

2. 按提示输入你想爬取的页数（如 3），然后依次输入每一页的页码（如 2、3、4），每输入一个页码按回车。

3. 程序会自动爬取对应页码的壁纸，下载到 `wallpapers` 文件夹，并在当前目录生成 `wallpapers_ifmt.csv` 文件。

## 文件说明

- `wallpaper_get.py`：主爬虫脚本
- `wallpapers/`：下载的壁纸图片存放目录
- `wallpapers_ifmt.csv`：保存壁纸链接和名称的 CSV 文件

## 注意事项

- 本脚本仅供学习和交流使用，请勿用于商业用途。
- 彼岸网有反爬虫机制，脚本已设置 User-Agent 和 Cookie，如遇到访问受限可尝试更换 Cookie。
- 下载速度较快时建议适当增加 `time.sleep()` 的时间，避免对目标网站造成压力。
- 运行前请确保有网络连接，并有写入当前目录的权限。

## 免责声明

本项目仅用于学习和技术交流，下载的图片版权归原网站及作者所有，请勿用于商业用途。

