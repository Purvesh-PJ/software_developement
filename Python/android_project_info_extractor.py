import os
import re

# ─── CONFIG ───────────────────────────────────────────────────────────
# Change this to your project folder:
PROJECT_ROOT = r"D:\skin_disease_detection"
OUTPUT_FILE  = "skn_dis_project_summary.md"

# File extensions to include in full text dump
INCLUDE_EXTS = {
    # Source code
    ".kt", ".java", ".py", ".js", ".jsx", ".ts", ".tsx", ".cpp", ".c", ".cs", ".rb", ".php", ".go",
    # Web/markup
    ".html", ".css", ".scss", ".xml", ".json",
    # Config & scripts
    ".gradle", ".properties", ".yaml", ".yml", ".toml",
    # Docs
    ".md"
}

# Specific file names to include
INCLUDE_FILES = {
    "Dockerfile", "Makefile",
    "README", "README.md", "LICENSE",
    "package.json", "tsconfig.json", "babel.config.js", "vite.config.js"
}

# File extensions to explicitly exclude (e.g., logs)
EXCLUDE_EXTS = {".log"}

# Directories and patterns to skip
SKIP_DIRS = {
    # VCS & IDE
    ".git", ".idea", ".vscode",
    # Build & output
    "build", "dist", "out", "bin", "obj", "target", ".gradle", ".next", ".expo", ".angular",
    # Dependencies & caches
    "node_modules", "__pycache__", ".venv", ".pytest_cache", ".mypy_cache",
    # OS files
    ".DS_Store", "Thumbs.db",
    # Log folders
    "logs",
    #
    "data"
}
# ───────────────────────────────────────────────────────────

def should_skip_dir(path):
    return any(part in SKIP_DIRS for part in path.split(os.sep))


def is_valid_file(filepath):
    _, ext = os.path.splitext(filepath)
    name = os.path.basename(filepath)

    # Exclude by extension
    if ext in EXCLUDE_EXTS:
        return False

    # Include only files/extensions explicitly allowed
    return ext in INCLUDE_EXTS or name in INCLUDE_FILES

def generate_tree(root_dir):
    tree_lines = []

    def walk(dir_path, prefix=""):
        # Skip entire directory if it's in SKIP_DIRS
        if should_skip_dir(dir_path):
            return

        try:
            entries = sorted(os.listdir(dir_path))
        except Exception:
            return

        # Filter out skipped entries
        filtered = []
        for entry in entries:
            full_path = os.path.join(dir_path, entry)
            if should_skip_dir(full_path):
                continue
            filtered.append(entry)

        entries_count = len(filtered)

        for i, entry in enumerate(filtered):
            full_path = os.path.join(dir_path, entry)
            connector = "└── " if i == entries_count - 1 else "├── "
            tree_lines.append(f"{prefix}{connector}{entry}")
            if os.path.isdir(full_path):
                extension = "    " if i == entries_count - 1 else "│   "
                walk(full_path, prefix + extension)

    tree_lines.append(f"{os.path.basename(root_dir)}/")
    walk(root_dir)
    return "\n".join(tree_lines)

def extract_symbols(filepath, root_dir):
    rel_path = os.path.relpath(filepath, root_dir)
    symbols = []
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

            if filepath.endswith(".kt") or filepath.endswith(".java"):
                for match in re.finditer(r'\b(class|interface|object|enum|sealed\s+class)\s+(\w+)', content):
                    symbols.append((match.group(2), "class", rel_path))

                for match in re.finditer(r'fun\s+(\w+)\s*\(', content):
                    symbols.append((match.group(1), "function", rel_path))

            elif filepath.endswith(".xml"):
                if "<resources" in content:
                    for match in re.finditer(r'<(color|string|dimen|style|item|bool|integer)\s+name="([^"]+)"', content):
                        symbols.append((match.group(2), f"resource:{match.group(1)}", rel_path))
                elif "<LinearLayout" in content or "<ConstraintLayout" in content or "<RelativeLayout" in content:
                    symbols.append((os.path.basename(filepath), "layout", rel_path))

    except Exception:
        pass
    return symbols

def summarize_file(filepath, root_dir):
    rel_path = os.path.relpath(filepath, root_dir)
    summary = f"### `{rel_path}`\n\n```{filepath.split('.')[-1]}\n"
    try:
        with open(filepath, encoding="utf-8") as f:
            summary += f.read()
    except Exception as e:
        summary += f"_Could not read file: {e}_\n"
    summary += "```\n\n"
    return summary

def scan_project(root_dir):
    summaries = []
    all_symbols = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if should_skip_dir(dirpath):
            dirnames[:] = []  # don't go into subdirs inside skipped dirs
            continue
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if is_valid_file(filepath):
                summaries.append(summarize_file(filepath, root_dir))
                all_symbols.extend(extract_symbols(filepath, root_dir))
    return summaries, all_symbols

def write_summary(root_dir, output_file):
    summaries, all_symbols = scan_project(root_dir)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 🧠 Project Full Summary\n\n")
        f.write(f"- Root Dir: `{root_dir}`\n\n")

        f.write("## 📁 Folder Structure\n\n```\n")
        f.write(generate_tree(root_dir))
        f.write("\n```\n\n")

        f.write("## 🧩 Symbol Index\n\n")
        if not all_symbols:
            f.write("_No symbols extracted._\n\n")
        else:
            f.write("| Symbol           | Type           | Location                       |\n")
            f.write("|------------------|----------------|--------------------------------|\n")
            for name, typ, path in sorted(all_symbols):
                f.write(f"| {name:<16} | {typ:<14} | {path} |\n")
            f.write("\n")

        f.write("## 📄 Included Files (Full Content)\n\n")
        for section in summaries:
            f.write(section)

    print(f"✅ Full summary with folder tree and symbol index written to `{output_file}`")

if __name__ == "__main__":
    write_summary(PROJECT_ROOT, OUTPUT_FILE)
