import os
import yaml
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files

class ExcludePagesPlugin(BasePlugin):
    def on_files(self, files: Files, config):
        # Check if exclusion mode is active (defaults to False if not set)
        exclude_mode = os.getenv("MKDOCS_EXCLUDE_MODE", "false").lower() in ["true", "1"]

        if not exclude_mode:
            return files  # If exclusion is disabled, return all files

        new_files = []
        for file in files:
            if file.src_path.endswith('.md'):
                with open(file.abs_src_path, 'r', encoding='utf-8') as f:
                    try:
                        # Read metadata (YAML front matter)
                        front_matter = list(yaml.safe_load_all(f))
                        if front_matter and isinstance(front_matter[0], dict):
                            if "exclude" in front_matter[0]:
                                continue  # Skip excluded file
                    except yaml.YAMLError:
                        pass  # Ignore YAML errors (probably no front matter)
            new_files.append(file)

        return Files(new_files)
