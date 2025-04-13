from bs4 import BeautifulSoup
import json

def parse_categories(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    categories = []
    for option in soup.find_all('option'):
        if option['value'] == '-1':
            continue
            
        category = {
            "category": option.text.strip(),
            "id": option['value'],
            "class": option['class'][0] if 'class' in option.attrs else ''
        }
        categories.append(category)
    
    return categories

def main():
    input_file = 'raw_category.html'
    output_file = 'category_id.json'
    
    try:
        categories = parse_categories(input_file)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(categories, f, ensure_ascii=False, indent=2)
            
        print(f"成功提取并保存了 {len(categories)} 个分类到 {output_file}")
    except Exception as e:
        print(f"处理过程中发生错误: {str(e)}")

if __name__ == "__main__":
    main()
