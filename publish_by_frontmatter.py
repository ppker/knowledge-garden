# publish_by_frontmatter.py
import os
import shutil
import subprocess
from datetime import datetime

# --- 1. 配置区 (请根据您的实际情况修改) ---

# 您的私有仓库（保险库）的绝对路径
VAULT_PATH = os.path.abspath('.') 

# 您的公开仓库（陈列柜）在本地的绝对路径
# !!! 这是一个示例路径，请务必修改为您公开仓库的实际路径 !!!
SHOWCASE_PATH = '/Users/oldwinter/Code/my/knowledge-garden'

# 新增：强制包含的目录列表
# 这些目录下的所有内容都会被直接复制
FORCE_INCLUDE_DIRS = [
    '.obsidian',
    '.cursor'
]

# 新增：强制排除的文件或目录（支持相对路径）
# 这些项目即使在强制包含的目录中，也绝不会被复制
FORCE_EXCLUDE_ITEMS = [
    '.keys.json',
    os.path.join('.obsidian', 'plugins', 'quartz-syncer', 'data.json'),
    os.path.join('.obsidian', 'plugins', 'obsidian-cubox', 'data.json'),
    os.path.join('.obsidian', 'plugins', 'obsidian-image-auto-upload-plugin', 'data.json'), # 也排除这个以防万一
    os.path.join('.obsidian', 'workspace.json'),
    os.path.join('.obsidian', 'workspaces.json'),
]

# 自动生成的 Commit 信息
COMMIT_MESSAGE = f"Garden content update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def should_publish(file_path):
    """
    检查一个 MarkDown 文件是否应该被发布。
    通过读取文件的 frontmatter，寻找 'publish: true'。
    """
    if not file_path.endswith('.md'):
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            in_frontmatter = False
            for line in f:
                line = line.strip()
                if line == '---':
                    if not in_frontmatter:
                        in_frontmatter = True
                        continue
                    else:
                        # 到达 frontmatter 的结尾，还没找到就退出
                        return False
                
                if in_frontmatter:
                    # 简单但高效地检查 'publish: true'
                    if line.lower().replace(' ', '') == 'publish:true':
                        return True
            return False # 文件结束了也没找到
    except Exception:
        # 读取文件失败或编码错误等，则不发布
        return False

def run_command(command, working_dir):
    """在指定目录下执行一个 shell 命令"""
    print(f"Running command: '{' '.join(command)}' in '{working_dir}'")
    try:
        subprocess.run(command, check=True, cwd=working_dir, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {' '.join(command)}")
        print(f"Stderr: {e.stderr}")
        print(f"Stdout: {e.stdout}")
        raise

def main():
    """主执行函数"""
    print("Starting the publishing process based on 'publish: true' flag...")

    # --- 2. 安全检查 ---
    if SHOWCASE_PATH == '/Users/oldwinter/path/to/your/public-garden-repo' or not os.path.exists(SHOWCASE_PATH):
        print("\n" + "="*50)
        print("!!! 安全警告 !!!")
        print(f"请先修改脚本中的 `SHOWCASE_PATH` 变量。")
        print("="*50 + "\n")
        return

    # --- 3. 清理陈列柜 ---
    print(f"\nCleaning showcase directory: {SHOWCASE_PATH}")
    for filename in os.listdir(SHOWCASE_PATH):
        if filename == '.git': continue
        file_path = os.path.join(SHOWCASE_PATH, filename)
        try:
            if os.path.isdir(file_path): shutil.rmtree(file_path)
            else: os.remove(file_path)
        except Exception as e: print(f"Error removing {file_path}: {e}")

    # --- 4. 扫描保险库，决定要发布哪些文件 ---
    print("\nScanning vault to determine files to publish...")
    files_to_copy = set()
    published_md_folders = set()

    # 第一遍：标记 'publish: true' 的 MD 文件和强制包含的目录
    for root, dirs, files in os.walk(VAULT_PATH, topdown=True):
        # 忽略 .git 和 .trash 目录
        dirs[:] = [d for d in dirs if d not in ['.git', '.trash']]
        
        # 检查是否是强制包含的目录
        for force_dir in FORCE_INCLUDE_DIRS:
            if force_dir in dirs:
                dir_path = os.path.join(root, force_dir)
                # 将该目录下的所有文件都加入待复制列表
                for sub_root, _, sub_files in os.walk(dir_path):
                    for name in sub_files:
                        full_path = os.path.join(sub_root, name)
                        relative_path = os.path.relpath(full_path, VAULT_PATH)
                        # 检查是否在强制排除列表中
                        if os.path.basename(name) in FORCE_EXCLUDE_ITEMS or relative_path in FORCE_EXCLUDE_ITEMS:
                            print(f"  - Force excluding sensitive item: {relative_path}")
                            continue
                        files_to_copy.add(full_path)
                print(f"  - Force including directory: {force_dir}")

        for file in files:
            source_path = os.path.join(root, file)
            if should_publish(source_path):
                files_to_copy.add(source_path)
                published_md_folders.add(os.path.dirname(source_path))
                print(f"  - Marked for publish (frontmatter): {os.path.relpath(source_path, VAULT_PATH)}")

    # 第二遍：包含与已发布 MD 文件在同一目录下的其他文件（如 .canvas, 图片）
    for folder in published_md_folders:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path) and not file_path.endswith('.md'):
                if file_path not in files_to_copy:
                    files_to_copy.add(file_path)
                    print(f"  - Including asset: {os.path.relpath(file_path, VAULT_PATH)}")

    # --- 5. 执行复制操作 ---
    print(f"\nCopying {len(files_to_copy)} files to showcase...")
    if files_to_copy:
        for source_path in files_to_copy:
            relative_path = os.path.relpath(source_path, VAULT_PATH)
            dest_path = os.path.join(SHOWCASE_PATH, relative_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(source_path, dest_path)
            # print(f"  - Copied: {relative_path}") # 可以取消注释来查看每个文件的复制情况
    
    # --- 6. (占位) 未来在这里执行翻译逻辑 ---
    print("\nSkipping translation step (placeholder).")

    # --- 7. 在陈列柜仓库中执行 Git 操作 ---
    if files_to_copy:
        print("\nExecuting Git commands in showcase repository...")
        try:
            run_command(['git', 'add', '.'], SHOWCASE_PATH)
            run_command(['git', 'commit', '-m', COMMIT_MESSAGE], SHOWCASE_PATH)
            # run_command(['git', 'push'], SHOWCASE_PATH) # 已注释掉 push，需要时请手动取消注释或在陈列柜目录手动执行 git push
            print("\n✅ Publishing process completed! Please review and push the changes manually.")
        except Exception as e:
            print(f"\n❌ An error occurred during Git operations: {e}")
    else:
        print("\nNo files found to publish. Nothing to do.")


if __name__ == '__main__':
    main()
