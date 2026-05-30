import sys
import os
import urllib.request
import json
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_release.py <version>")
        sys.exit(1)
        
    version = sys.argv[1].strip()
    if not version.startswith('v'):
        version_tag = 'v' + version
    else:
        version_tag = version
        version = version[1:] # strip 'v'
        
    print(f"Updating site to version: {version_tag}")
    
    # 1. Fetch release info from GitHub API
    url = f"https://api.github.com/repos/veg/hyphy/releases/tags/{version_tag}"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    body = ""
    name = f"HyPhy {version_tag}"
    html_url = f"https://github.com/veg/hyphy/releases/tag/{version_tag}"
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            body = data.get('body', '')
            name = data.get('name', f"HyPhy {version_tag}")
            html_url = data.get('html_url', '')
    except Exception as e:
        print(f"Error fetching release notes: {e}")
        body = f"Release notes are available on [GitHub]({html_url})."

    # 2. Update docs/about.md (version string)
    about_path = 'docs/about.md'
    if os.path.exists(about_path):
        with open(about_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace "is currently at version 2.5.X"
        updated_content = re.sub(
            r'is currently at version [\d\w\-\.]+',
            f'is currently at version {version}',
            content
        )
        with open(about_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Updated docs/about.md")

    # 3. Update docs/news.md (prepending release notes)
    news_path = 'docs/news.md'
    if os.path.exists(news_path):
        with open(news_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        latest_release_md = f"""<!-- START_LATEST_RELEASE -->
## <img src="images/logo.png" width="16" height="16" style="vertical-align: middle; margin-right: 6px;" alt="" /> Latest Release: {version_tag} ({name})

{body}

For full details, visit the [GitHub Release Page]({html_url}).

---
<!-- END_LATEST_RELEASE -->"""

        start_marker = "<!-- START_LATEST_RELEASE -->"
        end_marker = "<!-- END_LATEST_RELEASE -->"
        
        if start_marker in content and end_marker in content:
            pattern = re.compile(
                r'<!-- START_LATEST_RELEASE -->.*?<!-- END_LATEST_RELEASE -->',
                re.DOTALL
            )
            updated_content = pattern.sub(latest_release_md, content)
        else:
            # Fallback if markers don't exist
            parts = content.split('\n---\n', 1)
            if len(parts) == 2:
                updated_content = parts[0] + '\n---\n\n' + latest_release_md + '\n\n' + parts[1]
            else:
                updated_content = content + '\n\n' + latest_release_md
                
        with open(news_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Updated docs/news.md")

    # 4. Update docs/assets/version.js
    version_js_path = 'docs/assets/version.js'
    os.makedirs(os.path.dirname(version_js_path), exist_ok=True)
    with open(version_js_path, 'w', encoding='utf-8') as f:
        f.write(f'window.HYPHY_VERSION = "v{version}";\n')
    print("Updated docs/assets/version.js")

if __name__ == '__main__':
    main()
