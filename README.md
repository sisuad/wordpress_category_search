# WordPress Category Search Tool / WordPress分类搜索工具

## English

This tool helps extract WordPress category IDs when you have admin access but no server/database access.

### Features
- Extract category IDs from WordPress admin HTML
- Save category data in JSON format (`category_id.json`)
- Parse raw HTML from WordPress admin interface

### Usage
1. Get `raw_category.html`:
   - Login to WordPress admin
   - Go to [Posts] > [Categories] 
   - Click [Screen Options] > set [Pagination] to max value
   - Open browser DevTools (F12) > Network tab
   - Find `edit-tags.php?taxonomy=category` request
   - In Response, copy `<div class="form-field term-parent-wrap">` section to `raw_category.html`
2. Run `python get_category_ids.py` to extract IDs
3. Results will be saved in `category_id.json`

### Files & Dependencies
- `get_category_ids.py`: Main script to extract category data (requires BeautifulSoup4)
- `config.json`: Configuration file (contains JWT Token for authentication)
- `category_id.json`: Output file with category IDs
- `raw_category.html`: Raw HTML output of category pages

### Requirements
- Python 3.x
- Install dependencies: `pip install -r requirements.txt`

## 中文

本工具适用于有WordPress后台权限但无服务器/数据库权限时提取分类ID。

### 功能
- 从WordPress后台HTML提取分类ID
- 将分类数据保存为JSON格式(`category_id.json`)
- 解析WordPress后台接口的原始HTML

### 使用方法
1. 获取`raw_category.html`:
   - 登录WordPress后台
   - 进入【文章】>【分类目录】
   - 点击【显示选项】>设置【分页】为最大值
   - 打开浏览器开发者工具(F12)>网络标签
   - 找到`edit-tags.php?taxonomy=category`接口请求
   - 在响应中复制`<div class="form-field term-parent-wrap">`部分到`raw_category.html`
2. 运行`python get_category_ids.py`提取分类ID
3. 结果将保存在`category_id.json`中

### 文件说明与依赖
- `get_category_ids.py`: 提取分类数据的主脚本(需要BeautifulSoup4)
- `config.json`: 配置文件(包含用于鉴权的JWT Token)
- `category_id.json`: 包含分类ID的输出文件
- `raw_category.html`: 分类页面的原始HTML

### 环境要求
- Python 3.x
- 安装依赖: `pip install -r requirements.txt`
