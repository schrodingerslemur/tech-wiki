import os
import re

DOCS_DIR = "docs"
README_FILE = "README.md"

def get_title(file_path):
    """Get the first markdown heading as the title; fallback to filename"""
    # try:
    #     with open(file_path, "r", encoding="utf-8") as f:
    #         for line in f:
    #             line = line.strip()
    #             if line.startswith("# "):
    #                 return line[2:].strip()
    # except Exception:
    #     pass
    # # fallback
    return os.path.splitext(os.path.basename(file_path))[0]

def walk_docs(base_dir):
    toc_lines = []

    for root, dirs, files in os.walk(base_dir):
        dirs.sort()
        files.sort()

        rel_root = os.path.relpath(root, base_dir)

        if rel_root == ".":
            indent_level = 0
        else:
            indent_level = rel_root.count(os.sep)
            indent = "  " * indent_level
            dir_name = os.path.basename(root)
            toc_lines.append(f"{indent}- **{dir_name}/**")

        indent = "  " * (indent_level + 1)

        for f in files:
            if not f.endswith(".md"):
                continue
            if f.lower() == "readme.md":
                continue

            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path)
            title = get_title(full_path)

            toc_lines.append(
                f"{indent}- [{title}]({rel_path.replace(os.sep, '/')})"
            )

    return toc_lines


def main():
    toc = walk_docs(DOCS_DIR)
    content = "# Tech Wiki\n\n"
    content += "This README is auto-generated from `docs/`.\n\n"
    content += "\n".join(toc) + "\n"

    # Only write if changed
    if os.path.exists(README_FILE):
        with open(README_FILE, "r", encoding="utf-8") as f:
            old = f.read()
        if old == content:
            print("README is up-to-date. Nothing changed.")
            return

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Generated {README_FILE} with {len(toc)} entries.")

if __name__ == "__main__":
    main()
